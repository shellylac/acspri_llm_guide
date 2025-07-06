---
id: openai_api_setup_colab
title: Setting Up OpenAI API in Google Colab
description: "Step-by-step guide for securely accessing the OpenAI API in Colab using Secrets Manager and direct code methods."
---

# 🧠 Setting Up OpenAI API Access in Google Colab

This guide walks you through two secure ways to use your OpenAI API key in Google Colab:
1. **Via Google Colab's built-in Secrets Manager**
2. **Directly via environment variables in code**

---

## ✅ Step 1: Get Your OpenAI API Key

1. Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Click **"Create new secret key"**
3. Copy and store your key safely (starts with `sk-...`)

---

## 🔐 Option A: Use Colab Secrets Manager (Recommended)

### 🪪 Step A1: Open Secrets Panel

- In Colab, click the 🔑 **key icon** on the left sidebar (labeled "Secrets").

### ➕ Step A2: Add Your Secret

- Click **“+ Add new secret”**
- For **Name**, type: `OPENAI_API_KEY`
- For **Value**, paste your OpenAI key (e.g., `sk-...`)
- Click **Add**

### 🔓 Step A3: Grant Notebook Access

If prompted:

> _Notebook does not have access to secret named "OPENAI_API_KEY". Grant access?_

Click **“Grant access”** — this is **per-notebook**, required once for each.

### 🧪 Step A4: Access Key in Code

```python
from google.colab import userdata

api_key = userdata.get('OPENAI_API_KEY')
print(api_key)  # Do NOT print in production
```

---

## 🛠 Option B: Use Direct Code Input (Alternative)

> ⚠️ Less secure — use with caution. Avoid sharing or storing notebooks with keys in plaintext.

### 🧪 Set the API Key

```python
import os

os.environ['OPENAI_API_KEY'] = 'sk-...yourkeyhere'
```

Then access:

```python
api_key = os.environ.get('OPENAI_API_KEY')
```

---

## ✅ Best Practices

| Practice | Why it matters |
|---------|----------------|
| Use Secrets Manager | Keeps keys safe and out of code |
| Never hard-code in shared notebooks | Avoid leaks and accidental exposure |
| Regenerate keys regularly | Especially after public notebooks or sharing |
| Name secrets clearly | Use `OPENAI_API_KEY`, `GEMINI_API_KEY`, etc. |

---

## 🔗 Using the Key with OpenAI SDK

```python
import openai

openai.api_key = userdata.get('OPENAI_API_KEY')  # or os.environ.get('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response['choices'][0]['message']['content'])
```

---

## 🧭 You’re Ready

You can now:
- Call OpenAI endpoints from Colab
- Safely manage API keys
- Reuse this setup across projects and demos

