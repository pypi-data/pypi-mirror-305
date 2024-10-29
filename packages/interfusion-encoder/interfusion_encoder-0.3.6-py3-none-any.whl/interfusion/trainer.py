# interfusion/trainer.py

import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModel
import torch.optim as optim
import torch.nn as nn
from torch.cuda.amp import GradScaler
from tqdm import tqdm
import os
import random
import numpy as np
from collections import defaultdict

from .models import CrossEncoderModel, compute_bi_encoder_embeddings
from .data_utils import CrossEncoderDataset, set_seed
from .config import get_default_config

def train_model(candidates, jobs, positive_matches, candidates_eval=None, jobs_eval=None, positive_matches_eval=None, user_config=None):
    """
    Train the InterFusion Encoder model.

    Parameters:
    - candidates: list of dictionaries representing candidates.
    - jobs: list of dictionaries representing jobs.
    - positive_matches: list of dictionaries representing positive matches.
    - candidates_eval: (optional) list of dictionaries representing evaluation candidates.
    - jobs_eval: (optional) list of dictionaries representing evaluation jobs.
    - positive_matches_eval: (optional) list of dictionaries representing evaluation positive matches.
    - user_config: (optional) dictionary to override default configurations.
    """

    # Merge user configuration with default configuration
    config = get_default_config()
    if user_config:
        config.update(user_config)

    set_seed(config['random_seed'])
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Create directory to save models
    os.makedirs(config['save_dir'], exist_ok=True)

    # Load data
    # Candidates and jobs are passed directly as lists of dictionaries

    # Build mappings
    candidate_id_to_text = {candidate['candidate_id']: candidate['candidate_text'] for candidate in candidates}
    candidate_id_to_features = {candidate['candidate_id']: candidate.get('candidate_features', None) for candidate in candidates}
    job_id_to_text = {job['job_id']: job['job_text'] for job in jobs}
    job_id_to_features = {job['job_id']: job.get('job_features', None) for job in jobs}

    if candidates_eval is None:
        # If evaluation data is not provided, use the training data
        candidates_eval = candidates
        jobs_eval = jobs
        positive_matches_eval = positive_matches

    # Build data_samples
    data_samples = []
    for match in positive_matches:
        candidate_id = match['candidate_id']
        job_id = match['job_id']
        data_samples.append({
            'candidate_id': candidate_id,
            'candidate_text': candidate_id_to_text[candidate_id],
            'positive_job_id': job_id,
            'positive_job_text': job_id_to_text[job_id],
            'candidate_features': candidate_id_to_features.get(candidate_id, None),
            'positive_job_features': job_id_to_features.get(job_id, None)
        })

    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config['cross_encoder_model_name'])

    # Initialize bi-encoder
    bi_encoder = AutoModel.from_pretrained(config['bi_encoder_model_name']).to(device)

    # Implement triangular learning rate scheduler with non-zero starting LR
    lr_start = config['initial_learning_rate']
    lr_max = config['learning_rate']
    num_epochs = config['num_epochs']
    start_mult = lr_start / lr_max  # Multiplier at epoch 0

    def lr_lambda(epoch):
        if epoch <= num_epochs / 2:
            return start_mult + (1.0 - start_mult) * (epoch / (num_epochs / 2))
        else:
            return start_mult + (1.0 - start_mult) * ((num_epochs - epoch) / (num_epochs / 2))

    # If using sparse features, set feature sizes
    candidate_feature_size = 0
    job_feature_size = 0
    if config['use_sparse']:
        # Verify that all candidates and jobs have 'candidate_features' and 'job_features'
        if all('candidate_features' in candidate for candidate in candidates) and all('job_features' in job for job in jobs):
            candidate_feature_lengths = [len(candidate['candidate_features']) for candidate in candidates]
            job_feature_lengths = [len(job['job_features']) for job in jobs]
            candidate_feature_size = max(candidate_feature_lengths)
            job_feature_size = max(job_feature_lengths)
            print(f"Candidate feature size detected and set to: {candidate_feature_size}")
            print(f"Job feature size detected and set to: {job_feature_size}")
        else:
            raise ValueError("All candidates and jobs must have 'candidate_features' and 'job_features' when 'use_sparse' is True.")

    # Load saved model if continue_training is True
    if config.get('continue_training', False):
        saved_model_path = config.get('saved_model_path', None)
        if saved_model_path and os.path.exists(saved_model_path):
            print(f"Loading saved model from {saved_model_path} for continued training...")
            checkpoint = torch.load(saved_model_path, map_location=device)

            # Initialize model
            model = CrossEncoderModel(config, candidate_feature_size, job_feature_size).to(device)

            # Load model state dict
            if 'model_state_dict' in checkpoint:
                model.load_state_dict(checkpoint['model_state_dict'])
                print("Model state dict loaded.")
            else:
                model.load_state_dict(checkpoint)
                print("Loaded model directly from checkpoint (no 'model_state_dict' key).")

            # Initialize optimizer, scheduler, and scaler
            optimizer = optim.AdamW(model.parameters(), lr=config['learning_rate'])
            scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
            scaler = torch.cuda.amp.GradScaler()

            # Load optimizer and scheduler states if available
            if 'optimizer_state_dict' in checkpoint:
                optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
                print("Optimizer state dict loaded.")
            else:
                print("Optimizer state dict not found in checkpoint.")

            if 'scheduler_state_dict' in checkpoint:
                scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
                print("Scheduler state dict loaded.")
            else:
                print("Scheduler state dict not found in checkpoint.")

            if 'scaler_state_dict' in checkpoint:
                scaler.load_state_dict(checkpoint['scaler_state_dict'])
                print("Scaler state dict loaded.")
            else:
                print("Scaler state dict not found in checkpoint.")

            start_epoch = checkpoint.get('epoch', 0) + 1
            print(f"Resuming training from epoch {start_epoch}")
        else:
            print("Saved model path does not exist. Starting training from scratch.")
            start_epoch = 0
            # Initialize model, optimizer, scheduler, and scaler
            model = CrossEncoderModel(config, candidate_feature_size, job_feature_size).to(device)
            optimizer = optim.AdamW(model.parameters(), lr=config['learning_rate'])
            scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
            scaler = torch.cuda.amp.GradScaler()
    else:
        print("Starting training from scratch.")
        start_epoch = 0
        # Initialize model, optimizer, scheduler, and scaler
        model = CrossEncoderModel(config, candidate_feature_size, job_feature_size).to(device)
        optimizer = optim.AdamW(model.parameters(), lr=config['learning_rate'])
        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
        scaler = torch.cuda.amp.GradScaler()

    # Precompute negatives using bi-encoder
    print("Precomputing negatives using bi-encoder...")
    negatives = precompute_bi_encoder_negatives(bi_encoder, tokenizer, candidates, jobs, positive_matches, config)

    # Generate initial hard negatives
    print("Generating initial hard negatives...")
    hard_negatives = generate_hard_negatives(model, data_samples, tokenizer, negatives, config, candidate_feature_size, job_feature_size)

    # Precompute N random negatives per candidate
    print("Precomputing random negatives...")
    random_negatives = precompute_random_negatives(candidates, jobs, positive_matches, config)

    # Initialize dataset with initial hard negatives and random negatives
    train_dataset = CrossEncoderDataset(
        data_samples, tokenizer, config, negatives=negatives,
        hard_negatives=hard_negatives, random_negatives=random_negatives
    )
    train_dataset.update_hard_negatives(hard_negatives)
    train_dataset.update_random_negatives(random_negatives)

    best_metric = 0.0  # Initialize best metric (e.g., Precision@5)
    for epoch in range(start_epoch, num_epochs):
        # Resample random negatives every epoch
        random_negatives = precompute_random_negatives(candidates, jobs, positive_matches, config)
        train_dataset.update_random_negatives(random_negatives)

        # Regenerate hard negatives every epoch if desired
        if (epoch + 1) % config['hard_negative_sampling_frequency'] == 0:
            print(f"Generating hard negatives for epoch {epoch+1}...")
            hard_negatives = generate_hard_negatives(model, data_samples, tokenizer, negatives, config, candidate_feature_size, job_feature_size)
            train_dataset.update_hard_negatives(hard_negatives)

        # Train for one epoch
        train(model, train_dataset, optimizer, device, config, epoch, scaler, scheduler)

        # Evaluate the model
        avg_precisions = evaluate(model, tokenizer, candidates_eval, jobs_eval, positive_matches_eval, config, bi_encoder, epoch)

        # Check if Precision@5 improved
        if 5 in avg_precisions:
            current_metric = avg_precisions[5]  # Precision at 5
            if current_metric > best_metric:
                best_metric = current_metric
                # Save the model
                model_save_path = os.path.join(config['save_dir'], f"interfusion_best_p5_{best_metric:.4f}.pt")
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': model.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'scheduler_state_dict': scheduler.state_dict(),
                    'scaler_state_dict': scaler.state_dict(),
                }, model_save_path)
                print(f"New best Precision@5: {best_metric:.4f}. Model saved to {model_save_path}")
                # Log model checkpoint to W&B
        else:
            print("Precision@5 not available in evaluation results.")

    # Optionally, save the final model
    final_model_save_path = os.path.join(config['save_dir'], "interfusion_final.pt")
    torch.save({
        'epoch': num_epochs - 1,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict(),
        'scaler_state_dict': scaler.state_dict(),
    }, final_model_save_path)
    print(f"Final model saved to {final_model_save_path}")

