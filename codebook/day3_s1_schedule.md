---
id: day3_session1_rag
title: Day 3 – Session 1: Retrieval-Augmented Generation (RAG)
description: Build an end-to-end pipeline for document retrieval and grounded generation using embeddings, ChromaDB, and Gemini Pro
---

![fig_day3_session1_header](../shared_assets/visuals/images/fig_day3_session1_header.png)

# Day 3 – Session 1: Retrieval-Augmented Generation (RAG)

> _"Your LLM is only as smart as its memory. Today we give it one."_  

---

## 🎯 Session Objectives

✅ Understand RAG and how it differs from pure LLM inference  
✅ Create a vector database (Chroma) from documents  
✅ Perform similarity search with sentence embeddings  
✅ Generate grounded responses using Gemini Pro or Hugging Face  
✅ Use Colab or Streamlit as front-end delivery mechanisms  

---

## 📘 GitBook Pages

| Page | Purpose | Status |
|------|---------|--------|
| `day3_rag_intro.md` | Main GitBook session outline and flow | ✅ |
| `embed_chroma.md` | Chunk + embed corpus using SentenceTransformers | ✅ |
| `similarity_query_chroma.md` | Retrieve similar chunks for a query | ✅ |
| `gemini_rag_generation.md` | Generate response using Gemini + citations | ✅ |

---

## 🔍 Workflow Summary

1. **Embed your documents** → ChromaDB  
2. **Query with a prompt** → retrieve relevant chunks  
3. **Generate grounded answer** → Gemini or Hugging Face  
4. **Run in Colab or Streamlit** → optional front-end interface  

---

## 💻 Notebooks

| Notebook | Description | Link |
|----------|-------------|------|
| `intro_to_rag.ipynb` | Full pipeline: embed → search → generate | [Colab Link](https://colab.research.google.com/github/MariaAise/test/blob/main/intro_to_rag.ipynb) |
| `embeddings_similarity_score.ipynb` | Sentence similarity demo (optional warm-up) | *(optional)* |

---

## 🎛️ Streamlit App

| File | Description | Use |
|------|-------------|-----|
| `day3_rag_streamlit.py` | UI to run the RAG workflow from browser | Giveaway |

---

## 🧩 Codebook Modules

| Module | Path | Purpose |
|--------|------|---------|
| `embed_chroma.md` | `codebook/embeddings/` | Load, chunk, embed, and persist documents |
| `similarity_query_chroma.md` | `codebook/retrieval/` | Retrieve top-k chunks by semantic similarity |
| `gemini_rag_generation.md` | `codebook/generation/` | Answer questions based on retrieved chunks with Gemini |

---

## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)


[OpenAPI Setup Guide](openai_api_setup_colab.md)

---

## 🗂 Suggested Reading Flow

| Step | File | Purpose |
|------|------|---------|
| 1️⃣ | `day3_rag_intro.md` | What is RAG and why it matters |
| 2️⃣ | `embed_chroma.md` | Build your vector store |
| 3️⃣ | `similarity_query_chroma.md` | Perform semantic search |
| 4️⃣ | `gemini_rag_generation.md` | Generate citations-aware output |
| 5️⃣ | `intro_to_rag.ipynb` | Run the full pipeline in Colab |
| 6️⃣ | `day3_rag_streamlit.py` | Optional UI for public-facing or research apps |

---

## 🧪 Output Comparison: Gemini vs Hugging Face

| Model | Citation Support | Reasoning | Setup |
|-------|------------------|-----------|-------|
| Gemini Pro | ✅ Inline `[source_n]` | ✅ Strong | API key required |
| HF Transformers (e.g. Flan-T5) | ❌ None | ⚠️ Basic | Local/Colab, no key needed |

---

## 🧠 Real-World Applications

- Literature review (with source traceability)  
- Interview transcript grounding  
- Research synthesis and cross-source QA  
- Internal knowledge systems  
- News and policy monitoring  

---

## 🔮 What’s Next?

➡️ Day 3 Session 2 focuses on **Agent Orchestration**, where RAG becomes one of many tools in a loop of reasoning, memory, and execution.

➡️ [Day 3 Session 2: Agents + ACP Loop →](day3_s2_schedule.md)
