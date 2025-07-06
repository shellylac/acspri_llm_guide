---
id: day2_session3_classification_labeling
title: Day 2 – Session 3: Classification & Labeling with Embeddings
description: Learn to classify semantic content using embeddings, zero-shot similarity, and fine-tuned classifiers in policy, stance, and social science research
tags: [day2, classification, embeddings, zero-shot, few-shot, peft, lora]
status: live
---

![fig_day2_session3_header](../shared_assets/visuals/images/fig_day2_session3_header.png)


# Day 2 – Session 3: Classification & Labeling with Embeddings

> _"Embeddings don’t just tell us what things **mean** — they let us decide what they **belong to**."_  

---

## 🎯 Session Objectives

✅ Use cosine similarity for zero-shot classification  
✅ Apply labeled anchors for few-shot decision logic  
✅ Train classifiers on sentence embeddings (logistic regression)  
✅ Explore PEFT (LoRA) fine-tuning for advanced upgrades  
✅ Understand upgrade paths to higher accuracy or explainability  

---

## 📘 GitBook Pages

| Page | Purpose | Usage |
|------|---------|--------|
| [`day2_classification_embeddings.md`](../docs/day2/day2_classification_embeddings.md)| 🧭 Session anchor page with full narrative | Core teaching doc |
| [`classify_policy_stance.md`](../docs/day2/classify_policy_stance.md) | 🧠 Step-by-step walkthrough: stance classification pipeline | Demo + participant reference |
| [`peft_finetune_demo.md`](../docs/day2/peft_finetune_demo.md) | 🔬 Advanced: PEFT explanation and integration strategy | Linked, optional |

---

## 🧠 Classification Strategies

This session focuses on 3 core strategies:

1. **Zero-shot by cosine similarity**
2. **Few-shot anchor matching**
3. **Supervised classification (logistic regression on embeddings)**

➡️ For advanced users: **PEFT fine-tuning** via LoRA is available as an upgrade path.

---

## 💻 Notebooks

| Notebook | Purpose | Link |
|----------|---------|------|
| `classify_policy_stance.ipynb` | Main in-session demo: classify statements using semantic embedding | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/classify_policy_stance.ipynb) |
| `peft_finetune_demo.ipynb` | Optional: Demonstrates lightweight model fine-tuning via LoRA | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/peft_finetune_demo.ipynb)

---
## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)


[OpenAPI Setup Guide](openai_api_setup_colab.md)

---
## 🔮 What’s Next?

➡️ [Day 3 Session 1: Retrieval-Augmented Generation (RAG) →](dday3s1_schedule.md)