---
id: hf_inference_api_call
title: Hugging Face Inference API – Basic Call (Hosted Models)
type: code
---

# 🤖 Hugging Face Inference API – Basic Call (Hosted Models)

This module defines a reusable Python wrapper for **making hosted model requests** to the Hugging Face Inference API.

It works with:
- Hosted models (e.g., `google/flan-t5-small`, `facebook/bart-large`)
- Public endpoints or gated models with approved access
- Use in zero-setup pipelines or client demos

---

## 🔐 Requirements

```bash
pip install requests
```

---

## 📦 Function: `query_huggingface_api`

```python
import requests

def query_huggingface_api(prompt, model_name, api_token, task="text2text-generation"):
    """Send a text prompt to a hosted HF model and return result."""
    headers = {"Authorization": f"Bearer {api_token}"}
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"❌ API Error: {response.status_code} – {response.text}")

    result = response.json()
    return result
```

---

## ✅ Example Usage

```python
reply = query_huggingface_api(
    prompt="Translate English to French: The weather is nice.",
    model_name="t5-small",
    api_token="your-hf-token"
)

print(reply)
```

---

## 🛠️ Notes

- Task is usually inferred by the model type (e.g., T5 → text2text).
- You can check model status or license before using.
- Add `parameters` to payload for max_length, temperature, etc.
- Returns JSON array or object depending on the model.

---

## 🔄 Custom Payloads

```python
payload = {
  "inputs": "Summarize this long article...",
  "parameters": {
    "max_length": 120,
    "temperature": 0.3
  }
}
```

---

## 🔗 Related Modules

| File                                | Purpose                                  |
|-------------------------------------|-------------------------------------------|
| `api_key_setup.md`                  | API token generation for Hugging Face     |
| `api_inference_quickstart.md`       | Comparison with Gemini and OpenAI APIs    |
| `compare_gemini_vs_hf.md`           | Output behavior comparison                |
| `hf_local_transformer_pipeline.md`  | Local Transformers pipeline call          |

---