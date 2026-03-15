import streamlit as st

from embeddings.embedder import load_documents, generate_embeddings
from database.vector_store import VectorStore
from rag.retrieval import retrieve_context
from rag.generation import generate_answer

import os
from pathlib import Path

@st.cache_data
def load_data():
    """Load documents and build vector store once."""
    data_path = Path(__file__).parent / "data" / "documents.txt"
    if not data_path.exists():
        st.error(f"Missing: {data_path}. Create it with sample docs.")
        st.stop()
    
    docs = load_documents(str(data_path))
    vectors = generate_embeddings(docs)
    vector_db = VectorStore()
    for doc, vec in zip(docs, vectors):
        vector_db.add(doc, vec)
    return vector_db

vector_db = load_data()

st.sidebar.info("""
**Quick Setup:**
- For OpenAI GPT: `export OPENAI_API_KEY=sk-your-valid-key`
- No key? App uses **local fallback** automatically.
- Run: `streamlit run app.py`
""")

st.title("AI Knowledge Assistant")

question = st.text_input("Ask a question")

if st.button("Submit"):

    context = retrieve_context(question, vector_db)

    answer = generate_answer(context, question)

    st.write("Answer:")
    st.write(answer)
