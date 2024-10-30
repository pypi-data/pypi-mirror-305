import pandas as pd
from agents.base_agent import SFNAgent
import os
from openai import OpenAI
from dotenv import load_dotenv
import re
from utils.prompt_manager import PromptManager
from config.model_config import MODEL_CONFIG

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

class SFNFeatureCodeGeneratorAgent(SFNAgent):
    def __init__(self):
        super().__init__(name="Feature Code Generator", role="Python Developer")
        self.model_config = MODEL_CONFIG["code_generator"]
    
    def execute_task(self, task, error_message=None) -> str:
        # Prepare kwargs for prompt
        prompt_kwargs = {
            'suggestion': task.data['suggestion'],
            'columns': task.data['columns'],
            'dtypes': task.data['dtypes'],
            'sample_records': task.data['sample_records'],
            'error_message': error_message
        }
        
        # Get both system and user prompts using PromptManager
        system_prompt, user_prompt = PromptManager.load_prompt('code_generator', **prompt_kwargs)
        
        print('>>> inside feature code generator agent..', user_prompt)
        
        response = client.chat.completions.create(
            model=self.model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=self.model_config["temperature"],
            max_tokens=self.model_config["max_tokens"]
        )

        code = response.choices[0].message.content.strip()
        print('>>> response received', code)
        return self.clean_generated_code(code)
    
    @staticmethod
    def clean_generated_code(code: str) -> str:
        code = re.sub(r'```python\n|```', '', code)
        code = re.sub(r'print\(.*\)\n?', '', code)
        code = re.sub(r'#.*\n', '', code)
        code = '\n'.join(line for line in code.split('\n') if line.strip())
        print('>>code cleaned..', code)
        return code