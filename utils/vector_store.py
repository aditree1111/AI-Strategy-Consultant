import chromadb
from utils.embeddings import create_embeddings

client = chromadb.Client()

try:
    collection = client.get_collection("annual_reports")
except:
    collection = client.create_collection("annual_reports")


def build_vector_store(chunks):

    embeddings = create_embeddings(chunks)

    ids = [str(i) for i in range(len(chunks))]

    try:
        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )
    except:
        pass

    return collection


def search_chunks(query, top_k=5):

    embedding = create_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]