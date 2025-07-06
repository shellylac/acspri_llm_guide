---

---

# 🔁 Embedding Demo Pipeline

This module wraps the basic embedding and comparison logic into a single, reusable pipeline function — ideal for demos, notebooks, or quick exploratory workflows.

---

## 🧭 What It Does

- Takes a list of sentences
- Generates sentence embeddings (MiniLM by default)
- Computes cosine similarity matrix
- Returns embeddings + similarity matrix

You can plug this into notebooks, Streamlit dashboards, or command-line tools.

---

## 🧪 Code

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def run_embedding_pipeline(sentences, model_name="all-MiniLM-L6-v2", round_values=True):
    """
    Encodes a list of sentences and computes cosine similarity matrix.
    
    Args:
        sentences (list[str]): Input texts
        model_name (str): SentenceTransformer model to load
        round_values (bool): Whether to round similarity scores for readability
    
    Returns:
        dict: {
            "embeddings": np.ndarray,
            "similarity": np.ndarray,
            "sentences": list[str]
        }
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)
    sim_matrix = cosine_similarity(embeddings)

    if round_values:
        sim_matrix = np.round(sim_matrix, 2)
    
    return {
        "sentences": sentences,
        "embeddings": embeddings,
        "similarity": sim_matrix
    }

🧠 Use Cases
Interactive demos

Educational walkthroughs

Batch similarity inspection

Heatmap generation

🔗 Related Modules

| Module Path                              | Description                                   |
| ---------------------------------------- | --------------------------------------------- |
| `embed_text_basics.md`                   | Embeds a list of sentences                    |
| `embed_compare_cosine.md`                | Computes cosine similarity between embeddings |
| `embedding_cluster_visual.ipynb`         | Visualizes embeddings with PCA                |
| `embeddings-and-similarity-scores.ipynb` | Full classroom notebook that can call this    |

