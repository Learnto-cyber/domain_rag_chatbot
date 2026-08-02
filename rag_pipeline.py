from retriever import Retriever
from llm import generate_answer


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()

    def ask(self, question):

        # Retrieve relevant document chunks
        retrieved_docs = self.retriever.retrieve(question, top_k=3)

        if len(retrieved_docs) == 0:
            return {
                "answer": "I couldn't find the answer in the uploaded documents.",
                "sources": []
            }

        # Build context
        context = ""

        for doc in retrieved_docs:
            context += doc["text"] + "\n\n"

        # Generate answer
        answer = generate_answer(context, question)

        return {
            "answer": answer,
            "sources": retrieved_docs
        }