---

---

# 🔥 Module: Visualize Similarity Matrix as Heatmap

## 📌 Purpose

This module produces a **heatmap of cosine similarity scores** between sentences or documents.

It’s designed to make **semantic relationships** between texts **visually interpretable** — ideal for clustering, auditing, and presentation.

This is particularly useful for:
- Interview/survey clustering
- Media frame divergence detection
- Deduplication audits
- Client-facing dashboards
- Public-facing reports

---

## 🧠 What It Does

- Takes a cosine similarity matrix as input
- Optionally takes sentence labels (row/col)
- Uses `seaborn.heatmap()` for visual rendering
- Annotates cells with numeric values for interpretability

---

## ⚙️ Function

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_similarity_heatmap(similarity_matrix, labels=None, figsize=(8, 6), annot=True, cmap="coolwarm", title="Semantic Similarity Heatmap"):
    """
    Plots a cosine similarity matrix as a heatmap.

    Parameters:
        similarity_matrix (np.ndarray or pd.DataFrame): 2D array of pairwise cosine scores
        labels (List[str], optional): Sentence or document labels
        figsize (tuple): Size of the plot
        annot (bool): Annotate heatmap cells with numeric values
        cmap (str): Color palette for heatmap
        title (str): Title of the plot

    Returns:
        None
    """
    if isinstance(similarity_matrix, pd.DataFrame):
        data = similarity_matrix
    else:
        data = pd.DataFrame(similarity_matrix, index=labels, columns=labels)

    plt.figure(figsize=figsize)
    sns.heatmap(data, annot=annot, cmap=cmap, square=True, fmt=".2f", linewidths=0.5, cbar=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()
```

---

## 🧪 Example Usage

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from visualize_similarity_heatmap import plot_similarity_heatmap

sentences = [
    "The law passed without opposition.",
    "A bill was approved unanimously.",
    "There was strong resistance to the new policy.",
    "The legislation was criticized in parliament."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)
sim_matrix = cosine_similarity(embeddings)

plot_similarity_heatmap(sim_matrix, labels=sentences)
```

---

## 📈 What You’ll See

- Darker red = more similar  
- Blue/neutral = lower similarity  
- Diagonal = 1.0 (each sentence with itself)

Heatmaps help reveal:
- **Clusters** of meaning
- **Contrastive pairs**
- **Outlier or noisy responses**
- **Topic coherence**

---

## 💡 Best Practices

| Tip | Why |
|-----|-----|
| Use short, clean sentences | Prevent label clutter and overlap |
| Label rows/columns clearly | Helps readers interpret heatmap quickly |
| Sort sentences logically | Group by question, source, or topic |
| Limit to ≤ 20 sentences | Heatmaps scale poorly with many rows |

---

## 🧠 Ideal For

| Use Case | Benefit |
|----------|---------|
| Interview analysis | Visual clustering by theme |
| Survey audits | Detect near-duplicates or inconsistencies |
| Media analysis | Contrast framing between outlets |
| Trigger detection | Highlight polarity gaps |
| Policy monitoring | Compare positions from different actors |

---

## 🧱 Related Modules

| Module                             | Description                                     |
|------------------------------------|-------------------------------------------------|
| `embed_text_hf_basic.md`           | Generate embeddings for cosine similarity       |
| `compare_embeddings_cosine.md`     | Compute similarity matrix from embeddings       |
| `meaning_matrix_heatmap.md`        | Combined visual + textual interpretation tool   |
| `day2_llm_meaning_instruments.ipynb` | Hands-on notebook using this module            |

---

## 🪪 Author  
*Maria Aise — Modular Codebook, ACSPRI 2025*  
Used across Streamlit dashboards, client reports, and academic visualizations.
