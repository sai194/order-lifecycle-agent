import os

MCP_TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "http://127.0.0.1:5000")
USE_MCP = os.getenv("USE_MCP", "false").lower() == "true"