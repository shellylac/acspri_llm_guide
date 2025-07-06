---
id: google_ai_studio_activity
title: Prompt Exploration Activity (Google AI Studio)
description: Structured activity block for exploring prompt design and parameter tuning using Gemini Pro in Google AI Studio.
author: Maria Aise
status: live
version: 1.0
created: 2025-07-05
updated: 2025-07-05
module_type: activity
tags:
  - prompting
  - google_ai_studio
  - gemini
  - activity
  - hands-on
  - day1
  - session3
used_in:
  - ACSPRI Course (Day 1, Session 3)
  - GitBook
  - Prompting Sandbox Notebook
  - Solo Practice Module
---


# 🧪 Prompting Activity: Exploring Prompts in Google AI Studio (Gemini Pro)

> Use this to explore how prompt design + model parameters affect output clarity, format, and tone.

---

## 🔹 1. Choose a Task

Pick one use case from the table below and paste the sample prompt into [Google AI Studio](https://aistudio.google.com/app/prompts):

| Task Type         | Prompt Goal                                                         |
| ----------------- | ------------------------------------------------------------------- |
| Health Summary    | Translate policy text into 3 public-facing bullet points            |
| Legal Rewrite     | Simplify legal/regulatory language for non-expert readers           |
| Academic Abstract | Rephrase dense research summary for Year 10 students                |
| Grant Review      | Evaluate short proposal across clarity, feasibility, and innovation |

---

## 🔹 2. Prompt Template

Paste this into Google AI Studio:

```
# Role: Academic Simplifier

You are a science communicator. Your task is to rewrite the abstract below for Year 10 students. Use plain English. Max 100 words.

## Abstract
[Paste abstract here]
```

✅ Add structure: “Use 2 short paragraphs”\
✅ Add tone: “Make it sound like a TED talk”\
✅ Add constraints: “Include 1 real-world example”

---

## 🔹 3. Adjust Model Parameters (Gemini Panel)

| Parameter             | What It Does                                                         | When to Change                                |
| --------------------- | -------------------------------------------------------------------- | --------------------------------------------- |
| **Temperature**       | Controls randomness. Lower = focused, higher = creative              | 0.2–0.4 for summaries; 0.7–1.0 for creativity |
| **Top-K / Top-P**     | Samples token pool. Defaults are fine unless tweaking tone diversity | Advanced only                                 |
| **Max Output Tokens** | Limits length of output                                              | 100–250 for most tasks                        |
| **Stop Sequences**    | Specifies where output should end                                    | Optional for truncation control               |

🧠 *Tip: Try Temperature = 0.3 for precision and 0.9 for brainstorming.*

---

## 🔹 4. Explore Prompt Variants

| Dimension   | What to Add                                            |
| ----------- | ------------------------------------------------------ |
| **Persona** | “You are explaining to a nervous parent.”              |
| **Format**  | “Respond in a table: Point / Why It Matters / Analogy” |
| **Clarity** | “Use short, active sentences only.”                    |
| **Tone**    | “Sound like a TED speaker giving advice to students.”  |

---

## 🔹 5. Reflect & Score

| Criterion      | Gemini Output Score (1–5) |
| -------------- | ------------------------- |
| Clarity        | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5       |
| Relevance      | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5       |
| Follows Format | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5       |

✍️ Optional: Write 2 lines on what you’d tweak in your next version.

---

## 🔹 6. (Optional) Compare with GPT or Claude

Paste the same prompt into:

- [ChatGPT (GPT-4)](https://chat.openai.com)
- [Claude](https://claude.ai)
- [Hugging Face Chat](https://huggingface.co/chat)

Reflect:

- Which followed the instruction better?
- Which tone felt more aligned with your audience?
- What would you change to improve Gemini’s version?

---

## ✅ Summary: What You Learn

- How prompt **structure + constraints** shape model output
- How **temperature and token limits** affect output diversity
- How to **adapt prompts** for different audiences and formats

