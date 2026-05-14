import pandas as pd

file_path = "../../bronze/superstore_batch_1.csv" # tijdelijk voor testen, gaat later via UI binnenkomen

def read_csv(file_path):
    """Reads a CSV file and returns a DataFrame."""

    try:
        df = pd.read_csv(file_path, encoding="latin1")
        print(f"Successfully read {file_path}")

        return df

    except Exception as e:

        print(f"Error reading {file_path}: {e}")

        return None

        print("Extract module loaded successfully.")
    