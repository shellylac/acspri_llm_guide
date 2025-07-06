---
id: huggingface_chat_activity
title: Prompt Exploration Activity (Hugging Face in Colab)
description: Hands-on prompt testing activity using Hugging Face pipelines in Google Colab.
---



# 🧪 Prompting Activity: Exploring Prompts in OpenAI Playground

> Explore how prompt structure and model settings impact GPT-4 or GPT-3.5 output directly inside the OpenAI Playground.

---

## 🔹 1. Access the Playground

1. Go to [https://platform.openai.com/playground](https://platform.openai.com/playground)
2. Log in with your OpenAI account
3. Set your model to **GPT-4** or **GPT-3.5** (if GPT-4 access is enabled)

---

## 🔹 2. Copy This Prompt Template

Paste into the text area:

```
You are a science communicator. Rewrite the abstract below for a Year 10 student audience. Use plain language. Maximum 100 words.

## Abstract:
[Paste abstract here]
```

✅ Tip: Use the **"Insert"** button to test with a variety of pre-written abstracts or content snippets

---

## 🔹 3. Adjust Model Settings (Right Panel)

| Parameter         | Description                              | Suggested Range                     |
| ----------------- | ---------------------------------------- | ----------------------------------- |
| Temperature       | Controls randomness/creativity           | 0.2–0.4 = precise0.7–1.0 = creative |
| Maximum length    | Maximum number of tokens in response     | 100–300 for short tasks             |
| Top P             | Probabilistic sampling diversity control | Leave default                       |
| Frequency Penalty | Reduces repetition                       | Use 0.2–0.5 for summaries           |
| Stop Sequences    | Define where the model should stop       | Optional                            |

🧠 *Start with Temperature 0.3 for factual prompts, 0.9 for brainstorming.*

---

## 🔹 4. Try These Prompt Variants

| Type       | Modification                               |
| ---------- | ------------------------------------------ |
| Persona    | “Explain like a TED speaker.”              |
| Format     | “Return as 3 bullet points.”               |
| Style      | “Use short sentences and avoid jargon.”    |
| Constraint | “Include a real-world example or analogy.” |

---

## 🔹 5. Evaluate Output

Use this mini-rubric:

| Criterion    | GPT Output Score (1–5) |
| ------------ | ---------------------- |
| Clarity      | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5    |
| Relevance    | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5    |
| Format Match | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5    |

✍️ Optional: Copy your best output and try it again with a **slightly revised prompt**. What changes?

---

## 🔹 6. (Optional) Compare With Gemini or Claude

Try the same prompt in:

- [Gemini Pro](https://aistudio.google.com)
- [Claude](https://claude.ai)

Reflect:

- Does GPT follow structure better?
- Which model aligned more with your audience?
- How does Temperature affect tone across tools?

---

## ✅ Summary

You’ve now practiced:

- Designing precise vs. creative prompts
- Adjusting OpenAI model behavior using Temperature, Max Length, and Penalties
- Evaluating model outputs for clarity and alignment

This forms the basis for structured prompt testing inside research, teaching, and prototype workflows.

