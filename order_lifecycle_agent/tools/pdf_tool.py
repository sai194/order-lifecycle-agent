# order_lifecycle_agent/tools/pdf_tool.py
from pypdf import PdfReader
def get_refund_policy():
    reader = PdfReader("data/refund_policy.pdf")
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text