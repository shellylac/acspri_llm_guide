---
id: trigger-agent-lite
title: Trigger Detector Agent (Lite Version)
description: A lightweight LangChain agent using the ACP loop to detect trigger terms in user input; no external retrieval required.
tags: [agent, trigger, classification, react, acp, langchain, lite]
status: demo
---

# 🧠 Trigger Detector Agent (Lite)

This is a minimal working example of an **ACP-style LangChain agent** designed to detect triggering content using internal tools — no external RAG, memory, or database required.

---

## 🧾 Agent Description

```python
"""
Agent Name: TriggerDetector (Lite)
Purpose: Classify whether input text contains triggering or sensitive language based on keyword patterns
LLM: Gemini or OpenAI
Tools: KeywordScanner, SimpleClassifier
Framework: ACP + ReAct loop
RAG: ❌ Not used in this version
"""

### 🛠 Tools
🔹 Tool 1: scan_for_triggers
```python
from langchain_core.tools import tool

@tool
def scan_for_triggers(text: str) -> str:
    """Returns list of matched trigger terms from a predefined keyword list."""
    keywords = ["violence", "trauma", "abuse", "assault"]
    matches = [kw for kw in keywords if kw in text.lower()]
    return ", ".join(matches) if matches else "None"
```

### 🔹 Tool 2: classify_trigger_severity

```python
@tool
def classify_trigger_severity(matched_terms: str) -> str:
    """Returns low / moderate / high severity based on trigger term count."""
    count = len(matched_terms.split(","))
    if count == 0:
        return "None"
    elif count == 1:
        return "Low"
    elif count <= 3:
        return "Moderate"
    else:
        return "High"
```
### 🤖 LLM Setup

```python
USE_GEMINI = True

if USE_GEMINI:
    from langchain.chat_models import ChatVertexAI
    llm = ChatVertexAI(model="gemini-1.5-flash")
else:
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4")
```

#### 🔁 Create ACP Agent with ReAct

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    llm=llm,
    tools=[scan_for_triggers, classify_trigger_severity],
    system_prompt="""
    You are a safety-focused assistant using the ACP reasoning loop.
    For each input, scan for triggering content, assess severity, and return a clear final label.
    Follow: Thought → Action → Observation → (loop or exit)
    """
)
``` 

### 🚀 Run the Agent

```python
agent.invoke({
    "input": "The report described several cases of abuse and trauma."
})
```

Expected Output (ReAct Loop):

```text
Thought: I should scan for trigger terms.
Action: scan_for_triggers
Observation: abuse, trauma
Thought: I should classify severity.
Action: classify_trigger_severity
Observation: Moderate
Final Answer: The input contains moderate triggering content.
```

### 🧩 Optional Extensions

- 🧠 Add a reflection step using acp_comment_framework.md

- 💬 Wrap in a UI using Streamlit

- 📜 Log outputs to markdown for debugging

### 🔗 Related Modules
agent_orchestration_loop.md

[`agent_orchestration_loop.md`](agent_orchestration_loop.md)

| Module                                                                             | Purpose                                                                                 |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [`agent_orchestration_loop.md`](codebook/agents/agent_orchestration_loop.md) | Explains the ACP loop and how this agent fits into the orchestration pattern            |
| [`acp_agent_template.md`](codebook/templates/acp_agent_template.md)          | General-purpose agent scaffold used as a base for this implementation                   |
| [`acp_comment_framework.md`](codebook/templates/acp_comment_framework.md)    | Optional comment/critique layer for human-in-the-loop or reflection logic               |
| [`trigger_detector_demo.ipynb`](notebooks/trigger_detector_demo.ipynb)       | Interactive notebook version of this agent with printouts and Streamlit-ready structure |


