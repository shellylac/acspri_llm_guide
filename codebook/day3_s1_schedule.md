---
id: day3_session1_rag
title: "Day 3 – Session 1: Retrieval-Augmented Generation (RAG)"
description: "Build an end-to-end pipeline for document retrieval and grounded generation using embeddings, ChromaDB, and Gemini Pro"
---

![fig_day3_session1_header](../shared_assets/visuals/images/fig_day3_session1_header.png)

# Day 3 – Session 1: Retrieval-Augmented Generation (RAG)

> _"Your LLM is only as smart as its memory. Today we give it one."_  

---

## 🎯 Session Objectives

✅ Understand RAG and how it differs from pure LLM inference / fine-tuning 
✅ Create a vector database (Chroma) from documents  
✅ Perform similarity search with sentence embeddings  
✅ Generate grounded responses using Gemini Pro or Hugging Face  
✅ Building a GraphRag and understanding how it differs from RAG

---

## 📘 GitBook Pages

| Page | Purpose | Status |
|------|---------|--------|
| `day3_rag_intro.md` | Main GitBook session outline and flow | ✅ |
| `embed_chroma.md` | Chunk + embed corpus using SentenceTransformers | ✅ |
| `similarity_query_chroma.md` | Retrieve similar chunks for a query | ✅ |
| `gemini_rag_generation.md` | Generate response using Gemini + citations | ✅ |

---

## 💻 Notebooks

| Notebook | Description | Link |
|----------|-------------|------|
| `intro_to_rag.ipynb` | Full pipeline: embed → search → generate | [Colab Link](https://colab.research.google.com/github/MariaAise/test/blob/main/intro_to_rag.ipynb) |
| `graphrag.ipynb` | GraphRag for literature review application |[Colab Link](https://colab.research.google.com/github/MariaAise/test/blob/main/graphrag.ipynb)


---

## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)


[OpenAPI Setup Guide](openai_api_setup_colab.md)

---

## 🔮 What’s Next?

➡️ Day 3 Session 2 focuses on **Agent Orchestration**, where RAG becomes one of many tools in a loop of reasoning, memory, and execution.

➡️ [Day 3 Session 2: Agents + ACP Loop →](day3_s2_schedule.md)