# Include all the helper functions used in training
def precompute_bi_encoder_negatives(bi_encoder, tokenizer, candidates, jobs, positive_matches, config):
    bi_encoder.to('cuda' if torch.cuda.is_available() else 'cpu')
    candidate_texts = [candidate['candidate_text'] for candidate in candidates]
    candidate_ids = [candidate['candidate_id'] for candidate in candidates]
    job_texts = [job['job_text'] for job in jobs]
    job_ids = [job['job_id'] for job in jobs]

    # Compute embeddings
    print("Computing candidate embeddings...")
    candidate_embeddings = compute_bi_encoder_embeddings(bi_encoder, tokenizer, candidate_texts, config)
    print("Computing job embeddings...")
    job_embeddings = compute_bi_encoder_embeddings(bi_encoder, tokenizer, job_texts, config)

    # Normalize embeddings
    candidate_embeddings = nn.functional.normalize(candidate_embeddings, p=2, dim=1)
    job_embeddings = nn.functional.normalize(job_embeddings, p=2, dim=1)

    # Build mappings
    candidate_id_to_idx = {cid: idx for idx, cid in enumerate(candidate_ids)}
    job_id_to_idx = {jid: idx for idx, jid in enumerate(job_ids)}
    positive_pairs = set((match['candidate_id'], match['job_id']) for match in positive_matches)

    M = config['M']
    use_sparse = config['use_sparse']

    # Precompute negatives
    negatives = {}
    for candidate in tqdm(candidates, desc="Precomputing negatives"):
        candidate_id = candidate['candidate_id']
        c_idx = candidate_id_to_idx[candidate_id]
        c_emb = candidate_embeddings[c_idx].unsqueeze(0)  # Shape: [1, dim]

        # Compute similarities
        similarities = torch.matmul(c_emb, job_embeddings.t()).squeeze(0)  # Shape: [num_jobs]
        similarities = similarities.cpu().numpy()

        # Exclude positive jobs
        positive_job_ids = [match['job_id'] for match in positive_matches if match['candidate_id'] == candidate_id]
        positive_job_indices = [job_id_to_idx[jid] for jid in positive_job_ids]
        similarities[positive_job_indices] = -np.inf  # Exclude positives by setting similarity to -inf

        # Get top M negatives
        start_rank = 1000
        end_rank = start_rank + M
        top_m_indices = np.argpartition(-similarities, end_rank-1)[start_rank:end_rank]
        negative_job_ids = [job_ids[idx] for idx in top_m_indices]
        negative_job_texts = [job_texts[idx] for idx in top_m_indices]

        negatives[candidate_id] = {
            'job_ids': negative_job_ids,
            'job_texts': negative_job_texts
        }

        if use_sparse:
            negative_job_features = [jobs[idx].get('job_features', None) for idx in top_m_indices]
            if 'negative_job_features' not in negatives:
                negatives['negative_job_features'] = {}
            negatives['negative_job_features'][candidate_id] = negative_job_features

    return negatives
    
    
