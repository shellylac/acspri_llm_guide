---

---

# 📊 Meaning Matrix Heatmap

## 📌 Purpose

This module visualizes **pairwise semantic similarity** between sentences using a **heatmap**.  
It is ideal for detecting:
- Framing shifts
- Semantic drift
- Clustering patterns
- Opinion divergence
- Redundant or conflicting content

---

## 🧠 Why Use a Heatmap?

While raw cosine scores help compare **pairs**, a heatmap:
- Shows all sentence relationships at once
- Highlights clusters of semantic similarity
- Visually surfaces **outliers**, **near-duplicates**, and **stance shifts**

It’s especially helpful for:
- **Qualitative analysis** (e.g., interviews, open-ended surveys)
- **Narrative monitoring** (e.g., political discourse or media frames)
- **Trigger detection** (e.g., tone shifts across audiences)

---

## ⚙️ Function

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def plot_meaning_heatmap(sentences, embeddings, figsize=(8, 6), annot=True, cmap="coolwarm"):
    """
    Plots a cosine similarity heatmap for sentence embeddings.

    Parameters:
        sentences (list of str): Original sentence labels
        embeddings (np.ndarray): Sentence embedding matrix (n x d)
        figsize (tuple): Figure size
        annot (bool): Annotate cells with values
        cmap (str): Color palette

    Returns:
        None (displays a heatmap plot)
    """
    sim_matrix = cosine_similarity(embeddings)

    plt.figure(figsize=figsize)
    sns.heatmap(sim_matrix, xticklabels=sentences, yticklabels=sentences,
                annot=annot, cmap=cmap, fmt=".2f", square=True)
    plt.title("Semantic Similarity Matrix (Cosine)")
    plt.tight_layout()
    plt.show()
```

---

## 🧪 Example Usage

```python
from sentence_transformers import SentenceTransformer
from meaning_matrix_heatmap import plot_meaning_heatmap

sentences = [
    "The protest was peaceful.",
    "The riot turned violent.",
    "The demonstration drew a crowd.",
    "The violent clash disrupted traffic."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)

plot_meaning_heatmap(sentences, embeddings)
```

---

## 📈 What You’ll See

- Sentences with **close meaning** → warm colors (red/orange)
- Sentences with **different framing or stance** → cool colors (blue)

The matrix lets you *diagnose framing*, e.g.:
- “Protest” vs “Riot”
- “Disagreement” vs “Outrage”
- “Assistance” vs “Welfare”

---

## 🔁 Practical Use Cases

| Use Case | Example |
|----------|---------|
| Interview clustering | Group participant sentiments across questions |
| Media monitoring | Spot diverging language around same event |
| Survey harmonization | Collapse near-duplicate responses |
| Policy audit | Detect shifts in framing between political actors |
| Trigger systems | Flag unusually dissonant phrasings |

---

## 🧱 Related Modules

| Module                             | Description                                     |
|------------------------------------|-------------------------------------------------|
| `embed_text_hf_basic.md`           | Generates sentence embeddings                   |
| `compare_embeddings_cosine.md`     | Computes cosine scores between sentence pairs   |
| `semantic_drift_pipeline.md`       | Identifies topic/stance shifts over time        |
| `day2_llm_meaning_instruments.ipynb` | Notebook that uses this module interactively   |

---

## 🪪 Author  
*Maria Aise — Modular Codebook, ACSPRI 2025*  
Designed for visualizing latent meaning space in social science, narrative, and brand logic contexts.
