# 1. Init DB
uv run python scripts/init_db.py

# 2. Start payment API
uv run uvicorn api.payment_api:app --reload --port 8000

# 3. Start ADK Web UI
uv run adk web --port 8001


# 4. Questions
- "Should I escalate the refund for order 1001?"
- "Is there any issue with refund for order 1001?"
- "What is the status of refund for order 1001?"