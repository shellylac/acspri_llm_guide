
# 🧠 Module: `embed_text_hf_basic.md`

## 📌 Purpose

This module provides a structured way to **generate sentence embeddings** using Hugging Face models via the `sentence-transformers` library.  
Embeddings convert raw text into **high-dimensional vectors** that encode **semantic meaning**.

These vectors are foundational for:
- Calculating similarity (e.g., cosine distance)
- Clustering open-ended responses
- Classifying sentiment or stance
- Detecting semantic drift
- Powering downstream tools (e.g., Trigger Detectors, RAG agents)

---

## 📚 Background: What Are Sentence Embeddings?

A **sentence embedding** is a numeric representation of a full sentence or paragraph that captures its **meaning** in context — not just individual word definitions.

- These embeddings are vectors: arrays of real numbers (e.g., 384 dimensions)
- Vectors that are **close together** (small cosine distance) represent **semantically similar** sentences
- The model is trained to bring similar ideas close, and dissimilar ideas far apart

Example:

| Sentence A | Sentence B | Cosine Similarity |
|------------|------------|-------------------|
| “I support the bill.” | “The proposal is good.” | 0.82 |
| “I support the bill.” | “The policy was terrible.” | 0.22 |

---

## 🧠 Why `sentence-transformers`?

Unlike traditional Hugging Face models that return token-level outputs, the `sentence-transformers` library:

- Pools token embeddings into a **single sentence vector**
- Is **fine-tuned specifically for semantic similarity**
- Provides optimized models like `all-MiniLM-L6-v2`, `mpnet`, `multi-qa`, etc.
- Includes batching, GPU/CPU handling, and fast inference

---

## 🧪 Model Used: `all-MiniLM-L6-v2`

> ✅ Default model used in this course and MVP

### 🔍 Why this model?

- **Compact** (66M parameters): fast on CPU/Colab
- **384-dimensional vectors**: compact yet expressive
- Fine-tuned for **semantic similarity**, not just general language modeling
- Well-balanced performance on many tasks, including:
  - Text clustering
  - Paraphrase detection
  - Semantic search
  - Research qualitative coding

### 📘 Citation:
> [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) by SBERT.net (Reimers et al.)

---

## ⚙️ Function: `embed_sentences()`

```python
from sentence_transformers import SentenceTransformer

def embed_sentences(sentences, model_name='all-MiniLM-L6-v2'):
    '''
    Converts a list of sentences into dense semantic vectors using a pretrained model.

    Parameters:
        sentences (List[str]): List of sentences or short texts to embed
        model_name (str): Pretrained sentence transformer model from Hugging Face

    Returns:
        np.ndarray: A matrix of shape (n_sentences, embedding_dim), e.g., (5, 384)
    '''
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)
    return embeddings
```

---

## 🧪 Example Usage

```python
sentences = [
    "The minister supported the bill.",
    "The minister opposed the bill.",
    "The policy was popular.",
    "Many citizens disagreed with the proposal."
]

vectors = embed_sentences(sentences)
vectors.shape  # ➜ (4, 384)
```

---

## 🔍 Vector Output: What Does It Look Like?

The output of `model.encode()` is a NumPy array:

```python
array([[ 0.0123, 0.0842, -0.0031, ..., 0.0311],
       [-0.0034, 0.0722,  0.0124, ..., 0.0292],
       ... ])
```

- Each row = a sentence
- Each column = a latent semantic dimension
- These dimensions are **not human-readable**, but **relational** (e.g., sentiment, stance, objectivity, etc.)

---

## 🔁 Common Follow-Ups

| Task | Next Module |
|------|-------------|
| Compute semantic similarity | `compare_embeddings_cosine.md` |
| Visualize in 2D | `visualize_embeddings_pca.md` |
| Cluster sentence groups | `cluster_sentences_kmeans.md` |
| Classify sentiment | `embed_classify_loop.md` |

---
## 🧱 Related Modules

| Module                                   | Description                                               |
|------------------------------------------|-----------------------------------------------------------|
| `embed_compare_cosine.md`                | Compute cosine similarity between sentence embeddings     |
| `embedding_pipeline.md`                  | Full pipeline: embed → compare → visualize                |
| `embeddings-and-similarity-scores.ipynb` | Interactive notebook using this module in Day 2 Session 1 |
