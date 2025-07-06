---

---

# 🌐 Module: Semantic Drift Detection Pipeline

## 📌 Purpose

This module detects and visualizes **semantic drift**: changes in how meaning is expressed or framed over time, across sources, or between audiences.

It is particularly useful in:
- **Media discourse**: protest vs riot, welfare vs support  
- **Policy framing**: e.g., “tax relief” vs “government handouts”  
- **Longitudinal surveys**: shifting tone across generations  
- **Political communication**: how the same concept is reframed by parties

---

## 🧠 What Is Semantic Drift?

Semantic drift refers to **shifts in meaning** — not just in vocabulary, but in **tone, stance, and framing**.

> Example:
> - Year 1: “Protesters voiced their concern.”
> - Year 3: “Rioters disrupted the peace.”

The subject is similar, but **tone and implication have shifted**, often with political, social, or emotional consequences.

---

## 🎯 Pipeline Overview

This module performs:

1. **Embedding of sentences** using `sentence-transformers`
2. **Similarity computation** to quantify divergence
3. **PCA projection** into 2D for human interpretation
4. **Color-labeling by source/group/time** for comparison

---

## ⚙️ Function

```python
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def semantic_drift_analysis(sentences, labels=None, model_name='all-MiniLM-L6-v2', figsize=(7, 6)):
    """
    Visualizes semantic drift using sentence embeddings and PCA.

    Parameters:
        sentences (list of str): List of sentences to analyze
        labels (list of str): Optional grouping or source labels for each sentence
        model_name (str): Sentence embedding model to use
        figsize (tuple): Size of the matplotlib figure

    Returns:
        None (displays PCA scatterplot)
    """
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)

    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)

    plt.figure(figsize=figsize)
    if labels:
        unique_labels = list(set(labels))
        for label in unique_labels:
            indices = [i for i, l in enumerate(labels) if l == label]
            plt.scatter(reduced[indices, 0], reduced[indices, 1], label=label)
        plt.legend()
    else:
        plt.scatter(reduced[:, 0], reduced[:, 1])

    for i, sentence in enumerate(sentences):
        plt.annotate(f"{i+1}", (reduced[i, 0], reduced[i, 1]), fontsize=9)

    plt.title("Semantic Drift Projection (PCA)")
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
```

---

## 🧪 Example Usage

```python
sentences = [
    "The protest drew thousands of supporters.",
    "The riot caused widespread destruction.",
    "Demonstrators demanded justice peacefully.",
    "Violent mobs clashed with police in the streets."
]

labels = ["neutral", "negative", "neutral", "negative"]

semantic_drift_analysis(sentences, labels)
```

---

## 📈 What You’ll See

A 2D scatterplot showing where sentences **cluster** based on meaning.

- **Close points** = similar semantic framing
- **Distant points** = divergent tone/stance
- Colored labels help reveal **group-level drift**

---

## 💡 Best Practices

| Tip | Why |
|-----|-----|
| Label consistently | Use "source", "group", or "time period" to compare |
| Avoid long documents | Sentence embeddings assume 1 complete thought at a time |
| Normalize text | Strip special characters and extra spaces |
| Use PCA for interpretability | More stable than t-SNE for teaching |
| Try different embedding models | Multi-qa, mpnet, and `text-embedding-3-small` offer diverse perspectives |

---

## 🔁 Use Cases in Research

| Field | Example |
|-------|---------|
| Media studies | Track how climate coverage shifted over 10 years |
| Political science | Compare party descriptions of a bill |
| Sociology | Study generational differences in tone |
| Narrative mapping | Align discourse across actors or languages |

---

## 🧱 Related Modules

| Module                             | Description                                      |
|------------------------------------|--------------------------------------------------|
| `embed_text_hf_basic.md`           | Sentence embeddings from Hugging Face            |
| `meaning_matrix_heatmap.md`        | Heatmap visualization of similarity matrix       |
| `compare_embeddings_cosine.md`     | Pairwise similarity extraction                   |
| `day2_llm_meaning_instruments.ipynb` | Uses this pipeline to demonstrate framing drift |

-