def generate_hard_negatives(model, data_samples, tokenizer, negatives, config, candidate_feature_size, job_feature_size):
    # Function to generate hard negatives from precomputed negatives
    model.eval()
    device = next(model.parameters()).device
    N = config['N']
    batch_size = config['negative_batch_size']
    use_sparse = config['use_sparse']

    # Collect all candidate-negative pairs (from precomputed M negatives)
    candidate_texts = []
    negative_job_texts = []
    candidate_features_list = []
    negative_job_features_list = []
    candidate_ids = []
    negative_job_ids = []

    for sample in data_samples:
        candidate_id = sample['candidate_id']
        candidate_text = sample['candidate_text']
        candidate_features = sample.get('candidate_features', None)

        # Use precomputed M negatives
        neg_job_texts = negatives[candidate_id]['job_texts']  # List of M negative job texts
        neg_job_ids = negatives[candidate_id]['job_ids']      # List of M negative job IDs
        if use_sparse:
            neg_features_list = negatives['negative_job_features'][candidate_id]
        else:
            neg_features_list = [None] * len(neg_job_texts)

        candidate_texts.extend([candidate_text] * len(neg_job_texts))
        negative_job_texts.extend(neg_job_texts)
        negative_job_ids.extend(neg_job_ids)
        candidate_features_list.extend([candidate_features] * len(neg_job_texts))
        negative_job_features_list.extend(neg_features_list)
        candidate_ids.extend([candidate_id] * len(neg_job_texts))

    # Now process all candidate-negative pairs in batches
    total_pairs = len(candidate_texts)
    scores = []
    with torch.no_grad():
        for i in tqdm(range(0, total_pairs, batch_size), desc="Generating hard negatives"):
            batch_candidate_texts = candidate_texts[i:i+batch_size]
            batch_negative_job_texts = negative_job_texts[i:i+batch_size]
            inputs = tokenizer(batch_candidate_texts, batch_negative_job_texts, max_length=config['max_length'],
                               truncation=True, padding=True, return_tensors='pt')
            input_ids = inputs['input_ids'].to(device)
            attention_mask = inputs['attention_mask'].to(device)
            if use_sparse:
                batch_candidate_features = candidate_features_list[i:i+batch_size]
                batch_negative_job_features = negative_job_features_list[i:i+batch_size]
                features_list = []
                for cf, nf in zip(batch_candidate_features, batch_negative_job_features):
                    features = {
                        'candidate_features': torch.tensor(cf, dtype=torch.float) if cf is not None else torch.zeros(candidate_feature_size),
                        'job_features': torch.tensor(nf, dtype=torch.float) if nf is not None else torch.zeros(job_feature_size)
                    }
                    features_list.append(features)
                # Prepare features
                features_padded = CrossEncoderDataset.pad_features_static(features_list, candidate_feature_size, job_feature_size)
                features_tensor = features_padded.to(device)
            else:
                features_tensor = None

            if use_sparse and features_tensor is not None:
                logits = model(input_ids=input_ids, attention_mask=attention_mask, features=features_tensor)
            else:
                logits = model(input_ids=input_ids, attention_mask=attention_mask)
            batch_scores = logits.cpu().tolist()
            scores.extend(batch_scores)

    # Now collect scores per candidate
    from collections import defaultdict
    candidate_negatives = defaultdict(list)
    candidate_scores = defaultdict(list)
    for cid, neg_id, neg_text, neg_features, score in zip(candidate_ids, negative_job_ids, negative_job_texts, negative_job_features_list, scores):
        candidate_negatives[cid].append({
            'job_id': neg_id,
            'job_text': neg_text,
            'job_features': neg_features  # Include features here
        })
        candidate_scores[cid].append(score)

    # Now select top N hard negatives per candidate
    hard_negatives = {}
    for cid in candidate_negatives:
        neg_list = candidate_negatives[cid]
        neg_scores = candidate_scores[cid]
        # Get indices of top N scores
        top_indices = np.argsort(-np.array(neg_scores))[:N]
        hard_neg_list = [neg_list[i] for i in top_indices]
        job_ids = [item['job_id'] for item in hard_neg_list]
        job_texts = [item['job_text'] for item in hard_neg_list]
        if use_sparse:
            job_features = [item['job_features'] for item in hard_neg_list]
        hard_negatives[cid] = {
            'job_ids': job_ids,
            'job_texts': job_texts
        }
        if use_sparse:
            hard_negatives[cid]['job_features'] = job_features

    return hard_negatives  # Return the hard negatives separately

    
    
