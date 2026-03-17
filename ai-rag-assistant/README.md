# AI Document Assistant using RAG + Endee Vector Database

## Overview

This project implements a Retrieval-Augmented Generation (RAG) based AI assistant that answers user questions based on provided documents.

The system combines semantic search using a vector database with a language model to generate context-aware responses.

The core vector search functionality is powered by the Endee Vector Database, which enables efficient similarity search over document embeddings.

The application allows users to upload documents, index them into the vector database, and ask natural language questions about the content.

---

## Problem Statement

Traditional LLMs answer questions using general knowledge but cannot reliably answer questions about specific private documents.

This project solves that problem using Retrieval-Augmented Generation (RAG), where relevant information is retrieved from documents first and then passed to the LLM to generate grounded answers.

This enables accurate question answering over custom datasets.

---

## Key Features

• Document ingestion and chunking  
• Semantic embeddings using SentenceTransformers  
• High-performance vector search using Endee  
• Retrieval-Augmented Generation (RAG) pipeline  
• Interactive user interface built with Streamlit  
• Local fallback mode when API is unavailable  

---

## System Architecture

User Query  
↓  
Embedding Model (SentenceTransformers)  
↓  
Vector Search (Endee Vector Database)  
↓  
Top-K Document Retrieval  
↓  
Context Injection into LLM  
↓  
Answer Generation  

---

## Technology Stack

Python

Streamlit — Web interface

SentenceTransformers — Embedding model

Endee — Vector database for semantic search

OpenAI GPT (optional) — LLM for answer generation

---

## Project Structure

```
ai-rag-assistant
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── rag
│   ├── __init__.py
│   ├── retrieval.py
│   ├── generation.py
│   ├── vector_store.py
│   └── document_loader.py
│
├── embeddings
│   └── embedder.py
│
├── data
│   └── sample_documents.txt
│
└── assets
    └── architecture.png
```

---

## How the System Works

### 1. Document Processing

Input documents are split into smaller chunks to improve retrieval accuracy and semantic search performance.

### 2. Embedding Generation

Each document chunk is converted into a vector embedding using the SentenceTransformers model.

These embeddings capture the semantic meaning of the text.

### 3. Vector Storage

The embeddings are stored in the Endee Vector Database along with metadata containing the original document text.

This allows efficient similarity-based search over large document collections.

### 4. Query Processing

When a user submits a question:

1. The question is converted into an embedding vector
2. The vector database searches for the most similar document chunks
3. The top relevant results are retrieved

### 5. Answer Generation

The retrieved document chunks are passed as context to a language model, which generates an answer grounded in the document information.

This ensures responses are based on the uploaded data rather than general knowledge.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/ai-rag-assistant.git
cd ai-rag-assistant
```

### 2. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

If the API key is not provided, the application will run in local fallback mode.

### 5. Run the Application

```
streamlit run app.py
```

After running the command, open the browser and navigate to the local Streamlit URL to interact with the application.

---

## Example Queries

• What is reinforcement learning?  
• Explain deep learning  
• What is machine learning used for?  
• Describe neural networks  

---

## Example Use Cases

• AI-powered document assistants  
• Enterprise knowledge search systems  
• Customer support knowledge bases  
• Research paper question answering  
• Internal company documentation search  

---

## Future Improvements

• Multi-document upload support  
• Hybrid keyword + semantic search  
• Support for multiple embedding models  
• Persistent vector database storage  
• Deployment as a scalable API service  
• Integration with agent-based workflows  

---

## Conclusion

This project demonstrates how modern AI applications combine vector databases with large language models to enable accurate document-based question answering.

By integrating semantic search through the Endee Vector Database with Retrieval-Augmented Generation, the system can efficiently retrieve relevant information and generate context-aware responses.

This architecture reflects the design patterns used in many real-world AI systems such as knowledge assistants, enterprise search platforms, and intelligent document processing solutions.
