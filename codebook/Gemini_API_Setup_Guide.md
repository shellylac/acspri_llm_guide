---
id: gemini_api_setup_guide
title: Gemini API Setup Guide (Non-Technical)
type: guide
---

# 🌐 Gemini API Setup Guide (Non-Technical)

This guide walks you through how to **activate and use the Gemini Pro API** from Google.  
No coding experience required — perfect for workshop participants, research assistants, or clients.

---

## ✅ What You’ll Need

| Requirement       | Description                                              |
|-------------------|----------------------------------------------------------|
| Google Account    | Use any Gmail or institutional Google account            |
| Browser           | Chrome, Safari, Firefox — anything modern will work      |
| Email Access      | You may receive a confirmation or billing notice         |

---

## 🚀 Step 1: Get Your Gemini API Key

1. Go to: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Log in with your Google account (if prompted)
3. Click the **“Create API Key”** button
4. Copy the key — it looks like:  
   `AIzaSyXXXX...`
5. **Save this key** in a secure place (Notion, Password Manager, etc.)

> 🛑 Never share this key publicly. It gives access to your Gemini quota.

---

## 🧪 Step 2: Test Your Key (Optional)

Paste the following into a Python notebook or script:

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_KEY_HERE")
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Explain how LLMs generate text.")
print(response.text)
```

If successful, Gemini will return a paragraph.

---

## 💰 Step 3: Check Free Tier

Google’s **free usage tier** gives you:

- Limited free generations per month (e.g. 60–100)
- Access to `gemini-pro` model
- No credit card required for initial use

> For advanced usage (batch processing, analytics), you may upgrade to a paid tier later.

---

## 💡 Pro Tips

| Tip | Why It Helps |
|-----|--------------|
| Save your key in `.env` or notebook variables | Prevents leaks in shared files |
| Use Gemini in qualitative workflows | Interpret surveys, check framing, explain similarity |
| Combine with HF or OpenAI | Great for hybrid audits or mixed-methods pipelines |

---

## 🧱 Related Modules

| Module                      | Description                                 |
|-----------------------------|---------------------------------------------|
| `embed_text_gemini.md`      | Uses your Gemini key to embed or explain    |
| `compare_gemini_vs_hf.md`   | Benchmarks Gemini vs Hugging Face models    |
| `semantic_drift_detector.ipynb` | Uses Gemini to explain tone/framing shifts |

---

## 🪪 Author  
*Maria Aise — Modular Codebook, ACSPRI 2025*  
This guide boosts onboarding speed and confidence for both students and clients.
