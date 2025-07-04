---
id: train_logistic_classifier
title: Train Classifier on Sentence Embeddings
tags: [classification, embeddings, logistic regression, supervised learning]
type: module
---

# 📊 Train Classifier on Sentence Embeddings

This module shows how to train a lightweight supervised classifier (e.g., **logistic regression**) on top of **sentence embeddings**.  
It’s a fast, interpretable upgrade when you have labeled examples and need better accuracy than zero-shot similarity.

---

## 🧠 When to Use

- You have 50–500 labeled examples
- Your task is stable and low-stakes (e.g., open-end survey coding)
- You want a baseline supervised model without GPUs or deep learning

---

## ✅ Step-by-Step

### 1. Prepare Your Labeled Text

```python
all_texts = [
    "The policy will reduce CO2 emissions.",
    "I support climate change action.",
    "I’m not sure what to think.",
    "This is a waste of resources.",
    "Neutral stance overall.",
    "Totally disagree with the direction"
]

all_labels = [
    "Supportive", "Supportive",
    "Neutral",
    "Opposed", "Neutral", "Opposed"
]
```

---

### 2. Generate Sentence Embeddings

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

X = [model.encode(text) for text in all_texts]
y = all_labels
```

---

### 3. Train Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

print("Accuracy:", clf.score(X_test, y_test))
```

---

### 4. Predict New Inputs

```python
def classify(text):
    vec = model.encode([text])
    return clf.predict(vec)[0]

classify("I support the new initiative.")
```

---

## 🔬 Notes

- Embeddings make this model much stronger than plain TF-IDF.
- No need to tune deep models — this is fast and good enough for many use cases.
- Logistic regression is also **explainable**: use `clf.coef_` to explore weights.

---

## 🧩 Tips

- Label diversity matters — don’t train on templated inputs.
- You can extend this to SVM, random forests, etc.
- Use this as a “baseline model” before trying LoRA or full fine-tuning.

---

## 🔗 Related Modules

- [`label_by_similarity.md`](./label_by_similarity.md) — Zero/few-shot cosine-based classification  
- [`peft_finetune_demo.md`](./peft_finetune_demo.md) — Advanced fine-tuning using LoRA

