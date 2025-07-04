---
id: classify_policy_stance
title: Policy Stance Classification – Cosine + Embedding Classifier
tags: [classification, embeddings, cosine, policy, stance]
type: notebook
---

# 🧭 Classify Policy Stance – Step-by-Step

This notebook demonstrates 3 levels of classification using sentence embeddings:

1. **Zero-shot** via cosine similarity  
2. **Few-shot** (expanded anchors)  
3. **Supervised classifier** using logistic regression  
4. *(Optional)* Intro to LoRA fine-tuning

> 📘 This file is used in Session 3, Day 2 of the ACSPRI course.

---

## 🔹 1. Zero-Shot Classification

In zero-shot classification, we assign labels to new input texts **without training a model**.  
Instead, we compare each input to a small number of **anchor examples** that represent each class.  

The idea: if a sentence is semantically similar to known examples of a label, it probably belongs to that label.

This method uses **cosine similarity** in embedding space.

You’ll need:
- A list of representative examples per label
- A sentence embedding model (like `all-MiniLM-L6-v2`)
- A similarity function to compare input with anchors


### 🧰 Basic Version (Beginner-Friendly)

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def classify_text_basic(text, anchors, model):
    text_vec = model.encode([text])[0]
    scores = {}
    for label, examples in anchors.items():
        sims = [cosine_similarity([text_vec], [model.encode([ex])[0]])[0][0] for ex in examples]
        scores[label] = np.mean(sims)
    return max(scores, key=scores.get), scores
```

> ✅ Use this to understand the basic math: embed, compare, average.

---

### 🚀 Upgraded Version (GPU/Threshold Ready)

```python
import torch

def classify_text(text, anchors, min_confidence=0.3):
    text_vec = model.encode(text, convert_to_tensor=True)
    scores = {}
    for label, examples in anchors.items():
        example_vecs = model.encode(examples, convert_to_tensor=True)
        sims = torch.nn.functional.cosine_similarity(
            text_vec.unsqueeze(0),
            example_vecs
        )
        scores[label] = sims.mean().item()

    best_label = max(scores, key=scores.get)
    return (best_label, scores) if scores[best_label] >= min_confidence else ("Uncertain", scores)
```

> 🧠 Optimized for speed, confidence scoring, and Colab use.

---

## 🔁 2. Few-Shot Expansion

The zero-shot method works better with more anchor examples. This is called **few-shot classification**.

Each label category should ideally have 3–5 diverse examples:
- Cover different phrasings (formal, casual, sarcastic)
- Include borderline or weak examples
- Pull real quotes from your domain (surveys, interviews, etc.)

This improves:
- **Coverage** (captures broader meaning)
- **Stability** (less bias from single-word triggers)
- **Interpretability** (anchors look like your data)


Add 3–5 anchor examples per label to boost accuracy.

```python
anchor_examples = {
    "Supportive": [
        "I support the policy.",
        "It’s the right move.",
        "Very happy with this."
    ],
    "Neutral": [
        "I need more info.",
        "Still undecided.",
        "Mixed feelings."
    ],
    "Opposed": [
        "This is wrong.",
        "It restricts freedom.",
        "I'm against this."
    ]
}
```

---

## 🔸 3. Supervised Classifier on Embeddings

If you have labeled data (e.g. 100 survey responses already tagged), you can train a classifier.

Instead of using words directly, we embed each sentence into a vector and then train a classifier like **logistic regression** or **SVM**.

Why use this approach?
- More accurate than zero-shot similarity
- Uses labels to learn a decision boundary
- Works well with small-to-medium datasets (50–500 samples)

We’ll show both a basic and upgraded version.


### 🧰 Basic Version

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

print("Accuracy:", clf.score(X_test, y_test))
```

> ✅ Good for 30–300 labeled examples.

---

### 🚀 Upgraded Version

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

clf = make_pipeline(
    StandardScaler(),
    LogisticRegression(class_weight='balanced', max_iter=1000)
)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
```

> 🧠 Balanced, scalable, and gives precision/recall/F1.

---

## 🧪 4. Optional: Try PEFT (LoRA Fine-Tuning)

If your task is complex or domain-specific — and you have 500+ labeled samples — you can fine-tune the model itself.

We use **LoRA** (Low-Rank Adaptation), a technique that injects trainable weights into a frozen model.  
This is part of the **PEFT** (Parameter-Efficient Fine-Tuning) family.

Advantages:
- Doesn’t require retraining the full model
- Memory-efficient (can run on Colab or small GPUs)
- More powerful than shallow classifiers

If you're not ready to train your own model yet, skip this — it’s an optional extension.

📘 See guide: [`peft_finetune_demo.md`](./peft_finetune_demo.md)


See: [`peft_finetune_demo.md`](./peft_finetune_demo.md)  
Notebook: [`peft_finetune_demo.ipynb`](../codebook/classification/peft_finetune_demo.ipynb)

---

## 📘 Recommended Use

| Technique            | Use When...                             |
|----------------------|------------------------------------------|
| Cosine Similarity    | You have no training labels              |
| Logistic Regression  | You have 30–500 labeled examples         |
| LoRA Fine-Tuning     | You want high performance + customization |

🔗 Related Modules

| Module                                   | Description                                                   |
| ---------------------------------------- | ------------------------------------------------------------- |
| `embed_compare_cosine.md`                | Code module for generating similarity matrix                  |
| `embeddings-and-similarity-scores.ipynb` | Live notebook demo of cosine similarity                       |
| `embedding_pipeline.md`                  | Pipeline that combines embedding + similarity + visualization |
| `day2_embeddings_basics.md`              | Main session content – this file is linked in 📐 section      |
| `label_by_similarity.md`                 | Classifies input using cosine similarity to labeled examples  |
| `train_logistic_classifier.md`           | Trains logistic regression classifier on top of embeddings    |
| `peft_finetune_demo.md`                  | LoRA fine-tuning walkthrough for more advanced users          |

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
