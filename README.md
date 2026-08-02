# 📚 Domain Specific RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** based chatbot that allows users to upload PDF documents and ask questions based only on the uploaded documents. The chatbot extracts text from PDFs, creates semantic embeddings, stores them in a FAISS vector database, retrieves relevant information, and generates answers using the **Groq Llama 3.3 70B** Large Language Model.

---

## 🚀 Features

- 📄 Upload one or more PDF documents
- 📖 Extract text from PDF files
- ✂️ Automatic text chunking
- 🧠 Semantic embeddings using Sentence Transformers
- 🔍 Fast document retrieval using FAISS
- 🤖 Answer generation using Groq LLM
- 📑 Displays source document and page number
- 💬 Session-based chat history
- 🎨 Interactive Streamlit interface

---

## 🛠 Technologies Used

- Python 3.11
- Streamlit
- PyPDF
- Sentence Transformers
- PyTorch
- FAISS
- LangChain Text Splitters
- Groq API
- python-dotenv

---

## 📂 Project Structure

```text
domain_rag_chatbot/
│
├── app.py
├── config.py
├── document_loader.py
├── chunker.py
├── vector_store.py
├── retriever.py
├── rag_pipeline.py
├── llm.py
├── prompt.py
├── requirements.txt
├── README.md
├── .env
│
├── documents/
├── extracted_text/
├── vector_store/
└── screenshots/
```

---

# ⚙️ Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/domain_rag_chatbot.git
cd domain_rag_chatbot
```

Replace `<your-username>` with your GitHub username.

---

## Step 2: Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Step 4: Install PyTorch

Install PyTorch before installing the project requirements.

```bash
pip install torch torchvision torchaudio
```

---

## Step 5: Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Create a `.env` File

Create a file named `.env` in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# ▶️ Running the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

If it does not open automatically, visit:

```
http://localhost:8501
```

---

# 📖 How to Use

### 1. Start the application

```bash
streamlit run app.py
```

---

### 2. Upload PDF Documents

Click **Upload PDF Files** and select one or more PDF documents.

Example:

- DBMS_notes.pdf
- Python_notes.pdf

---

### 3. Process the Documents

Click **Process Documents**.

The application will:

- Extract text from PDF pages
- Split text into chunks
- Generate embeddings
- Build the FAISS vector database

---

### 4. Ask Questions

Enter a question in the input box.

Example questions:

```
What is DBMS?
```

```
Explain SQL.
```

```
What are the advantages of Python?
```

```
Explain inheritance.
```

---

### 5. View the Results

The chatbot displays:

- Generated Answer
- Source Document
- Page Number
- Chat History

---

# 🔄 Workflow

```text
                User
                  │
                  ▼
          Upload PDF Files
                  │
                  ▼
         PDF Text Extraction
                  │
                  ▼
           Text Chunking
                  │
                  ▼
 Sentence Transformer Embeddings
                  │
                  ▼
       FAISS Vector Database
                  │
                  ▼
         User Asks Question
                  │
                  ▼
      Semantic Similarity Search
                  │
                  ▼
       Retrieve Relevant Chunks
                  │
                  ▼
        Groq Llama 3.3 70B
                  │
                  ▼
         Generate Final Answer
                  │
                  ▼
    Source References + Chat History
```

---

# 📝 Example Questions

- What is DBMS?
- Explain SQL.
- What are the advantages of DBMS?
- What is Python?
- Explain Object-Oriented Programming.
- What are Python keywords?
- Explain inheritance.
- Explain encapsulation.
- Explain polymorphism.
- What is normalization?

---

# 📁 Sample Documents

Upload PDF files directly through the application or place them inside the `documents/` folder.

Example:

- DBMS_notes.pdf
- Python_notes.pdf

---

# 📦 Requirements

- Python 3.11+
- Streamlit
- PyTorch
- Sentence Transformers
- FAISS
- PyPDF
- LangChain Text Splitters
- Groq API Key
- python-dotenv

---

# ✅ Testing

The application has been tested for:

- PDF Upload
- Multiple PDF Upload
- Text Extraction
- Text Chunking
- Vector Database Creation
- Semantic Retrieval
- Question Answering
- Source References
- Chat History
- Invalid Question Handling

---

# 🚀 Future Enhancements

- OCR support for scanned PDFs
- DOCX and TXT support
- Persistent chat history
- User authentication
- Cloud deployment
- Multi-language support

---

# 👨‍💻 Author

**Drisha D Padival**

Computer Science and Engineering

---

# 📄 License

This project is developed for educational and academic purposes.
