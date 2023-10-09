import pandas as pd

def read_excel(file_path, lab_no, header=[0,1], fn_col='FN', ln_col='LN', total_col='Total'):
    """
    Reads an Excel file and returns a dictionary of student names and their corresponding total marks.
    This function is specifically formatted for CPSC 121 Lab Marksheets as of 9 Oct 2022, and needs to be updated in case of any changes to how marksheets are formatted.

    Args:
    - file_path (str): The path to the Excel file.
    - lab_no (int): The number of the sheet to read.
    - header (list): A list of row numbers to use as the column names. Default is [0,1].
    - fn_col (str): The name of the column containing the first name of the student. Default is 'FN'.
    - ln_col (str): The name of the column containing the last name of the student. Default is 'LN'.
    - total_col (str): The name of the column containing the total marks of the student. Default is 'Total'.

    Returns:
    - A dictionary of student names and their corresponding total marks for the lab.
    """

    lab_title = f"Lab {lab_no}" # The title of the lab sheet: 'Lab 1', 'Lab 2', etc.

    df = pd.read_excel(file_path, sheet_name=lab_title, header=header)

    names = df[lab_title, ln_col] + ', ' + df[lab_title, fn_col] # formats names to canvas format ("LN, FN")
    # name_col = df[lab_title][fn_col] + ' ' + df[lab_title][ln_col]
    totals = find_total_col(total_col, df)
 
    return dict(zip(names, totals))

def find_total_col(total_col, df): # Returns column full of total marks
    for colname in df.columns.values:
        if total_col in colname:
                return  df[colname].iloc[:, 0]
        for subcolname in colname:
            if total_col in subcolname:
                return df[colname]
    

