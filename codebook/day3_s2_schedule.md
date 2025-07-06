

---
id: day3_session2_agents
title: Day 3 – Session 2: Agent Reasoning + LangChain Orchestration
description: Learn to structure, orchestrate, and operate intelligent agents using LangChain, reasoning loops, and modular tools
---

![fig_day3_session2_cover](../shared_assets/visuals/images/fig_day3_session2_cover.png)

# Day 3 – Session 2: Agent Reasoning + LangChain Orchestration

> _"Agents are not single prompts — they are **thinking systems**. Today we give them structure, tools, and memory."_  

---

## 🎯 Session Objectives

✅ Understand LangChain’s building blocks: tools, chains, memory, agents  
✅ Compare reasoning frameworks: ReAct vs ACP  
✅ Define tool specs and route model outputs into action  
✅ Implement LangChain orchestration patterns (codebook-ready)  
✅ Visualize agent planning and output paths  

---

## 🧠 Core Concepts

| Section | Description | Visual |
|---------|-------------|--------|
| Prompt → Chain → Agent | Layered logic: from single prompt to full agent | ![fig_prompt_chain_agent_flow](../shared_assets/visuals/fig_prompt_chain_agent_flow.png) |
| ReAct Framework | Reasoning loop: Thought → Action → Observation → Answer | ![fig_react_loop_diagram](../shared_assets/visuals/fig_react_loop_diagram.png) |
| Tool Definition | Card format: name, description, input/output schema | ![fig_tool_definition_card](../shared_assets/visuals/fig_tool_definition_card.png) |
| LangChain Orchestration | LangChain components: LLM ↔ Tool ↔ Memory ↔ Output | ![fig_langchain_orchestration_map](../shared_assets/visuals/fig_langchain_orchestration_map.png) |
| ACP Loop | Custom loop: Perceive → Reason → Act → Observe → Exit | ![fig_acp_loop_mermaid_style](../shared_assets/visuals/fig_acp_loop_mermaid_style.png) |

---

## 📘 GitBook Pages

| Page | Description | Status |
|------|-------------|--------|
| `agent_stack_basics.md` | Explains agent vs chain vs prompt logic | ✅ |
| `langchain_orchestration.md` | Architecture of LangChain and how components interact | ✅ |
| `react_vs_acp.md` | Compare reasoning loops (ReAct vs ACP) | ✅ |
| `acp_loop_explained.md` | Walkthrough of ACP with visuals + Streamlit pattern | ✅ |
| `agent_tool_registry.md` | Tool card structure + tool definition examples | ✅ |
| `llm_toggle_config.md` | Optional: Route logic to Gemini or OpenAI | ✅ |

---


## API Setup

[Gemini API Setup Guide](Gemini_API_Setup_Guide.md)
[Gemini API Setup Guide - screenshots](using_gemini_api_colab.md)

[Hugging Face API Setup Guide](huggingface_api_setup_colab.md)


[OpenAPI Setup Guide](openai_api_setup_colab.md)

---

## 🗂 Suggested Reading Flow

| Step | Page | Purpose |
|------|------|---------|
| 1️⃣ | `agent_stack_basics.md` | Prompt → Chain → Agent intro |
| 2️⃣ | `langchain_orchestration.md` | LangChain components layout |
| 3️⃣ | `react_vs_acp.md` | ReAct vs ACP loop theory |
| 4️⃣ | `acp_loop_explained.md` | ACP in LangChain logic |
| 5️⃣ | `agent_tool_registry.md` | Tool schema and IO blocks |
| 6️⃣ | `llm_toggle_config.md` | Provider toggling logic (optional) |

---

## 🧠 Use Cases in Focus

- Research agent using citation tools  
- Planning agents with decision forks  
- Retrieval-based agents with structured tool use  
- Streamlit apps that switch between Gemini/OpenAI  
- Agents embedded into document QA or policy analysis

---

## 🔮 What’s Next?

➡️ Session 3 wraps up the course by reviewing **how agents + embeddings + prompting** integrate into your custom RAG systems, Streamlit tools, or research pipelines.

➡️ [Day 3 Session 3: Agent Demos + Wrap-up →](day3_session3_demos.md)
