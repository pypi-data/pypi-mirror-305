from typing import Dict, Any, Tuple

def get_code_generator_prompt(**kwargs) -> Tuple[str, str]:
    """
    Generate prompts for feature engineering code generation.
    
    Required kwargs:
    - suggestion: str
    - columns: list
    - dtypes: dict
    - sample_records: list
    - error_message: str (optional)
    
    Returns:
    Tuple[str, str]: (system_prompt, user_prompt)
    """
    system_prompt = "You are a Python code generator for feature engineering tasks."
    
    user_prompt = """
    Generate Python code to implement the following feature engineering suggestion:
    
    {suggestion}
    
    Dataset information:
    Columns: {columns}
    Data types: {dtypes}
    Sample records: {sample_records}
    
    The code should work with a pandas DataFrame named 'df'.
    Only provide the Python code necessary to implement the feature.
    Do not include any print statements or explanatory comments.
    Ensure the new feature is added to the 'df' DataFrame.
    Do not include any markdown formatting or code block indicators.
    Make sure that the column names etc. are as per the provided dataset and NO GENERALIZATION IS DONE.
    If there is looping needed, provide the entire code.
    Write the code diligently like a proper developer, don't cut corners.
    """
    
    formatted_prompt = user_prompt.format(**kwargs)
    
    if kwargs.get('error_message'):
        formatted_prompt += f"\n\nThe previous code failed: {kwargs['error_message']}\nPlease fix it."
    
    return system_prompt, formatted_prompt