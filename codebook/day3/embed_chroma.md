---

---

## Step 1: Load your documents

```python
from langchain.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader("./data/", glob="**/*.txt", loader_cls=TextLoader)
docs = loader.load()
```

## Step 2: Chunk the documents

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
```

## Step 3: Embed and store in Chroma

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db")
db.persist()
```

## Notes

- Assumes `.txt` input files in `./data/`
- For PDFs, use `PDFLoader` or `PyMuPDFLoader`
- Output is a persistent local vector store you can reuse for retrieval tasks
