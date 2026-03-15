import streamlit as st

from embeddings.embedder import load_documents
from rag.retrieval import index_documents, retrieve_context
from rag.generation import generate_answer


import os
from pathlib import Path

@st.cache_data
def load_data():
    """Load documents and index to Endee once."""
    data_path = Path(__file__).parent / "data" / "documents.txt"
    if not data_path.exists():
        st.error(f"Missing: {data_path}. Create it with sample docs.")
        st.stop()
    
    docs = load_documents(str(data_path))
    index_documents(docs)
    return True

load_data()


st.sidebar.info("""
**Quick Setup:**
1. Start Endee: `docker compose up -d`
2. For OpenAI GPT: `export OPENAI_API_KEY=sk-your-valid-key`
3. Run: `cd ai-rag-assistant && streamlit run app.py`
""")


st.title("AI Knowledge Assistant")

question = st.text_input("Ask a question")

if st.button("Submit"):

    context = retrieve_context(question)


    answer = generate_answer(context, question)

    st.write("Answer:")
    st.write(answer)
