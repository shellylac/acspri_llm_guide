---
---

# 🔁 Embedding Pipeline – Encode → Compare → Visualize

This module provides a full workflow for generating sentence embeddings, comparing their similarity, and visualizing the results.

It’s ideal for:
- Analyzing open-ended survey responses
- Grouping interview quotes by semantic topic
- Building intuition around how LLMs “understand” language

---

## 📦 Requirements

Make sure you have the following packages installed:

```bash
pip install sentence-transformers scikit-learn umap-learn matplotlib
```

---

## 🧠 Step 1: Encode Sentences

Use a pretrained model from `sentence-transformers` to convert text into embeddings.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The policy is controversial.",
    "I support the new regulation.",
    "Many people disagree with the decision.",
    "This initiative will help the environment.",
    "The government is overreaching."
]

embeddings = model.encode(sentences)
```

> These are dense vectors (~384 dimensions) that represent the **semantic meaning** of each sentence.

---

## 🔍 Step 2: Compare Similarity (Cosine Matrix)

Use cosine similarity to compare how close sentences are in meaning.

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

similarity_matrix = cosine_similarity(embeddings)

print(np.round(similarity_matrix, 2))
```

> Diagonal values are always 1.0 (a sentence compared to itself).  
> Values close to 1.0 mean high similarity; near 0 means unrelated.

---

## 📊 Step 3: Visualize with UMAP or PCA

We’ll use UMAP to reduce embeddings to 2D for visual inspection.

```python
import umap
import matplotlib.pyplot as plt

reducer = umap.UMAP(n_neighbors=3, min_dist=0.3, metric="cosine")
embedding_2d = reducer.fit_transform(embeddings)

plt.figure(figsize=(8, 6))
plt.scatter(embedding_2d[:, 0], embedding_2d[:, 1], s=100)

for i, txt in enumerate(sentences):
    plt.annotate(txt, (embedding_2d[i, 0]+0.1, embedding_2d[i, 1]), fontsize=9)

plt.title("Sentence Embedding Clusters (UMAP)")
plt.grid(True)
plt.show()
```

> Each dot represents a sentence, placed according to **semantic similarity**.

---

## 🧪 Optional: Cosine Heatmap

Use Seaborn to create a heatmap of similarities.

```python
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.heatmap(similarity_matrix, annot=True, xticklabels=sentences, yticklabels=sentences, cmap="coolwarm")
plt.title("Cosine Similarity Between Sentences")
plt.show()
```

> This lets you **see patterns** in how sentences group together — helpful for qualitative analysis.

---

## 🧰 Summary

| Step        | Purpose                                      |
|-------------|----------------------------------------------|
| Encode      | Turn text into semantic vectors              |
| Compare     | Measure meaning similarity using cosine      |
| Visualize   | Interpret clusters with UMAP or heatmaps     |

---

## ✅ Use Cases

- Grouping free-text responses by theme
- Detecting duplicated survey answers
- Understanding qualitative patterns at scale
- Preprocessing for clustering or classification

---

## 🔗 Related Modules

| Module                        | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| `embed_text_basics.md`        | Basic text → vector encoding using sentence-transformers     |
| `embed_compare_cosine.md`     | Cosine similarity calculation between embeddings             |
| `embedding_cluster_visual.ipynb` | Notebook to explore sentence clusters in 2D               |
| `train_logistic_classifier.md`| Use embeddings as input to a supervised classifier           |

