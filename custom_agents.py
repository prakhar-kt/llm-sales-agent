from agents import Agent
from config import model
from instructions import (
    instructions_professional,
    instructions_concise,
    instructions_witty,
    subject_instructions,
    html_instructions,
    email_instructions,
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

email_picker = Agent(name="Email picker", instructions=email_instructions, model=model)

subject_writer = Agent(
    name="Email subject writer", instructions=subject_instructions, model=model
)

html_converter = Agent(
    name="HTML email body converter", instructions=html_instructions, model=model
)
