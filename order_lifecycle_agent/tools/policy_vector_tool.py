import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "refund_policy"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def search_refund_policy(query: str):
    """
    Search refund policy from persisted ChromaDB vector database.
    Use this tool before reading the full PDF.
    """

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query], normalize_embeddings=True).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )

    matches = []

    for i in range(len(results["documents"][0])):
        matches.append(
            {
                "chunk_id": results["ids"][0][i],
                "text": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            }
        )

    return {
        "query": query,
        "matches": matches,
    }