---

---

# 🧠 Prompt vs Chain vs Agent

Understanding the difference between prompts, chains, and agents is essential when building intelligent systems with LLMs.

This page provides a clear conceptual comparison with examples and when to use each.

---

## 🔹 Prompt (One-Shot)

A **prompt** is a static instruction passed directly to a language model. It does not maintain memory, take actions, or use tools.

### Example
> _"Summarise the following article in 3 bullet points."_

- ✅ Quick
- ✅ Simple
- ❌ No context or tool use
- ❌ No planning or reasoning

---

## 🔸 Chain (Multi-Step Workflow)

A **chain** is a predefined sequence of steps, often using LangChain or manual Python logic. It connects multiple model calls or operations together.

### Example
> Clean → Embed → Search → Generate

- ✅ Deterministic
- ✅ Can mix tools + logic
- ❌ No dynamic decision-making
- ❌ Doesn’t think about *why* a step is needed

---

## 🔺 Agent (Goal-Directed, Reasoning System)

An **agent** is an LLM-powered system that can:

- Decide what to do next
- Use tools as needed
- Observe intermediate outputs
- Reason and iterate

It operates in a loop of:
> **Thought → Action → Observation → Repeat → Final Answer**

### Example
> _"Find who won last night’s game. If needed, search the web. Then tell me the stadium address."_  
The agent:
1. Thinks: “I need to look up last night’s game.”
2. Calls Google Search
3. Observes results
4. Thinks: “Now I need the stadium.”
5. Calls Places API
6. Summarizes the result

- ✅ Dynamic decision-making
- ✅ Uses external tools
- ✅ Can loop or retry
- ✅ Best for goal-directed workflows

---

## 🧭 When to Use Each

| Scenario | Use |
|---------|-----|
| One-off summary or Q&A | ✅ Prompt |
| Repeatable ETL or classification steps | ✅ Chain |
| Open-ended reasoning, goal-seeking, dynamic actions | ✅ Agent |

---

## 🛠️ Built With LangChain

- Prompts → `LLMChain`
- Chains → `SequentialChain`, `SimpleChain`, etc.
- Agents → `create_react_agent`, `initialize_agent`, `LangGraph`

---

## 🔁 Reusability

This framework applies to:
- ACSPRI course foundations
- ZaraGPT system architecture
- Client workflows using agent-based search or planning
- MVP components for reasoning + tool orchestration

