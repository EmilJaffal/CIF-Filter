import pandas as pd


def process_excel(file_path):
    """
    Process data from an Excel sheet
    """
    # Read the Excel file into a DataFrame
    data = pd.read_excel(file_path)
    return data
