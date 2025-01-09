import pandas as pd

def read_csv(input_file):
    """
    Reads data from an input CSV file.
    
    Parameters:
    - input_file (str): Path to the input CSV file.
    
    Returns:
    - DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(input_file)
        print(f"Input file '{input_file}' successfully read.")
        return df
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None
    
if __name__ == "__main__": 
    print("my name is input manager")
    input_file = "TEST COMMENTS/product_comments.csv"
    df = read_csv(input_file=input_file)
    print(df)