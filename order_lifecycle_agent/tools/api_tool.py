import requests

def get_payment_details(order_id: str):
    return requests.get(f"http://127.0.0.1:8000/payments/{order_id}").json()
