---
id: prompt_eval_interface
title: LLM Evaluation App – Interface Blueprint
description: Simple evaluation interface to rate and compare LLM outputs using sliders and structured logic
tags: [prompt evaluation, streamlit pattern, user interface, research tools]
status: draft
---

# 🧱 LLM Evaluation App – Interface Blueprint

This is the design for a simple web app to **evaluate LLM-generated responses** using sliders and structured inputs.

---

## 🔹 What it does

- Lets you **test and compare multiple prompt versions**
- Helps you **rate the quality of generated output**
- Automatically calculates a score and justification
- Lets you export your evaluations or save them to Notion

---

## 🔹 What it looks like  
_Think of it as a smart form you interact with in your browser_

| Section | Purpose |
|--------|---------|
| **Prompt Version (Dropdown)** | Choose which version of your prompt was used (e.g., V1: zero-shot, V2: CoT, etc.) |
| **Generated Output (Text Box)** | Paste the response you got from the model |
| **Scoring Sliders** | Rate the output on:  
  - Relevance  
  - Completeness  
  - Clarity |
| **Auto Score + Summary** | Calculates a total score and generates a justification like:  
  _"This output is moderately relevant and clear, but lacks detail."_ |
| **Save / Export** | Download scores as CSV or send to a workspace like Notion |

---

## 🧠 Why it matters (especially for researchers)

- Forces **explicit evaluation criteria**
- Helps you **track what works and why**
- Enables **structured experimentation** with prompt types
- Makes LLM quality assessment **visible, explainable, and auditable**

---


