from sentence_transformers import SentenceTransformer
from rag.vector_store import create_collection, add_documents, search

model = SentenceTransformer("all-MiniLM-L6-v2")

def index_documents(chunks):
    """
    Index documents: create collection and add embeddings.
    """
    create_collection()
    embeddings = model.encode(chunks)
    add_documents(chunks, embeddings)



def retrieve_context(query):

    query_embedding = model.encode(query)

    results = search(query_embedding)

    return "\n".join(results)
