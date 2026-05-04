from google.adk.tools.toolbox_toolset import ToolboxToolset

from order_lifecycle_agent.services.config import MCP_TOOLBOX_URL


def get_mcp_toolset():
    return ToolboxToolset(server_url=MCP_TOOLBOX_URL)