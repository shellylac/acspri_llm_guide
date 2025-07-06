---
id: compare_embeddings_cosine
title: Compare Sentence Embeddings (Cosine Similarity)
type: module
tags: [similarity, embeddings, cosine, NLP, sentence-transformers]
version: 1.0
dependencies:
  - numpy
  - scikit-learn
---

# 📐 Module: Compare Sentence Embeddings (Cosine Similarity

## 📌 Purpose

This module allows you to **compare the similarity between two or more sentences**, once they’ve been transformed into embeddings using a model like `sentence-transformers`.

The comparison is done using **cosine similarity**, which provides a score between `-1` and `1`:
- `1.0` → identical direction (perfect semantic alignment)
- `0.0` → orthogonal (no semantic similarity)
- `-1.0` → opposite meaning (rare in practice)

---

## 🧠 Why This Module?

After you generate sentence embeddings, the *raw vectors* are not human-readable.  
This module provides a way to **extract meaning** from embeddings by calculating **semantic closeness** between them.

It’s ideal for:
- Evaluating model behavior
- Measuring the similarity between paraphrases
- Detecting stance alignment or opposition
- Flagging redundancy or conflict in text

---

## ⚙️ Function: `compare_embedding_pairs`

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compare_embedding_pairs(text_list, embeddings, round_score=3):
    """
    Compare sentence embeddings and return a readable summary of pairwise cosine similarity.

    Parameters:
        text_list (list of str): List of original sentences
        embeddings (np.ndarray): Embeddings array (n_sentences x embedding_dim)
        round_score (int): Number of decimal places to round to (default: 3)

    Returns:
        List of tuples: (Sentence A, Sentence B, Similarity Score)
    """
    sim_matrix = cosine_similarity(embeddings)
    n = len(text_list)
    results = []

    for i in range(n):
        for j in range(i+1, n):
            results.append((
                text_list[i],
                text_list[j],
                round(sim_matrix[i, j], round_score)
            ))

    return results
```

---

## 🧪 Example Usage

```python
from sentence_transformers import SentenceTransformer
from compare_embeddings_cosine import compare_embedding_pairs

sentences = [
    "The minister supported the bill.",
    "The bill was passed unanimously.",
    "Citizens protested the legislation."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)

similarities = compare_embedding_pairs(sentences, embeddings)

for a, b, score in similarities:
    print(f""{a}"  ⟷  "{b}"  →  Score: {score}")
```

---

## 📊 Sample Output

```
"The minister supported the bill." ⟷ "The bill was passed unanimously." → Score: 0.89
"The minister supported the bill." ⟷ "Citizens protested the legislation." → Score: 0.31
"The bill was passed unanimously." ⟷ "Citizens protested the legislation." → Score: 0.27
```

This clearly shows that sentence 1 and 2 are close in meaning, while sentence 3 diverges in tone or stance.

---

## 🧪 Tips for Use

| Tip | Explanation |
|-----|-------------|
| Normalize input | Lowercasing, stripping whitespace, etc. helps consistency |
| Use sentence units | Avoid paragraphs — embeddings assume one complete thought per unit |
| Round conservatively | Rounding to 3 decimals usually balances interpretability and resolution |
| Visualize | Use seaborn heatmap or PCA to complement raw scores |

---

## 🧱 Related Modules

| Module                         | Description                                                  |
|--------------------------------|--------------------------------------------------------------|
| `embed_text_hf_basic.md`       | Generates sentence embeddings                                |
| `embed_compare_cosine.md`      | Builds full similarity matrix (useful for heatmaps)          |
| `embedding_pipeline.md`        | Complete pipeline for embedding → similarity → visualization |
| `day2_llm_meaning_instruments.ipynb` | Notebook where this module is used in live coding           |

---
