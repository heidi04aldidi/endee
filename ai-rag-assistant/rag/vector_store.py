from endee_client import Client
from endee_client import EndeeError

# Initialize Endee vector database
db = Client()

COLLECTION_NAME = "documents"



def create_collection():
    """
    Creates a vector collection if it doesn't exist
    """
    try:
        if COLLECTION_NAME not in db.list_collections():
            db.create_collection(
                name=COLLECTION_NAME,
                dimension=384  # embedding size
            )
    except EndeeError as e:
        print(f"Warning: Could not create collection (server may not be running): {e}")



def add_documents(chunks, embeddings):
    """
    Store document chunks and embeddings in Endee
    """

    vectors = []

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        vectors.append({
            "id": str(i),
            "vector": emb.tolist(),
            "metadata": {"text": chunk}
        })

    try:
        db.insert(
            collection_name=COLLECTION_NAME,
            vectors=vectors
        )
    except EndeeError as e:
        print(f"Error inserting to Endee: {e}")



def search(query_embedding, k=3):
    """
    Search for similar document chunks
    """

    try:
        results = db.search(
            collection_name=COLLECTION_NAME,
            vector=query_embedding.tolist(),
            top_k=k
        )

        texts = [r["metadata"]["text"] for r in results if "metadata" in r and "text" in r["metadata"]]

        return texts
    except EndeeError as e:
        print(f"Error searching Endee (check if server running): {e}")
        return []

