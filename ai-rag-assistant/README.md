# AI RAG Knowledge Assistant with Endee

Streamlit app for Retrieval-Augmented Generation powered by **Endee** vector database.

## Quick Start

1. **Start Endee server** (persistent data in `./endee-data`):

   ```bash
   docker compose up -d
   ```

   Verify: http://localhost:8080

2. **Install Python deps**:

   ```bash
   cd ai-rag-assistant
   pip install -r requirements.txt
   ```

3. **(Optional) OpenAI key**:

   ```bash
   cp .env.example .env
   # Edit .env: OPENAI_API_KEY=sk-...
   ```

4. **Run app**:
   ```bash
   streamlit run app.py
   ```
   Open http://localhost:8501. App auto-indexes sample ML docs.

## Features

- Endee vector store (HNSW, cosine sim, metadata)
- SentenceTransformer `all-MiniLM-L6-v2` (dim=384)
- OpenAI GPT-4o-mini or local fallback
- Graceful if Endee down (prints warnings)

## Structure

```
ai-rag-assistant/
├── app.py              # Streamlit UI
├── endee_client.py     # Endee HTTP client
├── data/documents.txt  # Sample ML docs
├── embeddings/         # Doc loader/embedder
├── rag/               # Retrieval/generation
```

## Endee Config

- Port: 8080
- Collection: `documents`
- Auth: Optional via `ENDEE_TOKEN` in `.env`

## Troubleshooting

- Endee errors: Check `docker compose logs`
- No API key: Shows retrieved context
- HF cache: First run downloads model (~80MB)