def precompute_random_negatives(candidates, jobs, positive_matches, config):
    # Function to precompute N random negatives per candidate
    job_ids = [job['job_id'] for job in jobs]
    job_id_to_text = {job['job_id']: job['job_text'] for job in jobs}
    job_id_to_features = {job['job_id']: job.get('job_features', None) for job in jobs}
    positive_job_ids_per_candidate = {}
    for match in positive_matches:
        cid = match['candidate_id']
        jid = match['job_id']
        if cid not in positive_job_ids_per_candidate:
            positive_job_ids_per_candidate[cid] = set()
        positive_job_ids_per_candidate[cid].add(jid)
    N = config['N']
    use_sparse = config['use_sparse']
    random_negatives = {}
    if use_sparse:
        random_negatives['negative_job_features'] = {}
    for candidate in candidates:
        cid = candidate['candidate_id']
        positive_jids = positive_job_ids_per_candidate.get(cid, set())
        negative_jids = list(set(job_ids) - positive_jids)
        if len(negative_jids) >= N:
            sampled_neg_jids = random.sample(negative_jids, N)
        else:
            sampled_neg_jids = random.choices(negative_jids, k=N)
        neg_job_texts = [job_id_to_text[jid] for jid in sampled_neg_jids]
        if use_sparse:
            neg_features_list = [job_id_to_features[jid] for jid in sampled_neg_jids]
            random_negatives['negative_job_features'][cid] = neg_features_list
        random_negatives[cid] = {
            'job_ids': sampled_neg_jids,
            'job_texts': neg_job_texts
        }
    return random_negatives

