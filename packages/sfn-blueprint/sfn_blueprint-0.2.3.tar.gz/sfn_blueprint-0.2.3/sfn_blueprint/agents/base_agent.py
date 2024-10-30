import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client globally (or via an environment variable)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

class SFNAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def execute_task(self, task):
        raise NotImplementedError("Subclasses must implement execute_task method")