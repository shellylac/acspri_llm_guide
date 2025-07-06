
---
title: Python Minimalist Foundations
description: Variables, loops, functions — core Python syntax for working with LLMs and data pipelines
tags: [python, beginner, functions, loops, variables, preprocessing, acspri]
sidebar_position: 2
slug: /day1/python-basics
---

# 🐍 Python Minimalist Foundations

> This module gives you just enough Python to be dangerous with data and LLMs. It's not a bootcamp — it's a launchpad.

---

## ✅ Why Learn Python?

Python is the language used in:
- Data analysis
- Large Language Models (LLMs)
- Automation and machine learning

If you're running GPT, Gemini, or Hugging Face models — you're using Python under the hood.

---

## 🔡 Variables

### 💡 What is a variable?

A **variable** is a named container that stores a value. It's how you hold text, numbers, lists, or anything else in memory while your code runs.

```python
name = "Maria"
age = 42
temperature = 18.7
is_ready = True
```

| Value | Type      | Description                        |
|-------|-----------|------------------------------------|
| `"Maria"` | `str`   | Text (called a *string*)            |
| `42`   | `int`     | Integer number                     |
| `18.7` | `float`   | Decimal number                     |
| `True` | `bool`    | Boolean (true or false)            |

Use `type()` to check:
```python
print(type(name))  # <class 'str'>
```

---

## 🔁 Loops

### 💡 What is a loop?

A **loop** repeats the same block of code over a list of items.

```python
topics = ["health", "climate", "education"]
for topic in topics:
    print("Analyzing:", topic)
```

### 📦 Real-World Use Case

You can use loops to process:
- Many input prompts
- A list of documents
- Survey responses

### 🔍 With Conditionals:

```python
scores = [88, 62, 45]
for score in scores:
    if score > 60:
        print("Pass:", score)
    else:
        print("Fail:", score)
```

---

## 🧱 Functions

### 💡 What is a function?

A **function** is a block of code you define once and use many times.

```python
def greet(name):
    print("Hello,", name)

greet("Maria")
```

### 📌 Why functions matter

Functions help you:
- Reuse code for multiple inputs
- Keep notebooks clean and organized
- Modularize your LLM workflows (e.g., `clean_text()`, `classify_text()`)

---

### 🔄 Function with return value:

```python
def double(x):
    return x * 2

result = double(5)
print(result)  # 10
```

---

## 🧠 Lambda Functions

### 💡 What is a lambda?

A **lambda** is a one-line anonymous function, often used inside `.apply()` in Pandas:

```python
df["length"] = df["text"].apply(lambda x: len(x))
```

- `lambda x:` says: here's a function with one input `x`
- `len(x)` is the output
- No need to write a full `def` block

Useful when:
- You're transforming a column
- You want compact logic

---

## 🔍 How to Inspect Function Parameters

When using a new library (like `pipeline()` from Hugging Face), you can explore:

```python
from transformers import pipeline
help(pipeline)
```

Or:
```python
pipeline?  # if using Jupyter/Colab
```

This will show:
- Function purpose
- Expected inputs
- Defaults

---

## ✅ Summary: Python You Actually Need

| Concept | Used For |
|--------|----------|
| `variables` | Store text, results, settings |
| `loops` | Process multiple prompts or rows |
| `functions` | Build clean, reusable pipelines |
| `lambda` | Apply small logic inside dataframes |
| `help()` | Explore unknown functions quickly |

---

## 🚀 What’s Next?

Now that you can read and write Python fluently enough:
- You’ll load text data
- Clean it with loops + functions
- Use it in LLMs (next: Hugging Face Pipelines)

**🔗 Continue to:** [`huggingface_pipeline_demo.ipynb`](../huggingface_pipeline_demo)
