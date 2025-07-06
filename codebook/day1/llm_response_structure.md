---
title: "LLM Response Structure"
description: "How LLMs return data — understanding dictionaries, JSON format, and how to unpack them in Python"

---

# 📦 LLM Response Structure

> This module shows how to interpret the output from any LLM — Hugging Face, OpenAI, or Gemini — by understanding dictionaries, JSON, and unpacking.

---

## 🔍 LLMs Return Dictionaries (or JSON)

When you call an LLM through a pipeline or API, it returns data in structured format.

```python
result = classifier("This is amazing!")
print(result)
```

Output:
```python
[{'label': 'POSITIVE', 'score': 0.9987}]
```

---

## 🧠 Key Terms

| Term        | Meaning                              |
|-------------|---------------------------------------|
| `dictionary`| Key-value data in Python              |
| `JSON`      | Text-based format for key-value data  |
| `key`       | The label used to identify a value    |
| `value`     | The actual data (text, number, etc.)  |

Python dictionaries **are** valid JSON. You can convert between them using:

```python
import json
json_string = json.dumps(result)      # dict → JSON
parsed_dict = json.loads(json_string) # JSON → dict
```

---

## 🛠 How to Unpack a Single Response

```python
output = result[0]
label = output["label"]
score = output["score"]

print("Label:", label)
print("Confidence:", round(score, 2))
```

📌 Always use `.get("key")` if you’re unsure if the key is present:
```python
label = output.get("label", "unknown")
```

---

## 🔁 Unpack in a Loop

```python
texts = ["Great job!", "Terrible service."]
results = classifier(texts)

for text, res in zip(texts, results):
    print(text, "→", res["label"], f"({res['score']:.2f})")
```

---

## 🔧 Wrap Into a Function

```python
def unpack_response(response):
    return {
        "label": response["label"],
        "confidence": round(response["score"], 2)
    }
```

Use in context:
```python
unpack_response(result[0])
```

---

## 🧾 Working with Nested Structures

Some APIs return more complex output, such as:

```python
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Here's a summary..."
      }
    }
  ]
}
```

To access the message:
```python
output["choices"][0]["message"]["content"]
```

---

## ✅ Summary

- LLMs return outputs as dictionaries or JSON (key-value pairs)
- Use Python indexing and key access to unpack
- Loop through batches for automation
- Wrap in functions for reuse

📘 Continue to: [`llm_response_explainer.ipynb `](llm_response_explainer.md )

---

### 🔗 Related Modules

| Module                                   | Description                                                   |
| ---------------------------------------- | ------------------------------------------------------------- |
| `huggingface_pipeline_demo.ipynb`        | First notebook using pipeline and reading response structure  |
| `llm_input_pipeline.md`                  | How to structure input and batch for the model                |
| `embedding_pipeline.md`                  | Applies unpacking to vector similarity tasks                  |
| `label_by_similarity.md`                 | Unpacks similarity and classifies text by distance            |
