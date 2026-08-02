import pickle
import faiss
from sentence_transformers import SentenceTransformer


class Retriever:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.index = faiss.read_index(
            "vector_store/saved_index/faiss.index"
        )

        with open(
            "vector_store/saved_index/metadata.pkl",
            "rb"
        ) as f:
            self.metadata = pickle.load(f)

    def retrieve(self, question, top_k=3):

        embedding = self.model.encode([question])

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results