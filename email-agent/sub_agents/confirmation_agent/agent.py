import sys
import yaml
with open("config.yml", 'r') as file:
    data = yaml.safe_load(file)

import os
os.environ["GOOGLE_API_KEY"] = data["GOOGLE_API_KEY"]

from google.adk.agents import LlmAgent
from . import prompt
from .tool import send_mail

confirmation_agent = LlmAgent(
    model = data["MODEL"],
    name = "confirmation_agent",
    description = "A helpful agent to confirm the mail to be sent and Send the mail using the `send_mail` tool.",
    instruction = prompt.instruction_confirmation_agent,
    tools = [send_mail]
)