---

---

## Purpose

This module takes top-k retrieved chunks from a vector store (e.g. Chroma) and uses **Google Gemini Pro** to generate a grounded response.  
It appends `[source_n]` citation markers to each chunk and instructs the model to cite sources inline.

---

## Prepare Prompt with Citation Markers

```python
retrieved_with_refs = []
for i, doc in enumerate(results):
    marker = f"[source_{i+1}]"
    text = doc.page_content.strip() + f"\n\n{marker}"
    retrieved_with_refs.append(text)

referenced_text = "\n\n".join(retrieved_with_refs)

prompt = f"""Answer the following question using the content below.
Include [source_n] markers to show where each fact comes from.

{referenced_text}

Question: {query}
"""
```

---

## Generate with Gemini Pro

```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(prompt)
print(response.text)
```

---

## Example Output

> **Q:** What are the dominant fashion directions this season?  
> **A:** According to the retrieved materials, minimalism and structured silhouettes dominate winter collections [source_1]. Bold colors like cobalt and red are heavily featured [source_2].

---

## Notes

- Assumes prior chunk retrieval (see [`similarity_query_chroma.md`](../retrieval/similarity_query_chroma.md))
- Works well in Streamlit or notebook-based UIs
- Inline citations improve trust, auditability, and research alignment

---

## Related Modules

- [`embed_chroma.md`](../embeddings/embed_chroma.md)
- [`similarity_query_chroma.md`](../retrieval/similarity_query_chroma.md)
