import pandas as pd
from typing import Tuple, Optional
from agents.code_generator import SFNFeatureCodeGeneratorAgent
from agents.code_executor import CodeExecutorAgent
from tasks import Task
from utils.retry_utils import with_retry
import logging

class SuggestionApplier:
    def __init__(
        self,
        code_generator: SFNFeatureCodeGeneratorAgent,
        code_executor: CodeExecutorAgent,
        logger: logging.Logger
    ):
        self.code_generator = code_generator
        self.code_executor = code_executor
        self.logger = logger
    
    @with_retry(max_attempts=3)
    def generate_and_execute_code(
        self,
        suggestion: str,
        df: pd.DataFrame,
        user_input: Optional[str] = None
    ) -> pd.DataFrame:
        """Generate and execute code for a given suggestion."""
        # Prepare the task
        code_task = Task("generate the code of suggestion")
        code_task.data = {
            "suggestion": suggestion + (f" User input: {user_input}" if user_input else ""),
            "columns": df.columns,
            "dtypes": df.dtypes,
            "sample_records": df.head(3).to_dict()
        }
        
        # Generate and execute code
        generated_code = self.code_generator.execute_task(code_task)
        self.logger.debug(f"Generated code:\n{generated_code}")
        
        execute_task = Task("Execute the generated code")
        execute_task.code = generated_code
        execute_task.data = df
        
        return self.code_executor.execute_task(execute_task)

    def apply_suggestion(
        self,
        suggestion: str,
        df: pd.DataFrame,
        user_input: Optional[str] = None
    ) -> Tuple[pd.DataFrame, bool, str]:
        """Apply a cleaning suggestion to the DataFrame."""
        try:
            self.logger.info(f"Attempting to apply suggestion: {suggestion}")
            
            # Generate and execute code with retries
            df = self.generate_and_execute_code(suggestion, df, user_input)
            
            self.logger.info(f"Suggestion applied successfully. New data shape: {df.shape}")
            return df, True, "All good"
            
        except Exception as e:
            error_msg = f"Failed to apply suggestion: {suggestion}. Error: {str(e)}"
            self.logger.error(error_msg)
            return df, False, f"Error: {str(e)}"
