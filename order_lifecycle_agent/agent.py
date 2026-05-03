from google.adk.agents import Agent
from order_lifecycle_agent.tools.db_tool import get_order_details
from order_lifecycle_agent.tools.api_tool import get_payment_details
from order_lifecycle_agent.tools.pdf_tool import get_refund_policy

root_agent = Agent(
    name="order_lifecycle_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an Order Lifecycle Agent.

    Analyze refund issues using:
    - Order + return details
    - Payment API
    - Refund policy

    Provide clear explanation with reasoning.
    """,
    tools=[
        get_order_details,
        get_payment_details,
        get_refund_policy
    ],
)
