import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.metadata = []

    def build_index(self, chunks):

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(texts)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.metadata = chunks

    def save(self, folder="vector_store/saved_index"):

        os.makedirs(folder, exist_ok=True)

        faiss.write_index(
            self.index,
            os.path.join(folder, "faiss.index")
        )

        with open(
            os.path.join(folder, "metadata.pkl"),
            "wb"
        ) as f:
            pickle.dump(self.metadata, f)