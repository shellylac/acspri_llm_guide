
import streamlit as st
import os
import google.generativeai as genai
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# --- Setup ---
st.title("🔍 Fashion AI RAG with Gemini (Citations Enabled)")
st.markdown("Ask questions grounded in your embedded PDF collection. Responses will include citation markers.")

# --- API Key Input ---
google_api_key = st.text_input("Enter your Google Gemini API Key", type="password")
if google_api_key:
    os.environ['GOOGLE_API_KEY'] = google_api_key
    genai.configure(api_key=google_api_key)

# --- Load Chroma DB ---
@st.cache_resource
def load_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
    return db

db = load_vectorstore()

# --- User Query ---
query = st.text_input("🔎 Ask your fashion research question:")
if query:
    with st.spinner("Retrieving relevant documents..."):
        results = db.similarity_search(query, k=3)

    retrieved_chunks = []
    for i, doc in enumerate(results):
        marker = f"[source_{i+1}]"
        text = doc.page_content.strip() + f"\n\n{marker}"
        retrieved_chunks.append(text)

    referenced_text = "\n\n".join(retrieved_chunks)

    # --- Gemini Generation ---
    prompt = f"""Answer the following question using the content below.
Include [source_n] markers to show where each fact comes from.

{referenced_text}

Question: {query}
"""

    if 'GOOGLE_API_KEY' in os.environ:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        st.markdown("## 📘 Gemini Response")
        st.write(response.text)
    else:
        st.warning("Please enter a valid Gemini API key.")
