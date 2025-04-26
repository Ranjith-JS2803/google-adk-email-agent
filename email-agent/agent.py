import os
from google.adk.agents import LlmAgent, SequentialAgent
from . import prompts
from .tools import send_mail

os.environ["GOOGLE_API_KEY"] = "AIzaSyA-DptK9fSIw9VxxAxuCPKOUJTu6vc_PjI"
MODEL = "gemini-2.5-pro-exp-03-25"

draft_mail_subject_agent = LlmAgent(
    model = MODEL,
    name="draft_mail_subject_agent",
    description = "A helpful agent to draft a mail subject.",
    instruction = prompts.instruction_draft_mail_subject_agent,
    output_key = "draft_subject"
)

draft_mail_body_agent = LlmAgent(
    model = MODEL,
    name="draft_mail_body_agent",
    description = "A helpful agent to draft a mail body.",
    instruction = prompts.instruction_draft_mail_body_agent,
    output_key = "draft_body"
)

critic_agent = LlmAgent(
    model = MODEL,
    name = "critic_agent",
    description = "A helpful agent to critique mail subject and body. Send the mail using the `send_mail` tool.",
    instruction = prompts.instruction_critic_agent,
)

confirmation_agent = LlmAgent(
    model = MODEL,
    name = "confirmation_agent",
    description = "A helpful agent to confirm the mail to be sent and Send the mail using the `send_mail` tool.",
    instruction = prompts.instruction_confirmation_agent,
    tools = [send_mail]
)

email_agent = LlmAgent(
    model = MODEL,
    name = "email_agent",
    description = "Writes a draft mail with subject and body then passes it to critic for further consideration.",
    instruction = prompts.instruction_email_agent,
    sub_agents = [
        draft_mail_subject_agent,
        draft_mail_body_agent,
        critic_agent,
        confirmation_agent
    ],
)

root_agent = email_agent