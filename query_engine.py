from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

print("===== Android AI Debug Assistant =====")

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

Settings.llm = None

db = chromadb.PersistentClient(
    path="/workspace/shared/android_ai_debug_assistant/chroma_db"
)

chroma_collection = db.get_or_create_collection(
    "android_debug_collection"
)

print("Documents in collection:", chroma_collection.count())

vector_store = ChromaVectorStore(
    chroma_collection=chroma_collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

index = VectorStoreIndex.from_vector_store(
    vector_store,
    storage_context=storage_context
)

query_engine = index.as_query_engine(similarity_top_k=2)

queries = [
    "Why is bluetooth pairing failing?",
    "Why is StateFlow not recomposing?",
    "Why is app crashing on launch?",
    "Why is WorkManager not running?"
]

for q in queries:
    print("\n" + "=" * 60)
    print(f"\nQuery: {q}")

    response = query_engine.query(q)

    print("\nAI Suggestion:")
    print(response)