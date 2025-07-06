---
id: day2_session2_embeddings_similarity
title: "Day 2 – Session 2: LLM Embeddings & Similarity"
description: "Learn to encode, compare, and visualize sentence-level meaning using embeddings and cosine similarity with Hugging Face and OpenAI"
---

![fig_day2_session2_header](../shared_assets/visuals/images/fig_day2_session2_header.png)

# Day 2 – Session 2: LLM Embeddings & Similarity

> _"Embeddings are not outputs — they are **instruments**. Tools to measure meaning, nuance, and distance."_  

---

## 🎯 Session Objectives

✅ Understand the role of embeddings in representing meaning  
✅ Distinguish between token, word, sentence, and document embeddings  
✅ Compute and interpret cosine similarity between sentence vectors  
✅ Visualize embeddings using heatmaps, clusters, and PCA plots  
✅ Use modular pipelines to compare sentence meaning and model behavior  

---

## 🧠 GitBook Theory Pages

| Topic | GitBook Page | Purpose |
|-------|--------------|---------|
| 📘 Embedding Overview | [day2_embeddings_intro.md](../../doc/day2/day2_embeddings_intro.md) | Main handout + session framing |
| 🧩 Embedding Intuition | [embedding_intuition.md](day2/embedding_intuition.md) | Explains sentence vs token vectors |
| 📐 Cosine Similarity | [cosine_similarity_explained.md](day2/cosine_similarity_explained.md) | Formula + visual + comparison table |

---

## 💻 Notebooks: Live Demos

| Notebook | Purpose | Link |
|----------|---------|------|
| `embeddings-and-similarity-scores.ipynb` | Main demo: encode → compare → score | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/embeddings-and-similarity-scores.ipynb) |
| `embedding_cluster_visual.ipynb` | Optional: Cluster visualization with PCA/t-SNE | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/embedding_cluster_visual.ipynb) |

---

## 🧩 Codebook Modules

| Module | Path | Purpose |
|--------|------|---------|
| `embed_text_basics.md` | [`embed_text_basics.md`](day2/embed_text_basics.md) | Encode sentences using Hugging Face |
| `embed_compare_cosine.md` | [`embed_compare_cosine.md`](`day2/embed_compare_cosine.md`) | Compute cosine similarity |
| `embed_demo_pipeline.md` | [`embed_demo_pipeline.md`](day2/`embed_demo_pipeline.md) | Optional: wrap embedding + similarity logic |

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
| 1️⃣ | `day2_embeddings_basics.md` | Framing and session scaffold |
| 2️⃣ | `embedding_intuition.md` | Diagrams: token vs sentence embeddings |
| 3️⃣ | `cosine_similarity_explained.md` | Vector math and conceptual clarity |
| 4️⃣ | `embed_text_basics.md` | Code logic: convert text to vectors |
| 5️⃣ | `embed_compare_cosine.md` | Pairwise comparison logic |
| 6️⃣ | `embedding_cluster_visual.ipynb` | (Optional) See sentence clusters spatially |
| 7️⃣ | `hf_embed_vs_openai_compare.ipynb` | (Optional) Detect model-level differences |

---

## 🧠 Application Use Cases

- Sentence similarity scoring (automated QA, stance detection)
- Document clustering, topic surfacing
- Grounding zero-shot classification
- Preprocessing for agents, prompt evaluation, or search

---

## 🔮 What’s Next?

➡️ [Day 2 Session 3: Classification Using Embeddings →](dday2s3_schedule.md)

