# 1. Init DB -- Sqllite 
uv run python scripts/init_db.py

# 2. Start payment API
uv run uvicorn api.payment_api:app --reload --port 8000
# Build policy index
uv run python scripts/build_policy_index.py
Creates data/chroma_db/
# Postgres, Init DB, MCP setup
docker compose down
docker compose pull
docker compose up -d
./toolbox --tools-file <pwd>/mcp/tools.yaml --port 5000
<!-- ./toolbox --tools-file /Users/saiyeluri/Documents/Apps/order-lifecycle-agent/mcp/tools.yml --port 5000 -->
If init.sql changed, then 
docker compose down -v
docker compose up -d

# 3. Start ADK Web UI
uv run adk web --port 8001
# Run Agent with MCP (using .env)
USE_MCP=true MCP_TOOLBOX_URL=http://127.0.0.1:5001 uv run adk web --port 8001
# Run Agent locally with DB (local DB not docker)
USE_MCP=false uv run uvicorn app.main:app --reload --port 8001




# 4. Questions
- "Should I escalate the refund for order 1001?"
- "Is there any issue with refund for order 1001?"
- "What is the status of refund for order 1001?"

# 9. UV libs
uv add fastapi google-adk pypdf requests uvicorn python-dotenv