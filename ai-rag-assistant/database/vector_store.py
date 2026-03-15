import numpy as np

class VectorStore:

    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text, vector):
        self.texts.append(text)
        self.vectors.append(vector)

    def search(self, query_vector, top_k=3):
        similarities = []

        for vec in self.vectors:
            sim = np.dot(query_vector, vec) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vec)
            )
            similarities.append(sim)

        top_indices = np.argsort(similarities)[-top_k:][::-1]

        results = [self.texts[i] for i in top_indices]

        return results
