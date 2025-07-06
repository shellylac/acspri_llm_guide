---
id: day1_session2_platforms
title: Day 1 – Session 2: Platform Walkthroughs & API Setup
description: Compare major LLM providers, walk through interface features, and launch your first model calls with real APIs
tags: [session2, api, openai, gemini, huggingface, colab]
status: live
---
![fig_day1_header](../shared_assets/visuals/images/fig_day1_session2_header.png)


# Day 1 – Session 2: Platform Walkthroughs & API Setup

> _"Three platforms. One interface layer. Your job is to learn how to access intelligence across providers — safely, precisely, and with full control."_  

---

## 🎯 What You’ll Learn

✅ Compare Gemini, OpenAI, and Hugging Face for real-world use  
✅ Navigate their UI features: extensions, tokens, temperature  
✅ Set up API keys safely and run your first model calls  
✅ Prepare for hands-on coding in Colab with multi-provider logic  

---

## 🧭 Structure of This Session

We move from **interface → access → execution** across three major platforms. This is the systems walkthrough you’ll use again and again when working with LLMs.

---

## 🌐 Platform Landscape

### 🧩 Platform Comparison
[`platform_comparison.md`](../docs/day1/platform_comparison.md)

- Access models: free vs paid
- Modalities: chat, code, vision
- Limits, costs, and provider fit

### 🗝️ [API Key Setup](day1/api_key_setup.md)
- How to generate keys for OpenAI, Gemini, and Hugging Face
- Where to store safely in Colab or `.env`

---

## 🖥 Walkthrough Pages

| Platform | Guide Page | Covers |
|----------|------------|--------|
| 🤗 Hugging Face | [huggingface_walkthrough.md](day1/huggingface_walkthrough.md) | Model hub, pipeline, Spaces |
| 🧠 Gemini Studio | [gemini_studio_walkthrough.md](day1/gemini_studio_walkthrough.md) | Extensions, generation modes, code toggle |
| 🔐 OpenAI Playground | [openai_playground_walkthrough.md](day1/openai_playground_walkthrough.md) | Modes, temperature, stop sequences |

---

## ⚙️ First API Calls (Colab)

You’ll test each platform directly using Python in your browser.

| Notebook | Link | Purpose |
|----------|------|---------|
| `llm_api_test_openai.ipynb` | [Run](https://colab.research.google.com/github/MariaAise/test/blob/main/llm_api_test_openai.ipynb) | ChatCompletion demo |
| `llm_api_test_gemini.ipynb` | [Run](https://colab.research.google.com/github/MariaAise/test/blob/main/llm_api_test_gemini.ipynb) | `generate_content()` call |
| `multi_provider_sandbox.ipynb` | [Run](https://colab.research.google.com/github/MariaAise/test/blob/main/multi_provider_sandbox.ipynb) | Side-by-side comparison |



---

## 🔁 Modular Code (Reference & Reuse)

These logic blocks are used across the course — and in future products.

| Module | Path | Description |
|--------|------|-------------|
| `openai_api_basic_call.md` | `codebook/apis/` | OpenAI call using `ChatCompletion.create()` |
| `gemini_api_basic_call.md` | `codebook/apis/` | Gemini call using Google SDK |
| `hf_inference_api_call.md` | `codebook/apis/` | HF pipeline + REST API |
| `platform_overview.yaml` | `codebook/llm_platforms/` | YAML metadata for limits, cost, speed |

---

## 🚧 Troubleshooting

📄 [Common API Issues](../../codebook/day1_platforms/troubleshooting_api_errors.md)  
- Invalid key errors  
- SDK mismatch  
- Colab runtime quirks  
- Quota or org-level restrictions

---

## 🧠 Reminder: GitBook Architecture

All files in this session live under:

- `gitbook/day1_platforms/`
- `notebooks/Day1_Session2/`
- `codebook/apis/`, `codebook/llm_platforms/`

This ensures your walkthroughs, code, and future product docs remain **modular and reusable**.

---

## 🗂 Suggested Reading Order

| Step | File | Purpose |
|------|------|---------|
| 1️⃣ | `platform_comparison.md` | Understand tradeoffs |
| 2️⃣ | `api_key_setup.md` | Set up for execution |
| 3️⃣ | `huggingface_walkthrough.md` | Explore HF models |
| 4️⃣ | `openai_playground_walkthrough.md` | Understand OpenAI UI |
| 5️⃣ | `gemini_studio_walkthrough.md` | Get into Gemini logic |
| 6️⃣ | `api_inference_quickstart.md` | Run a basic test |
| 7️⃣ | `troubleshooting_api_errors.md` | Fix what breaks |

---

## 🔚 What’s Next?

➡️ In **Session 3**, you’ll build on this by crafting and evaluating prompts across tasks: summarisation, classification, Q&A.

→ [Session 3: Prompt Architecture & Evaluation →](../day1_session3_prompt_architecture.md)

---

## 🔭 Up Next

➡️ [Session 3: Prompt Engineering + Platform Mastery →](day1s3_schedule.md)