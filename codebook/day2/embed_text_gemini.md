
# 🤖 Module: Text Embeddings using Gemini

## 📌 Purpose

This module uses the **Google Gemini API** to generate interpretive responses about sentence meaning.  
It is not a true "embedding" in the vector space sense — but it allows you to **probe what a language model "thinks"** a sentence means.

Used in **Day 2 Session 1** to compare:
- Gemini’s natural language interpretation
- Hugging Face’s numeric sentence embeddings

---

## 🧠 When to Use This

Use Gemini for:
- **Interpretability**: explain sentence meaning in plain English
- **Prompt-based diagnostics**: how LLMs respond to contrastive language
- **Framing analysis**: see how model tone or sentiment shifts
- **Prompt audits**: test prompt sensitivity across variations

Not suitable for:
- Quantitative similarity
- Vector-based downstream workflows (e.g., clustering, classification)

---

## 🔐 Requirements

- Free Gemini API key: https://makersuite.google.com/app/apikey
- `google-generativeai` Python package

```bash
pip install -q google-generativeai
```

---

## ⚙️ Function

```python
import google.generativeai as genai

def get_gemini_explanation(prompt, model_name="gemini-pro", api_key="YOUR_API_KEY"):
    # Sends a text-based prompt to Gemini and returns the model's response.
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text
```

---

## 🧪 Example Usage

```python
prompt = "Compare the meaning of: 'The minister supported the bill.' and 'The minister opposed the bill.'"
meaning = get_gemini_explanation(prompt, api_key="your-key-here")
print(meaning)
```

Expected output (truncated):

> "The first sentence expresses agreement or endorsement, while the second indicates resistance or disagreement..."

---

## 🧠 Use Case: Gemini vs HF in Parallel

You can use Gemini to generate interpretive explanation, and Hugging Face to quantify similarity:

```python
# Gemini: Interpret meaning
get_gemini_explanation(prompt)

# Hugging Face: Compute cosine similarity
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(["Sentence A", "Sentence B"])
```

---

## 🧪 Caution on Output

- Gemini's responses are **non-deterministic** (may vary each run)
- Great for human-facing audits, not math-based pipelines
- May reflect bias or framing embedded in training data

---

## 🔁 Applications

| Context | Use |
|---------|-----|
| Prompt testing | Interpret subtle prompt phrasing effects |
| Semantic contrast | Verify whether two sentences express similar meaning |
| Policy framing | Compare model interpretation of different wordings |
| Narrative analysis | Help interpret clustering output qualitatively |

---

## 🪪 Author  
*Maria Aise — Modular Codebook, ACSPRI 2025*  
Part of the hybrid Gemini + Hugging Face semantic probe toolkit

---

## 🧱 Related Modules

| Module                                   | Description                                               |
|------------------------------------------|-----------------------------------------------------------|
| `embed_text_hf_basic.md`                | Generate sentence embeddings for cosine/vector analysis   |
| `embed_compare_cosine.md`               | Compute similarity scores from Hugging Face embeddings    |
| `day2_llm_meaning_instruments.ipynb`   | Notebook using Gemini+HF for semantic reasoning comparison |
