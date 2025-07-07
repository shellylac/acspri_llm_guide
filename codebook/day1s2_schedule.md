---
id: "day1_session2_platforms"
title: "Day 1 – Session 2: Platform Walkthroughs & API Setup"
description: "Compare major LLM providers, walk through interface features"
---
![fig_day1_header](../shared_assets/visuals/images/fig_day1_session2_header.png)


# Day 1 – Session 2: Platform Walkthroughs & API Setup


## 🎯 What You’ll Learn

✅ Hugging Face platform: interface, main component, documentation  
✅ Gemini/Google AI Studio: quick overview
✅ OpenAI/OpenAI Playground: quick overview
✅ Set up API keys safely and run your first model calls  

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

## 🚧 Troubleshooting

📄 [Common API Issues](../../codebook/day1_platforms/troubleshooting_api_errors.md)  
- Invalid key errors  
- SDK mismatch  
- Colab runtime quirks  
- Quota or org-level restrictions

---

## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)

[OpenAPI Setup Guide](openai_api_setup_colab.md)

---

## 🔭 Up Next

➡️ [Session 3: Prompt Engineering + Platform Mastery →](day1s3_schedule.md)