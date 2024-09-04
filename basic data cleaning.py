import pandas as pd
import numpy as np

# Function for Checking NULL Counts and NULL Percentages
# ======================================================

def check_null(df):
    """
    This function calculates the count and percentage of null values in a given DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame for which to calculate null values.
    
    Returns:
    pandas.DataFrame: A DataFrame containing two columns: 'Null_Count' and 'Null_Percentage'. 
                     The DataFrame is filtered to show only rows where Null_Count > 0.
    """
    
    null_counts = pd.DataFrame(df.isnull().sum(), columns=['Null_Count'])
    null_percentage = pd.DataFrame(round((df.isnull().sum()/len(df))*100, 2), columns=['Null_Percentage'])
    
    # Combining the two dataframes
    null_info = pd.concat([null_counts, null_percentage], axis = 1)

    # Filtering to show only rows where Null_Count > 0
    null_info = null_info[null_info['Null_Count'] > 0]
    
    return null_info


