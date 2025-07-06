---
id: day1_session3_prompt_architecture
title: Day 1 – Session 3: Prompt Engineering + Platform Mastery
description: Learn to structure, debug, and evaluate prompts for LLM workflows across Gemini, OpenAI, and Hugging Face
tags: [prompting, session3, architecture, evaluation, colab, modularity]
status: live
---
![fig_day1_header](../shared_assets/visuals/images/fig_day1_session3_header.png)

# Day 1 – Session 3: Prompt Engineering + Platform Mastery

> _"Prompts are not just inputs — they are **architectural decisions**. Today we write systems, not strings."_

---

## 🎯 Session Objectives

✅ Understand the anatomy and strategy behind well-formed prompts  
✅ Compare major prompting frameworks: zero-shot, few-shot, CoT, ReAct  
✅ Identify and debug common prompt failures  
✅ Evaluate prompt quality using structured and automated methods  
✅ Apply prompt modularity for reuse across GitBook, MVP, and agents  

---

## 🧠 Theory Foundation (GitBook-first)

| Topic | GitBook Page | Purpose |
|-------|--------------|---------|
| 🪧 Introduction | [prompting_intro.md](../docs/day1/prompting_intro.md) | Framing prompting as interface logic |
| 🧩 Anatomy | [prompt_anatomy.md](../docs/day1/prompt_anatomy.md) | Breaks down instruction/context/examples |
| 🔀 Frameworks | [prompt_frameworks.md](../docs/day1/prompt_frameworks.md) | Zero-shot, Few-shot, CoT, ReAct, ToT |
| 🧯 Failures | [prompt_failures.md](../docs/day1/prompt_failures.md) | Common failure types + recovery |
| 🧱 Modularity | [prompt_modularity.md](../docs/day1/prompt_modularity.md) | Reuse logic for MVP and GitBook |
| 🧪 Evaluation | [prompt_evaluation.md](../docs/day1/prompt_evaluation.md) | Evaluation scores, trace, LLM-as-judge |

---

## 💻 Live Notebook Demo

| Notebook | Purpose | Link |
|----------|---------|------|
| `prompting_sandbox.ipynb` | Side-by-side test on Gemini, GPT-4, HF | [Run in Colab](https://colab.research.google.com/github/MariaAise/test/blob/main/prompting_sandbox.ipynb) |

Features:
- Toggle between prompt types and models
- Capture output differences
- Preview modular architecture for future UI

---

## 🧪 Project & Participant Assets

| File | Purpose | Use |
|------|---------|-----|
| [mini_project_templates.md](day1/mini_project_templates.md) | Homework-style real-world prompt challenges | Leads into independent work |

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
| 1️⃣ | `prompting_intro.md` | Session intro and context |
| 2️⃣ | `prompt_anatomy.md` | Foundational prompt structure |
| 3️⃣ | `prompt_frameworks.md` | Compare prompting methods |
| 4️⃣ | `prompt_failures.md` | Learn to debug |
| 5️⃣ | `prompt_modularity.md` | Enable strategic reuse |
| 6️⃣ | `prompt_evaluation.md` | Score and compare prompt quality |
| 7️⃣ | `mini_project_templates.md` | Ready-to-use sector-specific prompts |

---

## 🔮 What’s Next?

➡️ On Day 2, we go from prompt-level control to **classification & embeddings** — the building blocks of RAG and intelligent agents.

➡️ [Day 2 – Session 1: Meaning, Similarity & Semantic Drift →](day2s1_schedule.md)
