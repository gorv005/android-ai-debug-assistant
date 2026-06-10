from llama_index.core import (VectorStoreIndex,SimpleDirectoryReader,StorageContext,Settings)

from llama_index.vector_stores.chroma import ChromaVectorStore

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

import chromadb



print("Loading embedding model...")

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.llm = None

print("Loading documents...")

documents = SimpleDirectoryReader("/workspace/shared/android_ai_debug_assistant/docs").load_data()

print(f"Loaded {len(documents)} documents")



print("Creating ChromaDB...")

db = chromadb.PersistentClient(path="/workspace/shared/android_ai_debug_assistant/chroma_db")

chroma_collection = db.get_or_create_collection("android_debug_collection")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)



print("Creating vector index...")

index = VectorStoreIndex.from_documents(documents,storage_context=storage_context)

print("Vector DB created successfully!")