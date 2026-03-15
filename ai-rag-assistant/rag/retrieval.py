from embeddings.embedder import generate_embeddings

def retrieve_context(query, vector_store):

    query_embedding = generate_embeddings([query])[0]

    results = vector_store.search(query_embedding)

    context = "\n".join(results)

    return context
