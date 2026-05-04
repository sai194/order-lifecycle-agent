from pypdf import PdfReader


def get_refund_policy():
    """
    Fallback tool. Use only if vector policy search is unavailable
    or does not return enough context.
    """

    reader = PdfReader("data/refund_policy.pdf")
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return {
        "policy_text": text
    }