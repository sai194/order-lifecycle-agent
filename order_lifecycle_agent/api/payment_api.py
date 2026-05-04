from fastapi import FastAPI

app = FastAPI()

@app.get("/payments/{order_id}")
def get_payment(order_id: str):
    return {
        "order_id": order_id,
        "payment_status": "CAPTURED",
        "refund_status": "INITIATED",
        "refund_date": "2026-04-29"
    }
