# 🧠 Chain-of-Thought (CoT)

## What It Is:

**Chain-of-Thought (CoT)** is a reasoning strategy where the LLM is prompted to break down a problem into **explicit intermediate steps**, rather than jumping to an answer. Think of it as teaching the model to “think aloud.”

This results in:

* More accurate answers
* Better interpretability
* Easier error diagnosis

CoT is a **prompt-only technique** — no tools or APIs needed. It’s lightweight and highly effective across tasks.

---

## 🧩 Step-by-Step Breakdown

Here’s how CoT reasoning unfolds:

| Step                          | Function                             | Example Output                                                                 |
| ----------------------------- | ------------------------------------ | ------------------------------------------------------------------------------ |
| 1. **User Input**             | The user provides a question or task | “Which country has the larger population: Australia or Germany?”               |
| 2. **Step-by-Step Thought**   | The model breaks it down logically   | “First, I’ll recall population sizes. Australia has \~26M, Germany has \~83M…” |
| 3. **Intermediate Reasoning** | The model makes comparisons          | “Germany’s population is significantly higher.”                                |
| 4. **Final Answer**           | The model concludes explicitly       | “So the answer is Germany.”                                                    |

---

## 🧪 Examples in Action

### 🔹 Example 1: Numerical Reasoning

**Prompt:**
*“If a train leaves the station at 3 PM and travels 80km at 40km/h, what time does it arrive?”*

**CoT Response:**

> 1. It’s going 80 km at 40 km/h.
> 2. Time = distance / speed = 80 / 40 = 2 hours.
> 3. 3 PM + 2 hours = 5 PM.
>    Final Answer: 5 PM

### 🔹 Example 2: Social Science Coding

**Prompt:**
*“Does this quote support or oppose the policy change?”*

**Quote:**
*“I think we’ve had enough of this government meddling in local services.”*

**CoT Response:**

> 1. The speaker refers negatively to government involvement.
> 2. “Had enough” implies frustration or opposition.
> 3. “Meddling” is a negative term.
>    Final Answer: Opposes the policy.

---

## 🔁 CoT Inside ReAct: How It’s Used Together

CoT can be **nested inside ReAct’s `Thought:` steps**, giving structured reasoning before tool use.

```plaintext
Thought: First, I’ll identify the topic of this document. Then I’ll look for supporting evidence. Finally, I’ll match it to a code.
Action: classify_document
Action Input: "Text..."
```

Used this way, CoT improves **traceability**, especially in qualitative and mixed-method workflows.

---

## 🛠 How to Implement CoT as a Developer

### 🔹 Prompt Template

```python
prompt = f"""
Question: {user_input}
Let’s think step by step.
"""
```

You can enhance it with:

* Few-shot examples
* Prepend phrases like:

  * “Let’s reason through this.”
  * “Here’s how I’ll approach the problem.”

### 🔹 Fine-Tuning

Many models (like `openchat`, `phi-2`, `deepseek`, `GPT-4o`) **respond well to CoT prompting out of the box** — no fine-tuning needed.

If fine-tuning: train on `question + step-by-step + answer` pairs.

---

🔹**Example: Qualitative Interview Coding (Social Science)**

**Research Prompt:**
*“Classify the participant's statement into one of the following sentiment codes: `Supports`, `Neutral`, or `Opposes` regarding trust in government interventions.”*

**Quote:**

> *“They keep saying it’s for our safety, but I don’t feel like anyone’s actually listening to us.”*

---

### 🧠 CoT Response:

> 1. The speaker references the government's justification: “it’s for our safety.”
> 2. However, this is followed by a personal sentiment: “I don’t feel like anyone’s actually listening.”
> 3. The contrast indicates skepticism or dissatisfaction.
>    Final Answer: **Opposes**

---

### ✅ Why this is a good CoT use case:

* **Interpretive nuance** — not just keyword-based
* **Clear intermediate reasoning** — allows auditability and training
* **Applicable to automated coding agents** — can be embedded in `Thought:` field of a ReAct loop or used alone

---

### 🛠 Prompt Template You Can Use in Practice

```text
Classify the participant's statement into one of the following codes: Supports, Neutral, Opposes (regarding trust in government interventions).

Quote:
"They keep saying it’s for our safety, but I don’t feel like anyone’s actually listening to us."

Let’s think step by step.
```

