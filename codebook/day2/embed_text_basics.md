---
id: embed_text_basics
title: Embed Text (Sentence Transformers)
type: module
tags: [embeddings, sentence-transformers, NLP, feature-extraction]
author: Maria Aise
version: 1.0
dependencies:
  - sentence-transformers
  - numpy
  - torch
---

# 🧠 Module: `embed_text_basics.md`

## 🔍 Purpose

This module converts natural language sentences into dense numerical vectors using pretrained **sentence-level transformer models**.

These embeddings are designed to capture **semantic similarity** — meaning that two sentences with similar intent or meaning will produce **vectors that are close in vector space**. The output vectors can then be used in:

- Similarity comparison
- Clustering
- Text classification
- Semantic search
- Retrieval-Augmented Generation (RAG) workflows

---

## 🔧 Model Used

By default, this module uses:

`
- all-MiniLM-L6-v2`
From the sentence-transformers library by SBERT

- 384-dimensional output vectors

Fast and lightweight — ideal for interactive sessions and fast prototyping

Trained on SNLI, STS, NLI — excellent at semantic similarity tasks

Other model options:

- `multi-qa-MiniLM-L6-cos-v1` – trained for QA search

`paraphrase-mpnet-base-v2` – higher performance, slower

`text-embedding-3-small` – for OpenAI-based workflows (external variant)

### 🧾 Inputs
| Parameter    | Type        | Description                                                    |
| ------------ | ----------- | -------------------------------------------------------------- |
| `sentences`  | `List[str]` | List of complete sentences (not fragments or documents)        |
| `model_name` | `str`       | *(Optional)* Name of pretrained model to load from HuggingFace |


📌 Always provide sentences as clean, standalone units. Avoid long paragraphs or broken fragments.

### 🧪 Example Usage
``` python
from sentence_transformers import SentenceTransformer

def embed_sentences(sentences, model_name="all-MiniLM-L6-v2"):
    """
    Embeds a list of sentences using a pretrained sentence-transformers model.
    
    Parameters:
        sentences (List[str]): List of full sentences to embed
        model_name (str): Optional transformer model name
        
    Returns:
        np.ndarray: Embeddings of shape (n_sentences, embedding_dim)
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)
    return embeddings
```
### 🔍 Example Call
```python
sentences = [
    "The government passed a new education bill.",
    "Parliament approved a law about education.",
    "Cats are wonderful pets.",
    "Dogs make great companions."
]

embeddings = embed_sentences(sentences)
print(embeddings.shape)
# Output: (4, 384)
```

### 📤 Output
The output is a NumPy array with shape (n_sentences, embedding_dim) — where embedding_dim is typically 384 for MiniLM.

Each row is a dense vector representing one sentence’s position in semantic space.

| Sentence                                      | Embedding (truncated view)       |
| --------------------------------------------- | -------------------------------- |
| "The government passed a new education bill." | `[0.12, 0.34, -0.11, ..., 0.08]` |
| "Cats are wonderful pets."                    | `[0.03, -0.56, 0.42, ..., 0.21]` |

### 🧱 Related Modules
| Module                                   | Description                                               |
| ---------------------------------------- | --------------------------------------------------------- |
| `embed_compare_cosine.md`                | Compute cosine similarity between sentence embeddings     |
| `embedding_pipeline.md`                  | Full pipeline: embed → compare → visualize                |
| `embeddings-and-similarity-scores.ipynb` | Interactive notebook using this module in Day 2 Session 1 |

