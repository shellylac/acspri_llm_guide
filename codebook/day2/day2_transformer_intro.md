---
id: embed_text_hf_basic
title: Embedding Text with Hugging Face – Basics
type: module
tags: [embeddings, sentence-transformers, Hugging Face, semantic similarity, NLP]
description: >
  Learn how to convert sentences into semantic vectors using the Hugging Face `sentence-transformers` library.
  This module walks through model loading, encoding, and best practices for reproducible, explainable embedding workflows.
  Includes a breakdown of how to choose between cosine similarity, classifiers, and PEFT (LoRA) fine-tuning based on your use case.
created_by: Maria Aise (Dr. Maria Prokofieva)
program: ACSPRI Winter 2025 – Day 2, Session 2
---

# 🧠 Day 2 – Session 1: How LLMs Measure Meaning

## 🔍 Overview

This session bridges the gap between prompting (Day 1) and advanced semantic operations (Sessions 2 & 3).  
We explore **how transformers encode meaning**, and how tools like **Gemini** (qualitative) and **Hugging Face** (quantitative) interpret sentence-level semantics.

---

## 🎯 Learning Objectives

- Understand how transformer models represent meaning
- Compare Gemini (language-based) vs Hugging Face (vector-based) reasoning
- Compute and visualize sentence similarity using embeddings
- Detect subtle semantic shifts in language framing
- Prepare for downstream tasks like classification and clustering

---

## 📚 Topics Covered

- Transformer architecture (token → embedding → attention)
- Gemini API for meaning interpretation
- Sentence embeddings with `sentence-transformers`
- Cosine similarity and vector distance
- Semantic drift and framing divergence
- Annotator disagreement simulation

---

## 💻 Hands-On Notebook

The entire session is driven from one notebook:

👉 [`day2_llm_meaning_instruments.ipynb`](../../codebook/day2/day2_llm_meaning_instruments.ipynb)

It includes:

- Gemini meaning probes
- Sentence embedding with `all-MiniLM-L6-v2`
- Cosine similarity matrix + heatmap
- PCA projection of sentence clusters
- Semantic drift analysis (e.g., “protest” vs “riot”)
- Optional coder disagreement simulation

---

## 🧪 Models & Tools

- 🤖 Gemini API (`google.generativeai`)  
- 🧠 `sentence-transformers` (MiniLM)
- 📐 Cosine similarity (`sklearn.metrics`)
- 📊 Heatmaps with `seaborn`, PCA via `sklearn.decomposition`

---

## 🧠 Why This Matters

This session is not just technical. It's **foundational for real-world research** and **MVP product logic**:

| Use Case | How This Session Helps |
|----------|------------------------|
| Survey/sentence analysis | Quantify similarity, bias, stance |
| Brand tone auditing | Detect framing shifts |
| RAG input prep | Normalize and compare sources |
| Trigger detection | Establish vector-based conditions for agent logic |
| Qualitative coding | Replace inter-annotator disagreement with vector metrics |

---

## 📌 Next Steps

In Sessions 2 and 3, we build on these embeddings to:
- Classify sentence-level intent
- Cluster survey responses
- Build LoRA-classifiers and RAG systems

---

## 🪪 Created by

*Dr. Maria Aise (aka Maria Prokofieva)*  
For the ACSPRI Winter 2025 Program

