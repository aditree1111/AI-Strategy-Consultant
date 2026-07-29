import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create an in-memory ChromaDB client
client = chromadb.Client()

collection = client.get_or_create_collection(
    name="annual_reports"
)


def create_vector_store(chunks):
    """
    Store chunks in ChromaDB.
    """

    collection.delete(where={})

    embeddings = embedding_model.encode(chunks).tolist()

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    return collection