# Android AI Debug Assistant

AI-powered Android issue troubleshooting assistant using LlamaIndex + ChromaDB + HuggingFace embeddings.

## Problem Statement

Android developers spend significant time debugging repetitive issues like:
- Bluetooth pairing failures
- Compose lag
- StateFlow recomposition issues
- Permission crashes
- Network failures

This project creates an AI-powered semantic search assistant that retrieves similar historical issues and resolutions.

---

## Features

- Semantic search using embeddings
- ChromaDB vector database
- Android issue knowledge base
- AI-powered query engine
- Retrieval-Augmented Generation (RAG)
- Fast debugging assistance

---

## Tech Stack

- Python
- LlamaIndex
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

---

## Project Structure

```bash
android_ai_debug_assistant/
│
├── data/
│   ├── bluetooth_issue.txt
│   ├── stateflow_bug.txt
│   └── compose_lag.txt
│
├── chroma_db/
│
├── build_vector_db.py
├── query_engine.py
├── requirements.txt
├── README.md
└── demo_queries.txt
```

---

## Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build Vector Database

```bash
python build_vector_db.py
```

---

## Run Query Engine

```bash
python query_engine.py
```

---

## Example Queries

- Why is bluetooth pairing failing?
- Why is StateFlow not recomposing?
- Why is Compose screen lagging?
- Why are notifications delayed?

---

## Sample Output

```text
Issue:
Bluetooth scanner pairing failing on Android 14.

Cause:
Missing BLUETOOTH_CONNECT permission.

Resolution:
Request runtime Bluetooth permissions before pairing.
```

---

## Future Improvements

- Real LLM integration
- Streamlit UI
- Voice support
- Logcat analysis
- APK issue diagnosis

---

## Hackathon Submission

Built for:
TCS x AMD AI Hackathon 2026