def train(model, train_dataset, optimizer, device, config, epoch, scaler, scheduler):
    # Training function with mixed precision and listwise ranking loss
    model.train()
    train_dataloader = DataLoader(
        train_dataset,
        batch_size=config['train_batch_size'],  # Number of data samples per batch
        shuffle=True,
        collate_fn=train_dataset.collate_fn,
        num_workers=config['num_workers'],
        pin_memory=True
    )
    total_loss = 0
    criterion = nn.CrossEntropyLoss()
    for batch in tqdm(train_dataloader, desc=f"Training Epoch {epoch+1}"):
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels']
        candidate_to_indices = batch['candidate_to_indices']
        optimizer.zero_grad()
        with torch.cuda.amp.autocast():
            if model.use_sparse:
                features = batch['features'].to(device)
                logits = model(input_ids=input_ids, attention_mask=attention_mask, features=features)
            else:
                logits = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = 0.0
            for candidate_id, indices in candidate_to_indices.items():
                candidate_logits = logits[indices]  # Shape: [num_samples]
                candidate_labels = labels[indices]  # Shape: [num_samples]
                # The target is the index of the positive sample
                positive_indices = (candidate_labels == 1).nonzero(as_tuple=True)[0]
                if positive_indices.numel() == 0:
                    continue  # Skip if no positive sample
                target = positive_indices[0].to(device)
                candidate_logits = candidate_logits.unsqueeze(0)  # Shape: [1, num_samples]
                loss_candidate = criterion(candidate_logits, target.unsqueeze(0))
                loss += loss_candidate
            if len(candidate_to_indices) > 0:
                loss = loss / len(candidate_to_indices)
            else:
                loss = torch.tensor(0.0, requires_grad=True).to(device)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
        total_loss += loss.item()
    avg_loss = total_loss / len(train_dataloader)
    print(f"Average training loss: {avg_loss:.4f}")
    # Update learning rate
    scheduler.step()
    current_lr = scheduler.get_last_lr()[0]
    print(f"Current learning rate: {current_lr:.6f}")
    # Log training loss and learning rate to W&B

