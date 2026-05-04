from google.adk.agents import Agent

from order_lifecycle_agent.services.config import USE_MCP
from order_lifecycle_agent.tools.api_tool import get_payment_details
from order_lifecycle_agent.tools.db_tool import get_order_details
from order_lifecycle_agent.tools.mcp_tool import get_mcp_toolset
from order_lifecycle_agent.tools.pdf_tool import get_refund_policy
from order_lifecycle_agent.tools.policy_vector_tool import search_refund_policy

tools=[
    get_payment_details,
    search_refund_policy,
    get_refund_policy,
]

if USE_MCP:
    tools.append(get_mcp_toolset())
else:
    tools.append(get_order_details)

root_agent = Agent(
    name="order_lifecycle_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an Order Lifecycle Agent.

    Use MCP database tools when available to fetch order and return lifecycle data.
    Otherwise, use the local DB tool.

    Use payment API tools for payment capture, refund status, refund date, and settlement details.

    For refund policy:
    1. Always use search_refund_policy first to retrieve the most relevant policy chunks.
    2. Use get_refund_policy only as a fallback if vector search is unavailable or insufficient.
    3. Do not interpret policy without retrieved policy context.

    Reasoning rules:
    - Do not guess.
    - If order, return, payment, or policy data is missing, clearly say what is missing.
    - Base conclusions only on tool outputs.
    - If refund is within SLA, say no escalation is needed.
    - If refund failed or is outside SLA, recommend escalation.

    Always respond with:
    - Executive Summary
    - Order Summary
    - Return Summary
    - Payment Summary
    - Lifecycle Timeline
    - Policy Interpretation
    - Final Recommendation
    - Execution Trace / Tool Evidence if available
    """,
    tools=tools,
)