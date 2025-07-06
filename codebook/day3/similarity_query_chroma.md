---

---

## Purpose

Use this module to perform **semantic similarity search** over previously embedded documents stored in ChromaDB.  
This is a core retrieval component of any RAG (Retrieval-Augmented Generation) system.

---

## Load Chroma Vector Store

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
```

---

## Define Query and Search

```python
query = "What trends are emerging in winter fashion this season?"
results = db.similarity_search(query, k=3)
```

---

## Display Results

```python
for i, doc in enumerate(results):
    print(f"--- Result {i+1} ---")
    print(doc.page_content[:300])  # show first 300 characters
    print()
```

---

## Optional: Show Similarity Scores (if supported)

Chroma’s native `similarity_search` doesn’t expose scores by default.  
To view similarity scores, use `similarity_search_with_score`:

```python
results_with_scores = db.similarity_search_with_score(query, k=3)

for doc, score in results_with_scores:
    print(f"Score: {score:.4f}")
    print(doc.page_content[:300])
    print()
```

---

## Use Cases

- Inference-time retrieval for RAG
- Relevance-based filtering of text corpora
- Preprocessing step before generation or classification

---

## Related Modules

- [`embed_chroma.md`](../embeddings/embed_chroma.md)
- [`gemini_rag_generation.md`](../generation/gemini_rag_generation.md)
