---
id: day1_session1_llm_foundations
title: Day 1 – Session 1: LLM Foundations & Platforms
description: Foundations of LLMs, tokenization, embeddings, and the platforms that power your AI workflow
tags: [llm, nlp, transformers, huggingface, openai, gemini]
status: live
---
![fig_day1_header](../shared_assets/visuals/images/fig_day1_header.png)

# Day 1 – Session 1: LLM Foundations & Platforms

> _"We begin not with theory, but with the instrument. This is not about becoming a developer — it’s about learning to think through the machine."_  

---

## 🎯 Session Objectives

✅ LLM Ecosystems: From Foundations to Frontiers
✅ Set up Colab + Gemini  
✅ Understand minimal working Python for LLM workflows  
✅ Run your first HuggingFace model  
✅ Get oriented in the LLM landscape (OpenAI, Gemini, HF)  
✅ Learn how a transformer processes text step-by-step

---

## 🧱 Core Modules

### 🛠️ [Colab Setup: `colab_foundations.md`](day1/colab_foundations.md)
- API keys, pip installs, notebook config
- HuggingFace auth and environment

### 🧬 [Python Minimalism: `python_minimalist.md`](day1/python_minimalist.md)
- Variables, loops, functions = 80/20 Python for research workflows  
- Not coding school — just what’s useful

### 🤖 [LLM Pipeline Walkthrough: `llm_input_pipeline.md`](day1/llm_input_pipeline.md)
- Your friendly LLM in your full command with one line of code
- From input to output in a second

### 🤖 [LLM Response Structure: `llm_response_structure.md`](day1/llm_response_structure.md)
- Understanding your LLM results
- Components of the response output
  
---

## ⚙️ Jupyter Notebooks

### ▶️ [Colab Foundations Notebook](https://colab.research.google.com/github/MariaAise/test/blob/main/colab_foundations.ipynb)

- Install packages, load keys, run basic functions
- Reusable starting point for all future notebooks

### ▶️ [HuggingFace Pipeline Demo](https://colab.research.google.com/github/MariaAise/test/blob/main/huggingface_pipeline_demo.ipynb)
- Load sentiment analysis pipeline
- Classify custom text inputs with one line

### ▶️ [Bonus: Multi-task Pipeline](https://colab.research.google.com/github/MariaAise/test/blob/main/huggingface_pipeline_bonus.ipynb)
- Summarization  
- Translation  
- Zero-shot classification

### 🧪 [Optional: Response Explainer](https://colab.research.google.com/github/MariaAise/test/blob/main/llm_response_explainer.ipynb)
- Explore `dict`, `json`, unpacking nested responses
- Great for those unfamiliar with structured outputs

---

## 🧠 Suggested Flow

| Time          | Focus Area                         | Module or Notebook |
|---------------|------------------------------------|--------------------|
| 10:00–10:10   | Setup Colab + environment          | `colab_foundations.*` |
| 10:10–10:25   | Python quickstart (only useful bits) | `python_minimalist.md`, `colab_foundations.ipynb` |
| 10:25–10:35   | Sentiment pipeline (live demo)     | `huggingface_pipeline_demo.ipynb` |
| 10:35–10:50   | Bonus tasks (self-paced)           | `huggingface_pipeline_bonus.ipynb` |
| 11:00–11:10   | How transformers work              | `llm_input_pipeline.md` |

---

## 🔭 Up Next

➡️ [Session 2: Platform Walkthroughs & API Setup →](day1s2_schedule.md)