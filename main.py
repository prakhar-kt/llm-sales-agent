from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
from openai.types.responses import ResponseTextDeltaEvent
from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import asyncio
import nest_asyncio

from instructions import (
    instructions_professional, 
    instructions_witty, 
    instructions_concise,
    instructions_email_picker
)


nest_asyncio.apply()

load_dotenv(override=True)

model = "gpt-4o-mini"

@function_tool
def send_email():
    """ Send out an email with the given body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("rahkarp@gmail.com")
    to_email = To("rahkarp@gmail.com")
    content = Content("text/plain", "This is an important test email")
    mail = Mail(from_email, to_email, "Test Email", content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": response.status_code}
    
sales_agent_professional = Agent(
    name="Professional Sales Agent",
    instructions=instructions_professional,
    model=model
)

sales_agent_witty = Agent(
    name="Engaging Sales Agent",
    instructions=instructions_witty,
    model=model
)

sales_agent_concise = Agent(
    name="Busy Sales Agent",
    instructions=instructions_concise,
    model=model
)

email_picker = Agent(
    name="email_picker",
    instructions=instructions_email_picker,
    model=model
)

description = "Write a cold sales email"

# Convert Agents to tools
professional_sales_tool = sales_agent_professional.as_tool(
                            tool_name="sales_agent_professional",
                            tool_description=description
)

witty_sales_tool = sales_agent_witty.as_tool(
                    tool_name="sales_agent_witty",
                    tool_description=description
)

concise_sales_tool = sales_agent_concise.as_tool(
                        tool_name="sales_agent_concise",
                        tool_description=description
)

tools = [professional_sales_tool,
         witty_sales_tool,
         concise_sales_tool, 
         send_email]




# # Streaming results
# result = Runner.run_streamed(sales_agent_professional, 
#                              input="Write a cold sales email")
# async for event in result.stream_events():
#     if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#         print(event.data.delta, end="", flush=True)



# with trace("Email selection from sales people"):
#     results = await asyncio.gather(
#         Runner.run(sales_agent_professional, message),
#         Runner.run(sales_agent_witty, message),
#         Runner.run(sales_agent_concise, message)
#     )
    
# outputs = [result.final_output for result in results]

# emails = "Cold sales emails:\n\n" + "\n\nEmail:\n\n".join(outputs)

# best_email = await Runner.run(email_picker, emails)

# print(f"Best sales email:\n{best_email.final_output}")






















def main():
    


if __name__ == "__main__":
    main()
