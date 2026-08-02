class TextChunker:

    def __init__(self, chunk_size=800, overlap=100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def create_chunks(self, documents):

        chunks = []

        for doc in documents:

            text = doc["text"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk = text[start:end]

                chunks.append({
                    "text": chunk,
                    "document": doc["document"],
                    "page": doc["page"]
                })

                start += self.chunk_size - self.overlap

        return chunks