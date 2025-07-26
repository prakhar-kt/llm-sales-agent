import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from typing import Dict
from agents import function_tool

from custom_agents import (
    sales_agent_professional,
    sales_agent_witty,
    sales_agent_concise,
    subject_writer,
    html_converter,
)


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to all sales prospects"""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("rahkarp@gmail.com")
    to_email = To("rahkarp@gmail.com")
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
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

subject_tool = subject_writer.as_tool(
    tool_name="subject_writer",
    tool_description="Write a subject for a cold sales email",
)

html_tool = html_converter.as_tool(
    tool_name="html_converter",
    tool_description="Convert a text email to html email body",
)


email_tools = [subject_tool, html_tool, send_email]

sales_tools = [professional_sales_tool, witty_sales_tool, concise_sales_tool]
