import os
from typing import List, Dict, Any
import pandas as pd
from openai import OpenAI
from agents.base_agent import SFNAgent
from tasks.task import Task
from utils.prompt_manager import PromptManager
from config.model_config import MODEL_CONFIG

class SFNSuggestionsGeneratorAgent(SFNAgent):
    def __init__(self):
        super().__init__(name="Suggestions Generator", role="To generate suggestions")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_config = MODEL_CONFIG["feature_suggester"]

    def execute_task(self, task: Task) -> List[str]:
        """
        Execute the feature suggestion task.
        
        :param task: Task object containing the data and category
        :return: List of feature suggestions
        """
        if not isinstance(task.data, dict) or 'df' not in task.data or 'category' not in task.data:
            raise ValueError("Task data must be a dictionary containing 'df' and 'category' keys")

        df = task.data['df']
        category = task.data['category']
        
        columns = df.columns.tolist()
        sample_records = df.head(3).to_dict(orient='records')
        describe_dict = df.describe().to_dict()

        suggestions = self._generate_suggestions(columns, sample_records, describe_dict, category)
        return suggestions

    def _generate_suggestions(self, columns: List[str], sample_records: List[Dict[str, Any]], 
                            describe_dict: Dict[str, Dict[str, float]], category: str) -> List[str]:
        """
        Generate suggestions based on the data and category.
        
        :param columns: List of column names
        :param sample_records: List of dictionaries representing sample records
        :param describe_dict: Dictionary of statistical descriptions
        :param category: Identified category of the data
        :return: List of suggestions
        """
        # Get prompts using PromptManager
        system_prompt,user_prompt = PromptManager.load_prompt('suggestions_generator', 
                                          columns=columns,
                                          sample_records=sample_records,
                                          describe_dict=describe_dict,
                                          category=category)
        
        response = self.client.chat.completions.create(
            model=self.model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=self.model_config["temperature"],
            max_tokens=self.model_config["max_tokens"],
            n=self.model_config["n"],
            stop=self.model_config["stop"]
        )

        suggestions_text = response.choices[0].message.content.strip()
        return self._parse_suggestions(suggestions_text)

    def _parse_suggestions(self, suggestions_text: str) -> List[str]:
        """
        Parse the suggestions text into a list of individual suggestions.
        
        :param suggestions_text: Raw text of suggestions from the OpenAI model
        :return: List of individual suggestions
        """
        # Split the text by newlines and remove any empty lines
        suggestions = [line.strip() for line in suggestions_text.split('\n') if line.strip()]
        
        # Remove numbering from each suggestion
        suggestions = [suggestion.split('. ', 1)[-1] for suggestion in suggestions]
        
        return suggestions