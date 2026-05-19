import pandas as pd  # gebruikt voor data cleaning en DataFrame manipulatie
import logging  # logging voor ETL monitoring (info, warning, error)

def transform_data(df):
    """Transforms the DataFrame by performing basic cleaning."""

    if df is None:
        logging.error("No data to transform.")  # ETL stop als extract faalt
        return None

    try:

        # INFO BEFORE TRANSFORMATION
        logging.info("Starting data transformation")

        logging.info(f"Rows before cleaning: {len(df)}")

        logging.info(f"Duplicate rows: {df.duplicated().sum()}")

        logging.info(f"Null values: {df.isna().sum().sum()}")

        logging.info(f"\nColumn types before:\n{df.dtypes}")

        # WARNINGS BEFORE TRANSFORMATION (data quality checks)
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            logging.warning(f"{duplicates} duplicate rows detected")

        nulls = df.isna().sum().sum()
        if nulls > 0:
            logging.warning(f"{nulls} null values detected")

        negative_sales = (df['Sales'] < 0).sum()
        if negative_sales > 0:
            logging.warning(f"{negative_sales} negative sales values found")

        invalid_order_dates = df['Order Date'].isna().sum()  # check voor invalid datums vóór cleaning
        if invalid_order_dates > 0:
            logging.warning(f"{invalid_order_dates} invalid order dates found")

        invalid_ship_dates = df['Ship Date'].isna().sum()  # check voor invalid ship dates vóór cleaning
        if invalid_ship_dates > 0:
            logging.warning(f"{invalid_ship_dates} invalid ship dates found")

        
        # TRANSFORMATION STEP (data cleaning + standaardisatie)

        df = df.drop_duplicates()  # verwijdert dubbele rijen
        df = df.dropna()  # verwijdert rijen met null values

        df['Sales'] = df['Sales'].round(2)  # afronden van numerieke kolom
        df['Profit'] = df['Profit'].round(2)

        df['Order Date'] = pd.to_datetime(df['Order Date'], errors="coerce")  # datum parsing met foutafhandeling
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors="coerce")

        # NORMALIZE COLUMN NAMES (standaard ETL best practice)
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )

        # SELECT COLUMNS (Silver layer schema)
        df = df[[
            "order_id",
            "order_date",
            "ship_date",
            "customer_id",
            "customer_name",
            "country",
            "city",
            "region",
            "product_id",
            "product_name",
            "category",
            "sub_category",  # fixed: moet underscore zijn na normalization
            "sales",
            "quantity",
            "discount",
            "profit"
        ]]

        # INFO AFTER TRANSFORMATION
        logging.info(f"Rows after cleaning: {len(df)}")

        logging.info(f"\nColumn types after:\n{df.dtypes}")

        logging.info("Data transformation successful.")

        return df

    except Exception as e:
        logging.error(f"Error during data transformation: {e}")  # logging van volledige ETL error
        return None