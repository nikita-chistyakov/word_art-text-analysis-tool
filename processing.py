import pandas as pd

def process_data(df, process_function):
    """
    Processes the DataFrame using a custom function.
    
    Parameters:
    - df (DataFrame): The input pandas DataFrame.
    - process_function (function): A function that processes the DataFrame and returns a new DataFrame.
    
    Returns:
    - DataFrame: The processed DataFrame.
    """
    try:
        processed_df = process_function(df)
        print("Data successfully processed.")
        return processed_df
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        return None
    