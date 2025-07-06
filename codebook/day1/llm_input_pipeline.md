
---
title: LLM Input Pipeline
description: How LLMs process text inputs — formatting, batch structure, prompt setup, and output unpacking
tags: [llm, pipeline, prompt, input formatting, batch processing]
sidebar_position: 3
slug: /day1/llm-input-pipeline
---

# 🧮 LLM Input Pipeline

> This module explains how LLMs take input, what formatting matters, how batching works, and how to structure both your input and output for repeatable workflows.

---

## 🎯 What is an LLM Pipeline?

A **pipeline** is the connection between:
- Your raw data (text, documents, questions)
- The model (e.g. Hugging Face, OpenAI, Gemini)
- The output (label, summary, translation)

Your goal: create a clean, modular process that can be reused for real-world tasks.

---

## 🔣 Input Format Matters

LLMs are sensitive to:
- Punctuation
- Capitalization
- Line breaks
- Input length (token limits)

### ✅ Good vs Bad Inputs

**Too short:**
```
"good"
```

**Too long:**
```
"The following is an exhaustive list of all tax legislation enacted by..." (truncated)
```

**Balanced input:**
```
"This article discusses the potential social impact of machine learning in healthcare."
```

---

## 🧺 Batch Structure

Most LLM APIs (Hugging Face, OpenAI) support **batch processing** — multiple inputs at once:

```python
texts = [
  "This is great.",
  "Needs improvement.",
  "Not sure what to think."
]
results = classifier(texts)
```

This saves time, money, and manual labor.

---

## 🧱 Prompt Templates (OpenAI / Gemini style)

In OpenAI or Gemini, you often define a **prompt template**:

```python
template = "Classify this text as POSITIVE or NEGATIVE:

{text}"
prompt = template.format(text="I love this new policy.")
```

You can wrap this in a function to generate dozens of prompts dynamically.

---

## 🔁 Looping Over Inputs with Cleanup

```python
def clean(text):
    return text.lower().strip()

def classify_batch(texts):
    return [classifier(clean(t))[0] for t in texts]
```

---

## 🧾 Output: Unpacking LLM Responses

Most LLM pipelines return a **list of dictionaries**:

```python
[{'label': 'POSITIVE', 'score': 0.998}]
```

You can extract fields like this:

```python
result = classifier("Great job!")[0]
label = result["label"]
confidence = round(result["score"], 2)
```

Wrap it for automation:

```python
def unpack(response):
    return response["label"], round(response["score"], 2)
```

---

## 📊 Example: Full Pipeline

```python
texts = ["Great work", "Needs revision", "Unclear direction"]

def process(texts):
    results = classifier(texts)
    return [(t, r['label'], round(r['score'], 2)) for t, r in zip(texts, results)]

process(texts)
```

---

## 🧠 Summary

- Clean input = better output
- Batch inputs save time
- Wrap logic into small reusable blocks
- Know the structure of LLM outputs

---

## 🔗 What’s Next?

Now that you understand inputs and outputs:
- You'll build your own **custom logic pipelines**
- Combine tools (Hugging Face, OpenAI, Gemini)
- Chain LLMs with functions for decision workflows

📘 Continue to: [`llm_response_structure.md `](llm_response_structure.md )

--

### 🔗 Related Modules

| Module                                   | Description                                                   |
| ---------------------------------------- | ------------------------------------------------------------- |
| `embed_compare_cosine.md`                | Code module for generating similarity matrix                  |
| `embeddings-and-similarity-scores.ipynb` | Live notebook demo of cosine similarity                       |
| `embedding_pipeline.md`                  | Pipeline that combines embedding + similarity + visualization |
| `day2_embeddings_basics.md`              | Main session content – this file is linked in 📐 section      |
| `label_by_similarity.md`                 | Classifies input using cosine similarity to labeled examples  |
| `train_logistic_classifier.md`           | Trains logistic regression classifier on top of embeddings    |
| `peft_finetune_demo.md`                  | LoRA fine-tuning walkthrough for more advanced users          |
