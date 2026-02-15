

# 📚 Milestone 1 - RAG Document Ingestion Pipeline

This project implements the first milestone of a Retrieval-Augmented Generation (RAG) system.

The system loads documents (PDF + TXT), processes them into chunks, generates embeddings using a HuggingFace model, and stores them in a persistent Chroma vector database.

---

## 🚀 Features Implemented

✅ Startup cleanup (Old Chroma DB deletion)  
✅ Automatic directory scanning (Books folder)  
✅ PDF loading using PyPDFLoader  
✅ TXT loading using TextLoader  
✅ Metadata cleaning before indexing  
✅ Recursive chunking (chunk_size=3000, overlap=200)  
✅ Local embedding generation using MiniLM  
✅ Persistent vector storage using ChromaDB  

---

## 🛠 Tech Stack

- Python 3.11
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers
- dotenv (Environment variable management)

---


## 📂 Project Structure

MILESTONE_ONE/
│
├── ingest.py
├── requirements.txt
├── Books/
│   ├── cricket.txt
│   ├── freedom_fighter_bhagat_singh.pdf
│   ├── freedom_fighter_gandhi.pdf
│   └── freedom_fighter_rani_lakshmibai.pdf
│
├── chroma_db/  (generated)
└── venv/       (ignored)

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Ingestion Pipeline

python ingest.py

Expected Output:

Old chroma_db deleted successfully!
Total documents loaded: XX
Total chunks created: XX
Vector store created successfully!


---

🧠 How It Works

1. Clears old vector database


2. Loads all supported documents from Books/


3. Cleans metadata


4. Splits documents into chunks


5. Generates embeddings using MiniLM


6. Stores embeddings in Chroma vector store




---

🎯 Milestone 1 Status

✔ Document ingestion complete
✔ Vector database creation complete
✔ Embedding pipeline complete