This will trigger CoT behavior in GPT-4, Claude, Gemini 1.5, or even open models like Mistral, DeepSeek, or OpenChat.

---

## ✅ When to Use CoT

| Use Case                       | Why CoT Helps                           |
| ------------------------------ | --------------------------------------- |
| Survey response interpretation | Makes reasoning explicit and verifiable |
| Policy stance classification   | Helps model explain judgment            |
| Arithmetic, logic, deduction   | Reduces hallucination                   |
| Coding open-ended responses    | Mirrors how researchers think aloud     |

---

## ⚖️ CoT vs. ReAct vs. ToT

| Feature         | CoT               | ReAct                   | ToT                        |
| --------------- | ----------------- | ----------------------- | -------------------------- |
| Tools used      | ❌ No              | ✅ Yes                   | ❌ (typically)              |
| Looping         | ❌ One-pass        | ✅ Iterative             | ✅ Exploratory              |
| Clarity         | ✅ High            | ✅ Medium                | ❌ Often abstract           |
| Deployment ease | ✅ Easy            | ⚠️ Moderate             | 🚧 Complex                 |
| Best for        | Clear logic tasks | Tool-use, API workflows | Planning, open-ended paths |

---

## ⚠️ Limitations

* **No tool use**: Can’t fetch data, call APIs, or look up facts
* **No feedback loop**: Doesn’t adjust if wrong mid-stream
* **Overconfidence risk**: Can look logical even when incorrect
* **Doesn’t explore alternatives**: Only one reasoning path is followed

---

## 🧠 Summary

Use **Chain-of-Thought** when:

* You want **transparency** in logic
* Tasks don’t require external tools
* You’re working with **structured classification or deduction**

It’s the **default cognitive scaffold** inside many larger agent architectures — often wrapped by ReAct for execution or ToT for exploration.

---
## Related Modules


| Module                   | Description                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| `agent.md`    | Overview of LLM-based agents: what they are, how they differ from standalone models, and how reasoning, memory, and tools are orchestrated in modern agent architectures. Includes examples of agent workflows and social science use cases. |
| `agent_frameworks.md`    | Overview and classification of reasoning frameworks (CoT, ReAct, ToT) for agent design               |
| `cot.md`                 | Explanation of Chain-of-Thought (CoT) reasoning with breakdowns, examples, and visuals               |
| `react.md`               | ReAct framework loop explained: Thought → Action → Observation cycle and tool use                    |
| `tot.md`                 | Tree-of-Thoughts logic explained with examples of multi-path reasoning and selection                 |
| `tools.md`               | Agent tool registry and usage pattern (how to define, route, and call external tools)                |
| `extensions.md`          | How to extend agent capabilities with memory, RAG, chaining, or planning mechanisms                  |
| `function_call.md`       | OpenAI-style function calling interface: how LLMs call structured functions in agent workflows       |
| `targeted_learning.md`   | Prompt engineering strategies for social science use cases: guided logic, labels, and intent control |
| `langchain_basics.ipynb` | Jupyter notebook demo of basic agent setup using LangChain (tools, prompt templates, loop)           |
| `cot_vs_react_comparison.ipynb` | Side-by-side notebook comparing CoT-only vs ReAct-based workflows on social science tasks (e.g. coding, classification, search + reasoning). Includes performance notes, structure differences, and when to use which. |
| `cot_finetune.ipynb)` |  Notebook demo showing how to fine-tune a language model (e.g. Mistral, Phi-2) on Chain-of-Thought (CoT) reasoning patterns using instruction-style datasets. Includes PEFT-based LoRA setup, custom training examples for social science tasks, and explanation of when fine-tuning is necessary versus prompt-only CoT.|

---

## 🔮 What’s Next?

Next: [react.md]()

➡️ You’ve explored linear reasoning with Chain-of-Thought — now we shift to **ReAct**, where agents don’t just think, they act.
In this module, you’ll learn how LLMs follow a **Thought → Action → Observation** loop to interact with real-world tools, adjust their reasoning based on feedback, and handle multi-step tasks.
This framework powers tool-using agents — from document classification to dynamic search, summarization, and decision-making workflows in social science and beyond.
