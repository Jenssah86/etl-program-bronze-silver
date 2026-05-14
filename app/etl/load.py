import logging

def load_to_mysql(df, engine):
    try:
        logging.info("Loading data into silver_orders")

        df.to_sql(
            "silver_orders",
            con=engine,
            if_exists="append",
            index=False
        )

        logging.info(f"{len(df)} records loaded into silver_orders")

    except Exception as e:
        logging.error(f"Load failed: {e}")