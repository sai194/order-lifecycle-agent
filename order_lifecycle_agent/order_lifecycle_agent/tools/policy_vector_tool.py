import pickle
import re
from pathlib import Path

INDEX_PATH = Path("data/policy_vector_index.pkl")


def simple_embedding(text: str) -> set[str]:
    tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return set(tokens)


def score(query_tokens: set[str], chunk_tokens: set[str]) -> float:
    if not query_tokens or not chunk_tokens:
        return 0.0

    overlap = query_tokens.intersection(chunk_tokens)
    return len(overlap) / len(query_tokens)


def search_refund_policy(query: str):
    """
    Search persisted refund policy chunks.
    Use this before reading the full PDF.
    """

    if not INDEX_PATH.exists():
        return {
            "error": "POLICY_INDEX_NOT_FOUND",
            "message": "Run: uv run python scripts/build_policy_index.py",
        }

    with open(INDEX_PATH, "rb") as f:
        index = pickle.load(f)

    query_tokens = simple_embedding(query)

    ranked = []

    for item in index:
        ranked.append(
            {
                "id": item["id"],
                "text": item["text"],
                "score": score(query_tokens, item["tokens"]),
            }
        )

    ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)

    return {
        "query": query,
        "matches": ranked[:3],
    }