import pandas as pd  # pandas wordt gebruikt voor het inlezen en verwerken van CSV-data

file_path = "../../bronze/superstore_batch_1.csv"  # tijdelijke testpad (later vervangen door UI input)

def read_csv(file_path):
    """Reads a CSV file and returns a DataFrame."""

    try:
        df = pd.read_csv(file_path, encoding="latin1")  # encoding latin1 voorkomt decode errors bij speciale tekens
        print(f"Successfully read {file_path}")  # bevestiging dat bestand correct is ingelezen

        return df  # dataframe teruggeven aan pipeline

    except Exception as e:
        print(f"Error reading {file_path}: {e}")  # foutmelding als CSV niet ingelezen kan worden
        return None  # None teruggeven zodat pipeline dit kan afvangen

# LET OP: deze print staat buiten functie en wordt altijd uitgevoerd bij import
print("Extract module loaded successfully.")