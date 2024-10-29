from typing import Dict, Any, Tuple
import importlib
import os
from pathlib import Path

class PromptManager:
    @staticmethod
    def load_prompt(prompt_type: str, **kwargs) -> Tuple[str, str]:
        """
        Load and format prompts from the appropriate module.
        
        Args:
            prompt_type: The type of prompt to load (e.g., 'feature_engineering')
            **kwargs: Arguments to format the prompt with
            
        Returns:
            Tuple[str, str]: (system_prompt, user_prompt)
        """
        try:
            # Dynamically import the appropriate prompt module
            module = importlib.import_module(f'data.agent_prompts.{prompt_type}_prompts')
            prompt_function = getattr(module, f'get_{prompt_type}_prompt')
            return prompt_function(**kwargs)
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Prompt type '{prompt_type}' not found: {str(e)}")