def evaluate(model, tokenizer, candidates_eval, jobs_eval, positive_matches_eval, config, bi_encoder, epoch):
    model.eval()
    device = next(model.parameters()).device
    Ns = config['eval_Ns']
    K = config.get('eval_K', 50)  # Number of top jobs to retrieve using bi-encoder

    # Build candidate and job texts and IDs
    candidate_texts = [candidate['candidate_text'] for candidate in candidates_eval]
    candidate_ids = [candidate['candidate_id'] for candidate in candidates_eval]
    job_texts = [job['job_text'] for job in jobs_eval]
    job_ids = [job['job_id'] for job in jobs_eval]

    # Create a mapping from job_text to job_id
    job_text_to_id = {job['job_text']: job['job_id'] for job in jobs_eval}

    # Create a mapping from candidate_id to ground truth job_ids
    candidate_to_jobs = {}
    for match in positive_matches_eval:
        cid = match['candidate_id']
        jid = match['job_id']
        if cid not in candidate_to_jobs:
            candidate_to_jobs[cid] = set()
        candidate_to_jobs[cid].add(jid)

    # Compute embeddings using bi-encoder
    print("Computing candidate embeddings for evaluation...")
    candidate_embeddings = compute_bi_encoder_embeddings(bi_encoder, tokenizer, candidate_texts, config)
    print("Computing job embeddings for evaluation...")
    job_embeddings = compute_bi_encoder_embeddings(bi_encoder, tokenizer, job_texts, config)

    # Normalize embeddings
    candidate_embeddings = nn.functional.normalize(candidate_embeddings, p=2, dim=1)
    job_embeddings = nn.functional.normalize(job_embeddings, p=2, dim=1)

    # Compute similarity scores between all candidates and jobs
    similarities = torch.matmul(candidate_embeddings, job_embeddings.t())  # Shape: [num_candidates, num_jobs]
    similarities = similarities.cpu().numpy()

    ### Evaluation using bi-encoder similarities ###
    print("\nEvaluating using bi-encoder similarities...")
    precisions_at_N_bi = {N: [] for N in Ns}
    for idx, candidate_id in enumerate(candidate_ids):
        sim_scores = similarities[idx]  # Similarities for this candidate to all jobs
        # Get indices sorted by similarity in descending order
        sorted_indices = np.argsort(-sim_scores)
        sorted_job_ids = [job_ids[i] for i in sorted_indices]
        ground_truth_job_ids = candidate_to_jobs.get(candidate_id, set())
        for N in Ns:
            top_N_job_ids = sorted_job_ids[:N]
            hits = ground_truth_job_ids.intersection(top_N_job_ids)
            precision = len(hits) / N
            precisions_at_N_bi[N].append(precision)

    # Compute average precision at each N for bi-encoder
    avg_precisions_bi = {}
    print("\nAverage Precision at N using bi-encoder:")
    for N in Ns:
        avg_precision = np.mean(precisions_at_N_bi[N]) if precisions_at_N_bi[N] else 0.0
        avg_precisions_bi[N] = avg_precision
        print(f"Precision at {N}: {avg_precision:.4f}")

    ### Proceed with cross-encoder evaluation as before ###
    # For each candidate, get top K jobs and prepare cross-encoder inputs
    all_candidate_texts = []
    all_job_texts = []
    all_candidate_ids = []

    for idx, candidate_id in enumerate(candidate_ids):
        sim_scores = similarities[idx]
        top_k_indices = np.argpartition(-sim_scores, K-1)[:K]
        top_k_job_texts = [job_texts[i] for i in top_k_indices]
        candidate_text = candidate_texts[idx]
        num_jobs = len(top_k_job_texts)
        all_candidate_texts.extend([candidate_text] * num_jobs)
        all_job_texts.extend(top_k_job_texts)
        all_candidate_ids.extend([candidate_id] * num_jobs)

    # Prepare cross-encoder inputs
    print("\nEvaluating with cross-encoder...")
    total_pairs = len(all_candidate_texts)
    scores = []
    with torch.no_grad():
        for i in tqdm(range(0, total_pairs, config['negative_batch_size']), desc="Evaluating"):
            batch_candidate_texts = all_candidate_texts[i:i+config['negative_batch_size']]
            batch_job_texts = all_job_texts[i:i+config['negative_batch_size']]
            inputs = tokenizer(batch_candidate_texts, batch_job_texts, max_length=config['max_length'], truncation=True,
                               padding=True, return_tensors='pt')
            input_ids = inputs['input_ids'].to(device)
            attention_mask = inputs['attention_mask'].to(device)
            logits = model(input_ids=input_ids, attention_mask=attention_mask)
            batch_scores = logits.cpu().tolist()
            scores.extend(batch_scores)

    # Collect scores per candidate
    from collections import defaultdict
    candidate_job_scores = defaultdict(list)
    candidate_job_ids = defaultdict(list)
    idx = 0
    for cid, job_text in zip(all_candidate_ids, all_job_texts):
        candidate_job_scores[cid].append(scores[idx])
        candidate_job_ids[cid].append(job_text_to_id[job_text])
        idx += 1

    # Compute precision at N using cross-encoder
    precisions_at_N_cross = {N: [] for N in Ns}
    for candidate_id in candidate_ids:
        job_scores = candidate_job_scores[candidate_id]
        job_ids_list = candidate_job_ids[candidate_id]
        sorted_indices = np.argsort(-np.array(job_scores))
        sorted_job_ids = [job_ids_list[i] for i in sorted_indices]
        ground_truth_job_ids = candidate_to_jobs.get(candidate_id, set())
        for N in Ns:
            top_N_job_ids = sorted_job_ids[:N]
            hits = ground_truth_job_ids.intersection(top_N_job_ids)
            precision = len(hits) / N
            precisions_at_N_cross[N].append(precision)

    # Compute average precision at each N for cross-encoder
    avg_precisions = {}
    print("\nAverage Precision at N using cross-encoder:")
    for N in Ns:
        avg_precision = np.mean(precisions_at_N_cross[N]) if precisions_at_N_cross[N] else 0.0
        avg_precisions[N] = avg_precision
        print(f"Precision at {N}: {avg_precision:.4f}")

    # Log evaluation metrics to W&B
    metrics = {f"Precision@{N}": avg_precisions[N] for N in Ns}
    metrics.update({f"BiEncoder Precision@{N}": avg_precisions_bi[N] for N in Ns})
    metrics["Epoch"] = epoch + 1

    return avg_precisions

