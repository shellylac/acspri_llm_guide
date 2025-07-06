---
id: day2_session1_meaning_similarity
title: Day 2 – Session 1: Meaning, Similarity & Semantic Drift
description: Build semantic instruments using embeddings from Gemini and Hugging Face to measure, visualize, and compare sentence meaning
---
![fig_day2_session1_header](../shared_assets/visuals/images/fig_day2_session1_header.png)


# Day 2 – Session 1: Meaning, Similarity & Semantic Drift

> _"Today we build instruments — not for generating text, but for **measuring meaning**."_

---

## 🎯 Session Objectives

✅ Understand how transformer models embed semantic meaning  
✅ Generate and compare sentence embeddings using Gemini and Hugging Face  
✅ Visualize relationships via PCA and similarity heatmaps  
✅ Detect framing drift and coder disagreement in language  
✅ Reuse modules in classification, prompt QA, and RAG pipelines  

---

## 🧠 Theory Foundation (GitBook-first)

| Topic | GitBook Page | Purpose |
|-------|--------------|---------|
| 🧠 Transformer Framing | [day2_transformer_intro.md](../docs/day2/day2_transformer_intro.md) | Sets up embeddings as instruments of meaning |
| 🤖 Model Comparison | [compare_gemini_vs_hf.md](day2/compare_gemini_vs_hf.md) | Juxtaposes Gemini and HF embeddings |
| 🧪 Meaning Matrix | [meaning_matrix_heatmap.md](day2/meaning_matrix_heatmap.md) | Heatmap of sentence similarities |

---

## 💻 Live Notebook Demo

| Notebook | Purpose | Link |
|----------|---------|------|
| `day2_llm_meaning_instruments.ipynb` | End-to-end embeddings, similarity, drift, heatmaps | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/day2_llm_meaning_instruments.ipynb) |

Features:
- Gemini + HF sentence embedding
- Cosine similarity matrix
- PCA projection
---

## 🧩 Modular Codebook Blocks

| File | Purpose |
|------|---------|
| [`embed_text_hf_basic.md`](day2/embed_text_hf_basic.md) | HuggingFace embedding using MiniLM |
| [`embed_text_gemini.md`](day2/embed_text_gemini.md) | Gemini wrapper for sentence-level probes |
| [`compare_embeddings_cosine.md`](day2/compare_embeddings_cosine.md) | Pairwise cosine similarity logic |
| [`visualize_embeddings_pca.md`](day2/visualize_embeddings_pca.md)| 2D projection to plot sentence clusters |
| [`visualize_similarity_heatmap.md`](day2/visualize_similarity_heatmap.md)| Creates interpretable heatmap matrix |
| [`semantic_drift_pipeline.md`](day2/semantic_drift_pipeline.md)| Pipeline for analyzing language shifts |

---

## 🧪 Optional Tools & Research Extensions

| File | Purpose | Use |
|------|---------|-----|
| `semantic_drift_detector.ipynb` | Standalone RAG drift pipeline | Optional – client use |

---

## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)


[OpenAPI Setup Guide](openai_api_setup_colab.md)

---

## 🗂 Suggested Reading Order

| Step | File | Purpose |
|------|------|---------|
| 1️⃣ | `day2_transformer_intro.md` | Context: why embeddings matter |
| 2️⃣ | `embed_text_hf_basic.md` | Build first embeddings |
| 3️⃣ | `embed_text_gemini.md` | Probe meaning via Gemini |
| 4️⃣ | `compare_embeddings_cosine.md` | Quantify similarity |
| 5️⃣ | `visualize_embeddings_pca.md` | See clusters in 2D |
| 6️⃣ | `meaning_matrix_heatmap.md` | Visual matrix for interpretation |
| 7️⃣ | `semantic_drift_pipeline.md` | Detect language shift patterns |

---

## 🔮 What’s Next?

➡️ In Session 2, you’ll use these semantic tools to drive **classification, RAG, and multi-document workflows**.

➡️ [Day 2 Session 2: Classification & Retrieval →](dday2s2_schedule.md)
