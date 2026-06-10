from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb

Settings.llm = None

Settings.embed_model = HuggingFaceEmbedding(
                    model_name="BAAI/bge-small-en-v1.5"
    )

db = chromadb.PersistentClient(
                    path="/workspace/shared/android_ai_debug_assistant/chroma_db"
    )

chroma_collection = db.get_or_create_collection(
                    "android_debug_collection"
    )

vector_store = ChromaVectorStore(
                    chroma_collection=chroma_collection
    )

index = VectorStoreIndex.from_vector_store(
                    vector_store
    )

query_engine = index.as_query_engine()

response = query_engine.query(
                    "Why is bluetooth pairing failing?"
    )

print("\nAI Debug Suggestion:\n")
print(response)