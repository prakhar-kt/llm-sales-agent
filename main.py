from dotenv import load_dotenv
from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import nest_asyncio

from config import model
from instructions import instructions_email_picker
from tools import (
    send_email,
    professional_sales_tool,
    witty_sales_tool,
    concise_sales_tool,
)


nest_asyncio.apply()
load_dotenv(override=True)


def main():

    message = "Send a cold sales email addressed to 'Dear CEO'"

    tools = [professional_sales_tool, witty_sales_tool, concise_sales_tool, send_email]

    sales_manager = Agent(
        name="Sales Manager",
        instructions=instructions_email_picker,
        tools=tools,
        model=model,
    )

    with trace("Sales Manager"):
        result = await Runner.run(sales_manager, message)


if __name__ == "__main__":
    main()
