---
id: visualize_embeddings_pca
title: Visualize Sentence Embeddings with PCA
type: module
tags: [PCA, visualization, embeddings, dimensionality reduction, NLP]
version: 1.0
dependencies:
  - numpy
  - matplotlib
  - sklearn
---

# 📉 Module: Visualize Sentence Embeddings with PCA

## 📌 Purpose

This module reduces high-dimensional **sentence embeddings** to **2D** using **Principal Component Analysis (PCA)**, allowing you to **visualize meaning relationships** between sentences.

Sentence embeddings typically exist in 384- or 768-dimensional space, which is impossible to visualize directly.  
By projecting them into 2D, you can observe:

- **Clusters of semantically similar sentences**
- **Outliers or unusual responses**
- **Topic grouping or sentiment separation**
- **Narrative consistency or conflict**

---

## 🧠 Why PCA?

**PCA** is a technique that projects data onto axes that maximize variance.  
For text embeddings:

- PCA is **fast** and **deterministic** (unlike t-SNE/UMAP)
- Good for **teaching and debugging**
- Helps explore **semantic alignment and drift**

---

## ⚙️ Function

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def plot_pca_embeddings(embeddings, labels=None, sentences=None, figsize=(8, 6), title="PCA Projection of Sentence Embeddings"):
    """
    Projects sentence embeddings into 2D and visualizes using PCA.

    Parameters:
        embeddings (np.ndarray): Sentence embedding matrix (n x d)
        labels (List[str], optional): Labels or categories (e.g., sentiment, source)
        sentences (List[str], optional): Raw text to annotate points
        figsize (tuple): Matplotlib figure size
        title (str): Title of the plot

    Returns:
        None (displays 2D scatterplot)
    """
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)

    plt.figure(figsize=figsize)

    if labels:
        unique = sorted(set(labels))
        for group in unique:
            idx = [i for i, l in enumerate(labels) if l == group]
            plt.scatter(reduced[idx, 0], reduced[idx, 1], label=group)
        plt.legend()
    else:
        plt.scatter(reduced[:, 0], reduced[:, 1])

    if sentences:
        for i, text in enumerate(sentences):
            plt.annotate(f"{i+1}", (reduced[i, 0], reduced[i, 1]), fontsize=8)

    plt.title(title)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
```

---

## 🧪 Example Usage

```python
from sentence_transformers import SentenceTransformer
from visualize_embeddings_pca import plot_pca_embeddings

sentences = [
    "The protest remained peaceful.",
    "The riot caused chaos.",
    "The demonstration gathered support.",
    "Police clashed with violent crowds."
]

labels = ["neutral", "negative", "neutral", "negative"]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)

plot_pca_embeddings(embeddings, labels=labels, sentences=sentences)
```

---

## 🧠 What You’ll See

- A **2D scatterplot**, where similar sentences appear close
- Optional **color coding** by label (e.g., tone, group, year)
- Sentence index numbers to match with raw text

This gives an intuitive view of:
- **Semantic neighborhoods**
- **Separation between stances**
- **Consistency within topics or sources**

---

## 📈 Applications

| Application | Example |
|-------------|---------|
| Interview analysis | Plot how participants cluster by concern |
| Sentiment grouping | See if positive/negative labels group naturally |
| Political text framing | Compare party press releases visually |
| Narrative consistency | Detect stray or off-topic statements |
| Debugging embeddings | Inspect if meaning vectors behave coherently |

---

## 💡 Best Practices

| Tip | Why |
|-----|-----|
| Normalize text before embedding | Prevent noise from casing/punctuation |
| Use sentence-level input | Avoid overly long paragraphs |
| Color by label | Easier to explain to non-technical stakeholders |
| Use PCA for teaching/demo | Fast, interpretable, no stochasticity |
| Annotate by index | Then match points to sentences in table format |

---

## 🧱 Related Modules

| Module                             | Description                                       |
|------------------------------------|---------------------------------------------------|
| `embed_text_hf_basic.md`           | Generate embeddings for each sentence             |
| `semantic_drift_pipeline.md`       | Uses this function to visualize framing changes   |
| `meaning_matrix_heatmap.md`        | Heatmap version of similarity relationships       |
| `day2_llm_meaning_instruments.ipynb` | Hands-on notebook using this visualization       |

---

#