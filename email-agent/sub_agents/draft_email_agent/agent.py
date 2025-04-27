
import yaml
with open("config.yml", 'r') as file:
    data = yaml.safe_load(file)

import os
os.environ["GOOGLE_API_KEY"] = data["GOOGLE_API_KEY"]

from google.adk.agents import LlmAgent
from ..confirmation_agent.agent import confirmation_agent
from . import prompt

# Recipient Email Agent
draft_recipient_email_agent = LlmAgent(
    model = data["MODEL"],
    name = "draft_recipient_email_agent",
    description = "Asks the user for the recipient's email address if it's missing.",
    instruction = prompt.instruction_draft_recipient_email_agent,
    output_key = "draft_recipient_email_id"
)

# Draft Subject Agent
draft_subject_agent = LlmAgent(
    model = data["MODEL"],
    name = "draft_subject_agent",
    description = "Generates the subject of the email.",
    instruction = prompt.instruction_draft_mail_subject_agent,
    output_key = "draft_subject"
)

# Draft Body Agent
draft_body_agent = LlmAgent(
    model = data["MODEL"],
    name = "draft_body_agent",
    description = "Generates the body of the email.",
    instruction = prompt.instruction_draft_mail_body_agent,
    output_key = "draft_body"
)

draft_email_agent = LlmAgent(
    name = "draft_email_agent",
    description = "Delegates to `draft_recipient_email_agent`",
    sub_agents = [
        draft_recipient_email_agent,
        draft_subject_agent,
        draft_body_agent,
        confirmation_agent
    ]
)