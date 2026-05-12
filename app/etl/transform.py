import pandas as pd

def transform_data(df):
    """Transforms the DataFrame by performing basic cleaning and feature engineering."""
    if df is None:
        print("No data to transform.")
        return None
    
    try:
        # Example transformation: Fill missing values with the mean of each column
        df_filled = df.fillna(df.mean())
        
        # Example feature engineering: Create a new column that is the sum of two existing columns
        if 'column1' in df_filled.columns and 'column2' in df_filled.columns:
            df_filled['new_column'] = df_filled['column1'] + df_filled['column2']
        
        print("Data transformation successful.")
        return df_filled
    except Exception as e:
        print(f"Error during data transformation: {e}")
        return None
        