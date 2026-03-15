from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text_chunks):
    embeddings = model.encode(text_chunks)
    return embeddings

def load_documents(path):
    with open(path, "r") as f:
        data = f.read()

    paragraphs = data.split("\n\n")
    return paragraphs
