---

---

# 🧠 ACP Agent Template

This is a **template scaffold** for building reasoning agents using the **Agent Cognition Protocol (ACP)** and LangChain’s ReAct framework.

Use it as:
- A rapid starting point for building custom agents  
- A reusable structure for Streamlit/Colab demos or MVPs  
- A clean logic contract for research or consulting tools  

---

## ✳️ What Is ACP?

ACP (Agent Cognition Protocol) models how a cognitive agent thinks and acts:

1. **Perceive** → receive the input  
2. **Reason** → plan the next step  
3. **Act** → invoke a tool or decision path  
4. **Observe** → interpret the result  
5. **Repeat or Exit** → keep going or stop

This protocol helps you trace agent behavior and reduce hallucinations — especially important in research or enterprise applications.

---

### 🧱 Agent Metadata (Human-Readable Block)

Start your template with a high-level description. This isn’t code — it’s clarity for you and collaborators.

```python
"""
Agent Name: ZaraGPT
Purpose: Classify and summarize fashion PR across media
LLM: Gemini or OpenAI
Tools: SearchTool, StanceClassifier, SummarizeTool
ACP Loop: Perceive → Reason → Act → Observe → Repeat/Exit
Prompting: Uses ReAct loop inside ACP structure
"""
This keeps the agent logic transparent and modular. Always describe:

What it does

Which model it uses

Which tools are invoked

How decisions are made

### 🧰 Tool Setup

Tools are how your agent reaches into the world — search, classify, calculate, etc.

```python

from langchain_core.tools import tool

@tool
def search(query: str) -> str:
    """Search the web for recent updates related to a brand or topic."""
    return my_search_wrapper(query)

@tool
def classify(text: str) -> str:
    """Return sentiment or stance as pro / neutral / against."""
    return stance_model.predict(text)

 ```   
### ✅ Rules of Thumb:

- Clear function name

- Helpful docstring (used by LLM to decide when to call)

- Narrow, single-purpose logic per tool

### 🔧 LLM Setup and Switch
You can swap providers (Gemini/OpenAI) by toggling:

```python

USE_GEMINI = True

if USE_GEMINI:
    from langchain.chat_models import ChatVertexAI
    llm = ChatVertexAI(model="gemini-1.5-flash")
else:
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4")
🧠 Create ACP Agent Using ReAct
```
Use LangChain’s create_react_agent to define reasoning behavior.

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    llm=llm,
    tools=[search, classify],
    system_prompt="""
    You are a research assistant. Use the ACP pattern:
    Perceive input, Reason next step, Act via tools, Observe results.
    Loop until confident in the final answer.
    """
)
```

This creates an intelligent agent that logs Thought → Action → Observation on every turn.

### 🚀 Run an Agent Query

```python
agent.invoke({
    "input": "What are the public reactions to Zara’s latest campaign?"
})
```

LangChain will:

- Track every tool call

- Print thoughts and results step-by-step

- Automatically exit when the model is confident

### 🧪 Output Sample
```vbnet
Thought: I should look up reactions online.
Action: search
Observation: Found 3 articles mentioning mixed reviews.
Thought: I should classify the sentiment.
Action: classify
Observation: Neutral leaning negative
Final Answer: Public sentiment is mixed to negative based on recent reports.
```

### 🔁 How This Fits ACP
| ACP Step    | In Your Code                             |
| ----------- | ---------------------------------------- |
| Perceive    | `input` passed to `.invoke()`            |
| Reason      | Generated `Thought`                      |
| Act         | Model chooses a `tool`                   |
| Observe     | Result captured and displayed            |
| Repeat/Exit | Loop continues or returns `Final Answer` |


🧱 Optional: ACP YAML Metadata (for indexing)
``` yaml

# agent_zaragpt.yaml
agent_name: ZaraGPT
status: prototype
llm: gemini-1.5-flash
tools:
  - name: search
    purpose: news retrieval
  - name: classify
    purpose: sentiment stance classification
loop: ACP
framework: ReAct
```

### 🔗 Related Modules
| Module                                                                             | Description                          |
| ---------------------------------------------------------------------------------- | ------------------------------------ |
| [`agent_orchestration_loop.md`](../../codebook/agents/agent_orchestration_loop.md) | Describes how this loop works        |
| [`trigger_agent_lite.md`](../../codebook/agents/trigger_agent_lite.md)             | Lightweight version built using this |
| [`acp_comment_framework.md`](../../codebook/templates/acp_comment_framework.md)    | Add human-in-the-loop feedback       |
