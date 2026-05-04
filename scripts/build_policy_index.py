import os
import pickle
import re
from pathlib import Path

from pypdf import PdfReader

PDF_PATH = Path("data/refund_policy.pdf")
INDEX_PATH = Path("data/policy_vector_index.pkl")


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def chunk_text(text: str, max_chars: int = 500) -> list[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    chunks = []

    for paragraph in paragraphs:
        if len(paragraph) <= max_chars:
            chunks.append(paragraph)
        else:
            for i in range(0, len(paragraph), max_chars):
                chunks.append(paragraph[i : i + max_chars])

    return chunks


def simple_embedding(text: str) -> set[str]:
    """
    Simple local embedding substitute for Blog 2.
    This creates keyword-token vectors.
    Blog 3 can replace this with Gemini / Vertex AI embeddings.
    """
    tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return set(tokens)


def build_index():
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    text = extract_pdf_text(PDF_PATH)
    chunks = chunk_text(text)

    if not chunks:
        raise ValueError("No text chunks extracted from PDF.")

    index = []

    for idx, chunk in enumerate(chunks):
        index.append(
            {
                "id": f"policy_chunk_{idx}",
                "text": chunk,
                "tokens": simple_embedding(chunk),
            }
        )

    os.makedirs(INDEX_PATH.parent, exist_ok=True)

    with open(INDEX_PATH, "wb") as f:
        pickle.dump(index, f)

    print(f"Built policy index with {len(index)} chunks")
    print(f"Saved index to {INDEX_PATH}")


if __name__ == "__main__":
    build_index()