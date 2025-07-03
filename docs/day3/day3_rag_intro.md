---
id: rag-session
title: Retrieval-Augmented Generation (RAG)
description: Build a grounded text generation system using vector search and document embeddings
tags: [rag, vector db, research workflows, chunking, citations]
status: live
---

## What is Retrieval-Augmented Generation?

RAG combines a language model with a search system. Instead of generating text based solely on internal training, the model first **retrieves relevant information from external sources** — then uses that to generate responses.

This is how modern research assistants, document analysis tools, and private GPTs are built.

---

## Why Use RAG?

Traditional LLMs hallucinate facts. RAG helps you:

- Ground outputs in your own research corpus
- Avoid hallucinations in sensitive domains
- Add citations and traceable sources
- Work with custom/private documents

Example use cases:
- Social science literature reviews
- Interview transcript analysis
- Real-time policy briefs
- News monitoring for public opinion

---

## RAG Architecture (Visual)

[Embed Figma diagram — “rag_pipeline.fig”]

Basic flow:

1. **User query**
2. **Embedding → vector DB**
3. **Top-k document chunks retrieved**
4. **Prompt assembly with context**
5. **LLM generates grounded response**

---

## Key Concepts

| Term              | What it Means                                 |
|-------------------|------------------------------------------------|
| **Chunking**      | Splitting documents into small text units (e.g. 500 tokens) |
| **Embeddings**    | Numeric representation of text for similarity matching |
| **Vector DB**     | Stores chunks + supports fast semantic search |
| **Retriever**     | Finds chunks most similar to the user query |
| **Context window**| Injected chunks shown to the model before generation |

---

## Code Module

📁 [`embed_chroma.md`](../codebook/embeddings/embed_chroma.md)

This module covers:
- Loading PDFs or text
- Chunking + embedding
- Storing in Chroma DB
- Running a sample query

---

## Colab Notebook

🔗 [Run it in Google Colab](https://github.com/maria-aise/codebook/blob/main/notebooks/day2_rag_colab.ipynb)

You’ll:
- Embed a document set
- Query the vector DB
- Generate a response using top-k results
- (Optional) Add citation logic

---

## RAG vs LLM-Only (Example)

**Query:** *What does the 2024 ACIC report say about youth diversion programs?*

| LLM Only (GPT-4)        | “The ACIC report emphasizes youth-focused strategies…” ❌ Hallucinated |
| RAG with citation       | “According to p.17 of the ACIC report: ‘Diversion should be embedded early...’” ✅ Grounded |

---

## Advanced Patterns (Optional for Explorers)

- Multi-source retrieval (e.g. transcripts + reports)
- Chunk re-ranking with BM25 or MMR
- Citation injection using chunk metadata
- Query rewriting before retrieval

---

## Recap

- RAG extends LLMs by adding access to your own documents.
- You embed + chunk the data once, then reuse forever.
- You can use RAG for research, auditability, summarization, even Q&A over case law or interviews.

---

## Related Modules

- [`agent_loop_rag.md`](../codebook/agents/agent_loop_rag.md): how RAG fits inside a reasoning agent
- [`classify_policy_stance.md`](../codebook/classification/classify_policy_stance.md): follow-up example with policy classification

---
