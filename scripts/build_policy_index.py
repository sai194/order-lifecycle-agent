from pathlib import Path
import re

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

PDF_PATH = Path("data/refund_policy.pdf")
CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "refund_policy"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def extract_pdf_text():
    reader = PdfReader(str(PDF_PATH))
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def chunk_text(text: str, max_chars: int = 500):
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks = []

    for paragraph in paragraphs:
        if len(paragraph) <= max_chars:
            chunks.append(paragraph)
        else:
            for i in range(0, len(paragraph), max_chars):
                chunks.append(paragraph[i:i + max_chars])

    return chunks


def build_index():
    text = extract_pdf_text()
    chunks = chunk_text(text)

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks, normalize_embeddings=True).tolist()

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    existing = [c.name for c in client.list_collections()]
    if COLLECTION_NAME in existing:
        client.delete_collection(COLLECTION_NAME)

    collection = client.create_collection(name=COLLECTION_NAME)

    collection.add(
        ids=[f"refund_policy_chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {
                "source": "refund_policy.pdf",
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ],
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB at {CHROMA_PATH}")


if __name__ == "__main__":
    build_index()