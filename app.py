import json
import streamlit as st
# Chat history
if "history" not in st.session_state:
    st.session_state.history = []
from config import DOCUMENTS_DIR
from document_loader import PDFLoader
from chunker import TextChunker
from vector_store import VectorStore
from retriever import Retriever
from llm import generate_answer
from rag_pipeline import RAGPipeline

rag = RAGPipeline()
st.set_page_config(
    page_title="Domain Specific RAG Chatbot",
    page_icon="📚",
    layout="wide"
)
# Sidebar
with st.sidebar:
    st.title("📚 Domain RAG Chatbot")
    st.markdown("---")

    st.write("### Features")
    st.write("✅ PDF Upload")
    st.write("✅ Semantic Search")
    st.write("✅ Groq LLM")
    st.write("✅ Source References")

    st.markdown("---")
    st.info("Upload PDFs and ask questions.")
    if st.button("🗑 Clear Chat"):
        st.session_state.history = []
        st.rerun()
st.title("📚 Domain Specific RAG Chatbot")

st.write("Upload one or more PDF files and click **Process Documents**.")

# -----------------------
# Upload PDFs
# -----------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for pdf in uploaded_files:

        save_path = DOCUMENTS_DIR / pdf.name

        with open(save_path, "wb") as f:
            f.write(pdf.getbuffer())

    st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully.")

# -----------------------
# Process PDFs
# -----------------------

if st.button("Process Documents"):

    loader = PDFLoader()

    documents = loader.load_all_documents(DOCUMENTS_DIR)

    st.write("Documents Extracted:")
    st.write(documents)

    st.metric("Pages Extracted", len(documents))

    if len(documents) == 0:

        st.error("No text could be extracted from the uploaded PDFs.")

    else:

        st.success(f"{len(documents)} pages extracted successfully.")

        loader = PDFLoader()

        documents = loader.load_all_documents(DOCUMENTS_DIR)
        chunker = TextChunker()

        chunks = chunker.create_chunks(documents)

        st.success(f"{len(chunks)} chunks created.")

        vector_db = VectorStore()

        vector_db.build_index(chunks)

        vector_db.save()

        st.success("Vector database created successfully.")

        for page in documents:

            st.markdown("---")

            st.subheader(page["document"])

            st.write(f"**Page:** {page['page']}")

            st.write(page["text"][:1000])

        with open("extracted_text/pages.json", "w", encoding="utf-8") as f:
            json.dump(documents, f, indent=4, ensure_ascii=False)

        st.success("Metadata saved successfully!")
st.divider()
st.header("💬 Ask Questions")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching documents..."):
            try:
                result = rag.ask(question)
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()

        st.session_state.history.append(
            {
                "question": question,
                "answer": result["answer"],
                "sources": result["sources"]
            }
        )
        st.success("Answer Generated")

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("📄 Source Documents")

        for doc in result["sources"]:
            st.info(f"{doc['document']} | Page {doc['page']}")
if st.session_state.history:

    st.markdown("---")
    st.subheader("📝 Chat History")

    for chat in reversed(st.session_state.history):

        st.markdown(f"**🙋 Question:** {chat['question']}")
        st.write(chat["answer"])
        st.markdown("---")
st.caption("Developed using Streamlit • FAISS • Sentence Transformers • Groq")
