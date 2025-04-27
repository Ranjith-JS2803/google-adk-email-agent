
# Email Agent

A multi-agent system designed to draft and send emails intelligently using Google Generative AI models, built with Google's Agent Development Kit (ADK).

## Project Structure

parent-dir/  
├── email-agent/ \
├── config.yml    
├── requirements.txt

- **email-agent/**: Contains all the project source code.
- **config.yml**: Configuration file with model and API credentials.
  - Example YAML format:
    ```yaml
    MODEL: "<your-model-name>"
    GOOGLE-API-KEY: "<your-google-api-key>"
    ```

## ⚙️ Setup Instructions

1. **Install Dependencies**:

   Ensure you have Python 3.10+ installed. Create and activate a virtual environment, then install the required packages:

```bash
python -m venv adk_env
source adk_env/bin/activate  # On Windows: adk_env\Scripts\activate
pip install -r requirements.txt
```

2. **Configure API Keys**:

   Update the config.yml file with your model name and Google API key.

3. **Run the Application**:

   Navigate to the parent-dir (the directory containing email-agent/ and config.yml) and start the ADK web interface:

```bash
adk web
```

   This will launch a local web interface, typically accessible at http://localhost:8000, allowing you to interact with your agent.

## About the System

- **Master Agent**: Interacts with the user to understand the purpose of the email.
- **Sub-Agents**:
  - `recipient_email_agent`: Collects the recipient's email address.
  - `draft_subject_agent`: Drafts a suitable subject line.
  - `draft_body_agent`: Writes the body content.
  - `confirmation_agent`: Verifies all details and triggers sending.
- **Tools**:
   - `send_mail`: function defined to send the mail given the *to*, *subject* and *body* of the mail.
- **Integration**: Built to work with Google's Gemini models for content generation.