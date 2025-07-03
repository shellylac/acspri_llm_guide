# ⚙️ Setup Instructions
This notebook uses the following tools and APIs for document retrieval and LLM-based generation:

## 🔧 Libraries Required:
- `langchain`
- `chromadb`
- `pypdf` (for PDF parsing)
- `sentence-transformers` (embedding model)
- `google-generativeai` (for Gemini API)
- `openai` (for OpenAI GPT models)

Install them using the following cells where necessary.

## 🔐 API Keys Required:
- **Google Gemini API key** (set to `os.environ['GOOGLE_API_KEY']`)
- **OpenAI API key** (set to `openai.api_key`)

You can obtain keys from:
- Google Gemini: https://makersuite.google.com/app/apikey
- OpenAI: https://platform.openai.com/account/api-keys

Make sure to paste your keys in the designated code cells.
# 📘 Day 3 RAG Colab Notebook
This notebook demonstrates a complete Retrieval-Augmented Generation (RAG) workflow:
- Load PDFs from a folder
- Chunk and embed with SentenceTransformers
- Store in ChromaDB
- Run semantic search

# 🟩 Install dependencies
!pip install -q langchain chromadb pypdf sentence-transformers
# 🟨 Load PDFs from folder
from langchain.document_loaders import PyPDFLoader
from pathlib import Path

pdf_dir = Path("./pdfs")  # <-- Replace with your folder path
all_docs = []

for pdf_path in pdf_dir.glob("*.pdf"):
    loader = PyPDFLoader(str(pdf_path))
    docs = loader.load()
    all_docs.extend(docs)

print(f"Loaded {len(all_docs)} pages from {len(list(pdf_dir.glob('*.pdf')))} PDF files.")
# 🟧 Split documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)
print(f"Generated {len(chunks)} text chunks.")
# 🟥 Embed chunks and store in ChromaDB
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db")
db.persist()
print("Embeddings saved to ChromaDB.")
# 🔍 Run semantic search
query = "What are the findings about youth crime prevention?"
results = db.similarity_search(query, k=3)

for i, res in enumerate(results):
    print(f"--- Result {i+1} ---\n{res.page_content[:500]}\n")
## 🧠 Generate Answer with Gemini
Use Gemini model to answer a query based on the retrieved documents.
# ⚙️ Install Google Generative AI SDK if not already installed
!pip install -q google-generativeai
# 🔑 Setup Gemini API key
import os
os.environ['GOOGLE_API_KEY'] = "your-api-key-here"  # Replace with your actual key
# 📡 Generate response from Gemini using retrieved content
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

retrieved_text = "\n\n".join([doc.page_content for doc in results])
prompt = f"Answer the following question based on the retrieved content:\n\n{retrieved_text}\n\nQuestion: {query}"

response = model.generate_content(prompt)
print(response.text)
## 📎 Gemini Output: Without vs With Citations
This section demonstrates how to:
- Generate a plain Gemini response (no source info)
- Generate a response **with inline source references** using metadata from the retrieved chunks
# ➖ Gemini Response WITHOUT Source Info
plain_prompt = f"Answer the question based on the following content:\n\n{retrieved_text}\n\nQuestion: {query}"
response_plain = model.generate_content(plain_prompt)
print(response_plain.text)
# ➕ Gemini Response WITH Source References
# Append [source_n] markers using doc.metadata
retrieved_with_refs = []
for i, doc in enumerate(results):
    marker = f"[source_{i+1}]"
    content_with_marker = doc.page_content.strip() + f"\n\n{marker}"
    retrieved_with_refs.append(content_with_marker)

referenced_text = "\n\n".join(retrieved_with_refs)
citation_prompt = f"Answer the question using the content below. Include [source_n] in your answer to show where facts came from.\n\n{referenced_text}\n\nQuestion: {query}"
response_cited = model.generate_content(citation_prompt)
print(response_cited.text)
## 🤖 OpenAI Output: With vs Without Citations
Now let's demonstrate the same generation using OpenAI's GPT model instead of Gemini.
# 🟦 Install OpenAI SDK if not installed
!pip install -q openai
# 🔑 Setup OpenAI API key
import openai
openai.api_key = "your-openai-api-key-here"  # Replace with your OpenAI key
# ➖ OpenAI Response WITHOUT Source Info
openai_prompt = f"Answer the question based on the following content:\n\n{retrieved_text}\n\nQuestion: {query}"
completion_plain = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": openai_prompt}]
)
print(completion_plain['choices'][0]['message']['content'])
# ➕ OpenAI Response WITH Source References
referenced_text_openai = referenced_text  # reusing same `[source_n]` markers
openai_prompt_cited = f"Answer the question using the content below. Include [source_n] in your answer to show where facts came from.\n\n{referenced_text_openai}\n\nQuestion: {query}"
completion_cited = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": openai_prompt_cited}]
)
print(completion_cited['choices'][0]['message']['content'])