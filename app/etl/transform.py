import pandas as pd
import logging

def transform_data(df):
    """Transforms the DataFrame by performing basic cleaning."""

    if df is None:
        logging.error("No data to transform.")
        return None

    try:

        # INFO BEFORE TRANSFORMATION
        logging.info("Starting data transformation")

        logging.info(f"Rows before cleaning: {len(df)}")

        logging.info(
            f"Duplicate rows: {df.duplicated().sum()}"
        )

        logging.info(
            f"Null values: {df.isna().sum().sum()}"
        )

        logging.info(f"\nColumn types before:\n{df.dtypes}")

        # WARNiNGS BEFORE TRANSFORMATION
        duplicates = df.duplicated().sum()

        if duplicates > 0:
            logging.warning(
                f"{duplicates} duplicate rows detected"
            )
        
        nulls = df.isna().sum().sum()

        if nulls > 0:
            logging.warning(
                f"{nulls} null values detected"
            )

        negative_sales = (df['Sales'] < 0).sum()

        invalid_order_dates = df['Order Date'].isna().sum()

        if invalid_order_dates > 0:
            logging.warning(
                f"{invalid_order_dates} invalid order dates found"
            )

        invalid_order_dates = df['Ship Date'].isna().sum()

        if invalid_ship_dates > 0:
            logging.warning(
                f"{invalid_ship_dates} invalid ship dates found"
            )

        if negative_sales > 0:
            logging.warning(
                f"{negative_sales} negative sales values found"
            )

        
        # TRANSFORMATION
    
        # REMOVE DUPLICATES
        df = df.drop_duplicates()

        # REMOVE NULLS
        df = df.dropna()

        # ROUND DECIMALS
        df['Sales'] = df['Sales'].round(2)
        df['Profit'] = df['Profit'].round(2)

        # DATE CONVERSION
        df['Order Date'] = pd.to_datetime(
            df['Order Date'],
            errors="coerce"
        )

        df['Ship Date'] = pd.to_datetime(
            df['Ship Date'],
            errors="coerce"
        )

        # NORMALIZE COLUMN(NAMES)
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )

         # SELECT COLUMNS
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
            "sub-category",
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

        logging.error(
            f"Error during data transformation: {e}"
        )

        return None

