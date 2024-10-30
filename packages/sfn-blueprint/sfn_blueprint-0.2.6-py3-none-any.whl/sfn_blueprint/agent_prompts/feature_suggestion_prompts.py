from typing import Dict, Any, List

def get_feature_suggestion_prompt(**kwargs) -> Dict[str, str]:
    """
    Generate both system and user prompts for feature suggestion generation.
    
    Required kwargs:
    - columns: List[str]
    - sample_records: List[Dict[str, Any]]
    - describe_dict: Dict[str, Dict[str, float]]
    - category: str
    
    Returns:
    - Dict containing both system and user prompts
    """
    system_prompt = """You are a data science expert specializing in feature engineering and data quality improvement."""
    
    # Format the input data into strings
    columns_str = ", ".join(kwargs['columns'])
    samples_str = "\n".join([str(record) for record in kwargs['sample_records']])
    describe_str = str(kwargs['describe_dict'])
    
    user_prompt = f"""
    As a data science expert, analyze the following dataset and provide suggestions for feature engineering and data quality improvement.

    Dataset Category: {kwargs['category']}
    
    Columns: {columns_str}
    
    Sample Records:
    {samples_str}
    
    Statistical Description:
    {describe_str}

    Based on this information, suggest features or transformations that could improve the dataset for analysis or machine learning tasks. Consider the following:

    1. Relevant derived features based on the identified category ({kwargs['category']})
    2. Potential data quality issues and how to address them
    3. Possible feature combinations or interactions
    4. Numerical transformations (e.g., normalization, binning)
    5. Categorical encoding techniques
    6. Time-based features (if applicable)
    7. Text processing techniques (if applicable)

    Provide each suggestion as a separate item in a numbered list.
    Focus on practical steps to improve the data quality and create meaningful features.
    DO NOT DUPLICATE SUGGESTIONS.
    DO NOT PROVIDE HEADINGS.
    ONLY PROVIDE A LIST OF SUGGESTIONS separated by newlines.
    """
    
    return  system_prompt, user_prompt
