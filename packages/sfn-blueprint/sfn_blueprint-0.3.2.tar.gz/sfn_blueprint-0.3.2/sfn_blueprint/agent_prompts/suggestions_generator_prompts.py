from sfn_blueprint.utils.prompt_manager import SFNPromptManager
from typing import Tuple

def get_suggestions_generator_prompt(llm_provider: str = "openai", **kwargs) -> Tuple[str, str]:
    """
    Generate both system and user prompts for feature suggestion generation.
    
    Args:
        llm_provider: The LLM provider to use (e.g., 'openai', 'anthropic')
        **kwargs: Required prompt variables
    """
    # Format the input data into strings
    kwargs['columns_str'] = ", ".join(kwargs['columns'])
    kwargs['samples_str'] = "\n".join([str(record) for record in kwargs['sample_records']])
    kwargs['describe_str'] = str(kwargs['describe_dict'])
    
    prompt_manager = SFNPromptManager()
    return prompt_manager.get_prompt("suggestions_generator", llm_provider, **kwargs)
