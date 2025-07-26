from dotenv import load_dotenv
from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import nest_asyncio

from config import model
from instructions import email_instructions, sales_manager_instructions
from tools import email_tools, sales_tools


nest_asyncio.apply()
load_dotenv(override=True)


async def main():

    emailer_agent = Agent(
        name="Email manager",
        instructions=email_instructions,
        model=model,
        tools=email_tools,
        handoff_description="Convert an email to HTML and send it",
    )

    handoffs = emailer_agent

    sales_manager = Agent(
        name="Sales Manager",
        instructions=sales_manager_instructions,
        tools=sales_tools,
        model=model,
        handoffs=handoffs,
    )

    message = "Send out a cold sales email addressed to Dear CEO"

    with trace("Sales Manager"):
        result = await Runner.run(sales_manager, message)


if __name__ == "__main__":
    main()
