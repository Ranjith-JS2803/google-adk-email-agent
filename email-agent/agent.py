import yaml
with open("config.yml", 'r') as file:
    data = yaml.safe_load(file)

import os
os.environ["GOOGLE_API_KEY"] = data["GOOGLE_API_KEY"]

from google.adk.agents import LlmAgent
from .sub_agents.draft_email_agent.agent import draft_email_agent
from .sub_agents.confirmation_agent.agent import confirmation_agent
from . import prompt

email_agent = LlmAgent(
    model = data["MODEL"],
    name = "email_agent",
    description = "Handles user interactions for drafting and sending an email.",
    instruction = prompt.instruction_email_agent,
    sub_agents = [
        draft_email_agent
    ],
)

root_agent = email_agent