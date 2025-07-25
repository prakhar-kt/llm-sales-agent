import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from agents import function_tool

from custom_agents import (
    sales_agent_professional,
    sales_agent_witty,
    sales_agent_concise,
)


@function_tool
def send_email():
    """Send out an email with the given body to all sales prospects"""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("rahkarp@gmail.com")
    to_email = To("rahkarp@gmail.com")
    content = Content("text/plain", "This is an important test email")
    mail = Mail(from_email, to_email, "Test Email", content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": response.status_code}


description = "Write a cold sales email"

# Convert Agents to tools
professional_sales_tool = sales_agent_professional.as_tool(
    tool_name="sales_agent_professional", tool_description=description
)

witty_sales_tool = sales_agent_witty.as_tool(
    tool_name="sales_agent_witty", tool_description=description
)

concise_sales_tool = sales_agent_concise.as_tool(
    tool_name="sales_agent_concise", tool_description=description
)
