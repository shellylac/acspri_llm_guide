---

---

# 🧪 Prompting Activity: Hugging Face Prompt Testing in Google Colab

> Explore how open-source LLMs behave using Hugging Face pipelines and tasks in Google Colab.

---

## 🔹 1. Setup in Colab

Open a new [Google Colab notebook](https://colab.research.google.com) and run:

```python
!pip install -q transformers accelerate
```

Then import:

```python
from transformers import pipeline
```

---

## 🔹 2. Choose a Task

Supported task types:

- `text-generation`
- `summarization`
- `text2text-generation`

Example setup:

```python
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

---

## 🔹 3. Define Prompt Input + Parameters

Define the input content:

```python
input_text = """
Australia’s rural health report identifies increased rates of diabetes, lower vaccine coverage, and access disparities.
"""
```

Now test with a text-generation pipeline:

```python
generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")
output = generator(
    f"Summarise this: {input_text}",
    max_new_tokens=100,            # Controls length of response
    temperature=0.7,               # Creativity (0.2 = precise, 1.0 = creative)
    top_k=50,                      # Top-K filtering for sampling
    top_p=0.9,                     # Nucleus sampling (Top-P)
    repetition_penalty=1.1        # Reduces repeated phrases
)
print(output[0]['generated_text'])
```

🧠 **Tips:**

- Use `max_new_tokens=250` for full summaries
- Set `temperature=0.3` for clinical tone, `0.9` for marketing-style rewrites
- Try `repetition_penalty=1.2` when getting redundant outputs

---

## 🔹 4. Use Structured Prompt Templates

Prompting open-source models benefits from clearly defined structure. Use roles, tasks, and constraints explicitly:

```python
prompt = f"""
You are a public health communicator. Rewrite the following text for a Year 10 audience using plain English. Add 3 bullet points and a real-world example.

## Text:
{input_text}
"""
```

Try this prompt with different tasks:

```python
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")
result = pipe(prompt, max_new_tokens=200, temperature=0.6)
print(result[0]['generated_text'])
```

✅ **Add structure with:**

- “Respond in Markdown”
- “Use simple headings and bullet points”
- “Speak as if presenting to school council”

🧠 **Best Practice:** Modular prompts can be passed into reusable pipelines and tracked per task variation.

---

## 🔹 5. Try Different Models

| Model                           | Description                       |
| ------------------------------- | --------------------------------- |
| `tiiuae/falcon-7b-instruct`     | Chat-style open source LLM        |
| `mistralai/Mistral-7B-Instruct` | Compact and high-performing model |
| `facebook/bart-large-cnn`       | Best for summarization            |

```python
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")
pipe(prompt, max_new_tokens=200)
```

---

## 🔹 6. Evaluate Output

| Criterion | Score (1–5)         |
| --------- | ------------------- |
| Clarity   | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5 |
| Relevance | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5 |
| Structure | ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5 |

✍️ Reflection: Does output follow role/tone? Is it suitable for non-expert readers?

---

## ✅ Summary

- Hugging Face makes it easy to run open models in Colab
- Prompt structure + decoding parameters impact output style and quality
- Use task-specific pipelines (`summarization`, `text-generation`) and tune with temperature/top-k/token limits

---

📎 [Prompt Evaluation →](prompt_evaluation.md)\
📎 [Prompting Sandbox →](prompting_sandbox_v2.ipynb)\
📎 [Google AI Studio Activity →](google_ai_studio_activity.md)\
📎 [OpenAI Playground Activity →](openai_playground_activity.md)

