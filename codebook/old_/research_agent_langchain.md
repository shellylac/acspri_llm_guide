# 🧠 Build a Research Agent with LangChain, Wikipedia, and SerpAPI

This in-depth tutorial explains what an **agent** is, how it differs from simple **tool calling**, and shows you how to build your own **multi-tool research agent** using LangChain, Wikipedia, and SerpAPI.

---

## 🤖 What Is an Agent?

An **agent** is an intelligent system that can:
- **Observe** the world (via user inputs or tools like search),
- **Reason** about tasks,
- **Act** by calling tools like APIs,
- **Iterate** and refine answers until a goal is achieved.

**Agents are not static.** They perform **multi-step decision making** to achieve goals, using tools and logic to guide their process. A popular agent design pattern is **ReAct** (Reason + Act).

---

## 🔧 What Is Tool Calling?

**Tool calling** is when an LLM (like GPT-4 or Gemini) invokes a specific function or API in response to a prompt. It’s **single-step**:  
“Need external info → Call tool → Done.”

Tool calling is perfect for:
- Pulling weather data
- Executing a Python function
- Performing one-shot search

But it lacks planning, memory, or iteration.

---

## 🔍 Tool Calling vs. Agent Systems

| Feature                  | Tool Calling              | Agent System                  |
|--------------------------|---------------------------|-------------------------------|
| Calls external tools     | ✅                         | ✅                             |
| Decision-making loop     | ❌                         | ✅                             |
| Tool selection logic     | ❌                         | ✅ (via orchestration layer)   |
| Handles multiple steps   | ❌                         | ✅                             |
| Uses memory              | ❌                         | ✅                             |
| Example                  | GPT function call          | LangChain ReAct agent         |

---

## 🧰 Tools for a Research Agent

We’ll integrate:

- `WikipediaTool` → summary from Wikipedia
- `SerpAPI` → Google-like real-time search

**Other optional tools**:
- PDF summarization
- Chroma (vector DB)
- Email/Calendar
- PythonREPLTool

---

## ✅ Setup: Dependencies

```bash
pip install langchain langchain-community wikipedia
```

Set your API key:

```python
import os
os.environ["SERPAPI_API_KEY"] = "your_serpapi_key"
```

---

## 🧪 Define the Tools

```python
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import tool
import wikipedia

@tool
def search_web(query: str) -> str:
    "Use the SerpAPI to run a Google Search."
    search = SerpAPIWrapper()
    return search.run(query)

@tool
def wiki_lookup(query: str) -> str:
    "Search Wikipedia for information."
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found: {e.options[:3]}"
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## 🧠 Initialize the Agent

```python
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4")
tools = [search_web, wiki_lookup]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",  # ReAct agent
    verbose=True
)
```

---

## 💬 Ask a Research Question

```python
response = agent.run(
    "What is the latest research on urban loneliness? Summarize key insights from Wikipedia and the web."
)
print(response)
```

The agent will:
1. Reason through the question
2. Decide which tool(s) to call
3. Act via tool invocation
4. Use tool outputs to finalize its response

---

## 🔄 What’s Happening Under the Hood

This is a **ReAct agent loop**:
```
Thought → Action → Action Input → Observation → Repeat → Final Answer
```

LangChain orchestrates the tool invocation loop automatically.

---

## 🧩 Extend with Custom Tools (PDF Summarizer Example)

```python
@tool
def summarize_pdf(file_path: str) -> str:
    from PyPDF2 import PdfReader
    reader = PdfReader(file_path)
    text = " ".join(page.extract_text() for page in reader.pages)
    return text[:1500]
```

Add it to the agent’s tool list to allow PDF analysis.

---

## 🔁 Recap: When to Use What?

Use **tool calling** when:
- You need a one-off function call
- No memory, iteration, or decision logic needed

Use an **agent** when:
- Multiple tools involved
- The question needs planning
- You want memory, retries, or intermediate reasoning

---

## 🧱 Maria Aise Modular Architecture Alignment

This notebook fits into the `codebook/agents/` module:

- Save this file as `research_agent_langchain.md`
- Tag with YAML frontmatter
- Add to `codebook_index.yaml`

It becomes:
- ✅ A teaching asset for ACSPRI
- ✅ A module for ZaraGPT
- ✅ A monetizable GitBook export

---

## ✅ Next Steps

- Add memory with `ConversationBufferMemory`
- Visualize the ReAct steps
- Wrap in Streamlit for UI
- Connect to PDF uploads or Notion

Let me know if you want this as `.ipynb`, `.md`, or synced to GitBook directly.