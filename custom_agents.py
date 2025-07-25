from agents import Agent
from config import model
from instructions import (
    instructions_professional,
    instructions_concise,
    instructions_witty,
    instructions_email_picker,
)


sales_agent_professional = Agent(
    name="Professional Sales Agent", instructions=instructions_professional, model=model
)

sales_agent_witty = Agent(
    name="Engaging Sales Agent", instructions=instructions_witty, model=model
)

sales_agent_concise = Agent(
    name="Busy Sales Agent", instructions=instructions_concise, model=model
)

email_picker = Agent(
    name="email_picker", instructions=instructions_email_picker, model=model
)
