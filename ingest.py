# # STEP 1: Imports
# from langchain_community.document_loaders import (
#     DirectoryLoader,
#     PyPDFLoader,
#     TextLoader,
#     #CSVLoader,
#     #WebBaseLoader
# )


# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma

# # STEP 2: Load Documents from Folder

# # Load PDF files
# pdf_loader = DirectoryLoader(
#     path="./Books",
#     glob="**/*.pdf",
#     loader_cls=PyPDFLoader
# )

# # Load TXT files
# text_loader = DirectoryLoader(
#     path="./Books",
#     glob="**/*.txt",
#     loader_cls=TextLoader
# )

# # Load all documents
# documents = []
# documents.extend(pdf_loader.load())
# documents.extend(text_loader.load())

# print(f"Total documents loaded: {len(documents)}")

# # STEP 3: Split Documents into Chunks

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )

# split_docs = text_splitter.split_documents(documents)

# print(f"Total chunks created: {len(split_docs)}")

# # STEP 4: Create Embeddings

# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )




# # STEP 5: Store in Vector Database (Chroma)

# vector_store = Chroma.from_documents(
#     documents=split_docs,
#     embedding=embedding_model,
#     persist_directory="./chroma_db",
#     collection_name="fresh_session"
# )

# print("Vector store created successfully!")

# STEP 1: Imports
import os
import shutil

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# STEP 2: Startup Cleanup (Clear old DB)
if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")
    print("Old chroma_db deleted successfully!")


# STEP 3: Load Documents from Folder

# Load PDF files
pdf_loader = DirectoryLoader(
    path="./Books",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

# Load TXT files
text_loader = DirectoryLoader(
    path="./Books",
    glob="**/*.txt",
    loader_cls=TextLoader
)

# Load all documents
documents = []
documents.extend(pdf_loader.load())
documents.extend(text_loader.load())

print(f"Total documents loaded: {len(documents)}")


# STEP 4: Metadata Cleaning
for doc in documents:
    doc.metadata = {
        key: value
        for key, value in doc.metadata.items()
        if isinstance(value, (str, int, float))
    }


# STEP 5: Split Documents into Chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,   # Updated as per milestone
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(split_docs)}")


# STEP 6: Create Embeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# STEP 7: Store in Vector Database (Chroma)

vector_store = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    persist_directory="./chroma_db",
    collection_name="milestone_one_collection"
)

print("Vector store created successfully!")