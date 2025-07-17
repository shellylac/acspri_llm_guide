---

---

# 🤖 LangChain ReAct Agent: Gemini + OpenAI Version

This module defines a reusable LangChain ReAct agent capable of reasoning step-by-step and using external tools. The agent can be powered by either **Gemini** (default) or **OpenAI**.

---

## 🔧 Setup: Choose LLM Provider

```python
# Set this flag to switch between Gemini and OpenAI
USE_GEMINI = True
```

```python
if USE_GEMINI:
    from langchain.chat_models import ChatVertexAI
    llm = ChatVertexAI(model="gemini-1.5-flash")
else:
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4", temperature=0)
```

---

## 🛠️ Tool Definitions

```python
from langchain.tools import tool
from langchain.utilities import SerpAPIWrapper, GooglePlacesAPIWrapper

@tool
def search(query: str) -> str:
    """Search the web for real-time information."""
    return SerpAPIWrapper().run(query)

@tool
def places(query: str) -> str:
    """Look up places and addresses."""
    return GooglePlacesAPIWrapper().run(query)
```

These tools will be passed to the agent at creation.

---

## ⚙️ Create the Agent

```python
from langgraph.prebuilt import create_react_agent

tools = [search, places]

agent = create_react_agent(
    llm = llm,
    tools = tools,
    verbose = True
)
```

This uses LangChain's built-in ReAct orchestration. It will:
- Decide which tool to use
- Pass inputs
- Observe outputs
- Repeat until confident enough to return an answer

---

## ▶️ Run the Agent

```python
response = agent.invoke({
    "input": "Who did the Texas Longhorns play last week, and what is the address of the opposing stadium?"
})
print(response["output"])
```

---

## 📎 Notes

- **Tool descriptions are critical** for good agent behavior.
- Make sure your API keys are configured for SerpAPI and Google Places.
- You can extend this agent with additional tools, memory, or a Streamlit interface.

---

## 🔁 Reusability

This logic is reusable across:
- ACSPRI live demos
- GitBook tutorials
- Streamlit UI (e.g., `day3_rag_streamlit.py`)
- Your MVPs (ZaraGPT, Trigger Detector, Gemini Planner)

For reference: see `day3_agents.md`, `llm_thought_action_observe.md`, and `tool_definition_schema.md`.
