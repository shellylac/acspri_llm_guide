---
id: huggingface_api_setup_colab
title: Setting Up Hugging Face API in Google Colab
description: Step-by-step guide for accessing Hugging Face models in Colab using the API key securely via Secrets Manager and code.
tags: [huggingface, colab, api, secrets, setup]
status: live
---

# 🤗 Setting Up Hugging Face API Access in Google Colab

Use this guide to securely access Hugging Face’s hosted inference API from Colab notebooks using either:

1. **Google Colab's Secrets Manager** *(recommended)*  
2. **Direct environment variable assignment** *(alternative)*

---

## ✅ Step 1: Get Your Hugging Face Token

1. Log into [https://huggingface.co](https://huggingface.co)
2. Go to **Settings > Access Tokens**
3. Click **“New token”** (select `read` scope for most use cases)
4. Copy the token (starts with `hf_...`)

---

## 🔐 Option A: Use Colab Secrets Manager

### 🪪 Step A1: Open the Secrets Tab

- Click the 🔑 **Secrets** icon in the Colab left sidebar.

### ➕ Step A2: Add New Secret

- Click **“+ Add new secret”**
- **Name**: `HF_TOKEN`
- **Value**: Paste your Hugging Face API token

### 🔓 Step A3: Grant Access to Your Notebook

When prompted:
> _Notebook does not have access to secret named "HF_TOKEN"_

Click **“Grant access”**

### 🧪 Step A4: Use in Code

```python
from google.colab import userdata

hf_token = userdata.get('HF_TOKEN')
```

You can now pass this token to `transformers` or `requests`.

---

## 🛠 Option B: Set API Key Directly in Code

⚠️ **Not recommended** in shared or production notebooks.

```python
import os

os.environ['HF_TOKEN'] = 'hf_your_token_here'
```

Use in Python:

```python
hf_token = os.environ.get('HF_TOKEN')
```

---

## 🔗 Using with `transformers` Library

For hosted models (e.g., using `pipeline` with remote access):

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english", 
                use_auth_token=hf_token)

pipe("I love open-source NLP!")
```

Or for REST API calls:

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer {hf_token}"}

response = requests.post(API_URL, headers=headers, json={"inputs": "This is awesome!"})
print(response.json())
```

---

## ✅ Best Practices

| Practice | Benefit |
|----------|---------|
| Use Secrets Manager | Avoids exposing keys in code |
| Name consistently | `HF_TOKEN`, `OPENAI_API_KEY`, etc. |
| Regenerate tokens when exposed | Especially after sharing notebooks |
| Don’t store tokens in `.ipynb` files | Keep notebooks portable and secure |

---

## 🧠 You’re Ready

You can now:
- Run hosted Hugging Face models
- Use transformers locally or remotely
- Plug into APIs securely via token control
