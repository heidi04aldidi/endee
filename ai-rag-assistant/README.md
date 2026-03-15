# AI RAG Knowledge Assistant 🧠

A Streamlit app for Retrieval-Augmented Generation using ML documents.

## 🚀 Quick Start

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **(Optional) Set OpenAI API Key for GPT generation:**

   ```bash
   cp .env.example .env
   # Edit .env with your OPENAI_API_KEY
   source .env  # or export OPENAI_API_KEY=sk-...
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   Open http://localhost:8501

## Features

- Loads docs from `data/documents.txt`
- SentenceTransformer embeddings (`all-MiniLM-L6-v2`)
- In-memory cosine similarity vector search
- OpenAI GPT-4o-mini generation **or local fallback** (no quota issues)

## Troubleshooting

- **No API key?** App auto-falls back to showing context.
- **Watchdog perf:** `pip install watchdog`
- HF warnings: Normal on first model download.

## Structure

```
ai-rag-assistant/
├── app.py              # Streamlit UI
├── data/documents.txt  # Sample ML docs
├── embeddings/         # Embedder
├── database/           # VectorStore
└── rag/               # Retrieval & Generation
```
