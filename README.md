# LangChain Learning Repository

A comprehensive collection of LangChain learning experiments, hands-on notebooks, LLM integrations, embeddings, and prompt engineering projects.

---

## 📁 Repository Structure

```text
Lang_chain_Learning/
├── Campus_X/                # LangChain tutorial modules & exercises (CampusX series)
│   ├── Chains/              # LangChain Sequential & Custom Chains
│   ├── MODELS/              # Chat models (Google Gemini, Hugging Face), embeddings, and LLMs
│   ├── PROMPTS/             # PromptTemplate and FewShotPrompt examples
│   └── stracture_out/       # Structured output parsing with Pydantic & LangChain
│
└── Laing_Chain_Course/      # Hands-on LangChain Course
    ├── basic_lang_chain.ipynb # Notebook covering Groq SDK, ChatGroq, and init_chat_model
    ├── notes.txt            # Virtual environment and setup notes
    ├── requirements.txt     # Python dependencies
    └── projects/            # Practice projects (e.g. RAG_APP with PyPDFLoader & MongoDB)
        └── RAG_APP/
            ├── main.py      # Document loading and preprocessing pipeline
            └── load_data.py # Ingestion, metadata tagging, embeddings & MongoDB Atlas Vector Search
```

---

## ⚡ Quick Start

### 1. Set Up Environment
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install Requirements
```powershell
pip install -r Laing_Chain_Course/requirements.txt
```

### 3. API Keys Configuration
Create a `.env` file in the relevant subfolder (e.g. `Laing_Chain_Course/.env`) based on the `.env.example` templates.
Ensure API keys such as `GROQ_API_KEY` or `Google_Gemini_API_KEY` are defined.

---

## 🔒 Security Note
All `.env` files and `.venv` folders are strictly excluded by `.gitignore` to prevent any credential leakage.
