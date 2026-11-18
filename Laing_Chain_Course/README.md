# LangChain Course & Hands-on Practice

This directory contains introductory experiments, notebooks, and reference materials for learning [LangChain](https://www.langchain.com/) and integrating Large Language Models (LLMs) via [Groq](https://groq.com/).

---

## 📂 Directory Structure

```text
Laing_Chain_Course/
├── basic_lang_chain.ipynb   # Hands-on notebook covering Groq & LangChain basics
├── notes.txt               # Notes on Python virtual environment setup & commands
├── requirements.txt        # Recommended Python dependencies
├── requirments.txt         # Course package list
├── .env.example            # Template for environment variables (API keys & model config)
├── .gitignore              # Files and folders excluded from Git version control
└── projects/
    └── RAG_APP/            # RAG Application pipeline
        ├── main.py         # PyPDF document loader, sanitization & chunking
        └── load_data.py    # Complete ingestion, metadata tagging, embeddings & MongoDB Atlas Vector Search
```

---

## 📚 Projects

### RAG_APP (`projects/RAG_APP/`)
End-to-end Retrieval-Augmented Generation (RAG) data pipeline:
- **`main.py`**:
  - **Document Loading**: Extracts pages from PDF documents using `PyPDFLoader` (`langchain_community`).
  - **Data Sanitization**: Filters out empty or short pages (e.g., word count < 20).
  - **Text Chunking**: Breaks text into overlapping segments via `RecursiveCharacterTextSplitter` (`chunk_size=500`, `chunk_overlap=150`).
- **`load_data.py`**:
  - **Automated Metadata Tagging**: Uses `create_metadata_tagger` with `ChatOpenAI` function calling to extract title, keywords, and code indicators.
  - **Voyage AI Embeddings**: Generates high-quality vector embeddings using `voyage-3.5-lite` via `langchain_voyageai`.
  - **Vector Database Storage**: Stores chunks, metadata, and embeddings into MongoDB Atlas via `MongoDBAtlasVectorSearch`.

---

## 🚀 Key Topics Covered in `basic_lang_chain.ipynb`

1. **Direct LLM Interaction using Groq SDK**:
   - Calling models like `openai/gpt-oss-120b` directly using `groq.Groq`.
   - Managing prompt messages and completion tokens.
   - Inspecting reasoning tokens and model response metadata.

2. **LangChain Integration (`langchain-groq`)**:
   - Initializing chat models with `ChatGroq`.
   - Invoking models with standard LangChain syntax (`llm.invoke(...)`).
   - Extracting `AIMessage` content and analyzing response metadata (`token_usage`, `finish_reason`).

3. **Universal Model Initialization with `init_chat_model`**:
   - Initializing chat models uniformly without provider-specific class imports via `langchain.chat_models.init_chat_model`.
   - Managing `MODEL` and `MODEL_PROVIDER` globally via `.env` configuration.
   - Using provider-prefix shorthand syntax: `init_chat_model("provider_name:model_id")` (e.g., `init_chat_model("groq:openai/gpt-oss-120b")`).

4. **Model Fallbacks & Core Components**:
   - Implementing fallback strategies across models using LangChain.
   - Restricting agent/model behavior under defined conditions.

5. **LangChain Message Types**:
   - Working with `SystemMessage`, `HumanMessage`, and `AIMessage` to structure prompts and control assistant behavior.

---

## 🛠️ Getting Started

### 1. Create and Activate a Virtual Environment

In Windows PowerShell:

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\activate
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure API Credentials

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Open `.env` and fill in your configuration:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
MODEL="openai/gpt-oss-120b"
MODEL_PROVIDER="groq"
```

> **Note:** Never commit `.env` or your raw API keys to GitHub. The `.gitignore` file is configured to keep it private.

### 4. Run the Jupyter Notebook

Launch JupyterLab or open the notebook directly in your IDE (VS Code / Antigravity):

```powershell
jupyter notebook basic_lang_chain.ipynb
```
Select the Python kernel from `.venv` when running cells.
