
import pandas as pd

def write_csv(df, output_file):
    """
    Writes a DataFrame to an output CSV file.
    
    Parameters:
    - df (DataFrame): The pandas DataFrame to write to the file.
    - output_file (str): Path to the output CSV file.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Output file '{output_file}' successfully written.")
    except Exception as e:
        print(f"An error occurred while writing the output file: {e}")

