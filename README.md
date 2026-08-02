# 📚 Domain Specific RAG Chatbot

A Domain-Specific Retrieval-Augmented Generation (RAG) Chatbot that allows users to upload PDF documents and ask questions based on their content. The application extracts text from PDFs, creates vector embeddings using Sentence Transformers, stores them in a FAISS vector database, retrieves relevant information, and generates accurate answers using the Groq LLM.

---

## 🚀 Features

- Upload one or more PDF documents
- Extract text from PDF pages
- Split text into semantic chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Retrieve the most relevant document chunks
- Generate answers using the Groq LLM
- Display source document names and page numbers
- User-friendly Streamlit interface

---

## 🛠 Technologies Used

- Python 3.11+
- Streamlit
- PyPDF
- Sentence Transformers
- FAISS
- LangChain Text Splitters
- Groq API (Llama 3.3)
- Python Dotenv

---

## 📂 Project Structure

```
domain_rag_chatbot/
│
├── app.py
├── config.py
├── document_loader.py
├── chunker.py
├── vector_store.py
├── retriever.py
├── llm.py
├── prompt.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
│
├── documents/
├── extracted_text/
├── vector_store/
│   └── saved_index/
│
└── .env
```

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd domain_rag_chatbot
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a .env File

Create a file named

```
.env
```

Add your Groq API key.

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# 📖 How to Use

### Step 1

Launch the application using

```bash
streamlit run app.py
```

---

### Step 2

Upload one or more PDF files using the **Upload PDF Files** button.

---

### Step 3

Click **Process Documents**.

The application will:

- Extract text
- Split text into chunks
- Generate embeddings
- Build the FAISS vector database

---

### Step 4

Enter a question in the input box.

Example:

```
What is machine learning?
```

---

### Step 5

Click **Ask**.

The chatbot will:

- Search the vector database
- Retrieve relevant document chunks
- Send the retrieved context to the Groq LLM
- Display the generated answer

---

### Step 6

Review the answer and the source document/page references displayed below it.

---

# 🔄 Workflow

```
PDF Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Groq LLM
      │
      ▼
Generated Answer
```

---

# 📦 Required Packages

```
streamlit
pypdf
faiss-cpu
sentence-transformers
langchain-text-splitters
groq
python-dotenv
numpy
pandas
```

---

# 🧪 Example Questions

- What is Artificial Intelligence?
- Explain Neural Networks.
- What are the applications of Machine Learning?
- Define Data Mining.
- Explain Cloud Computing.

---


# 👨‍💻 Author

**Drisha D Padival**

---

# 📄 License

This project is developed for educational and academic purposes.
