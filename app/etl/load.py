import logging  # logging voor ETL monitoring (load status, success/failure)

def load_to_mysql(df, engine):
    try:
        logging.info("Loading data into silver_orders")  # start van load stap

        df.to_sql(
            "silver_sales_orders",  # target table in MySQL (silver layer)
            con=engine,       # SQLAlchemy engine connection
            if_exists="append",  # append zodat nieuwe batches toegevoegd worden (no overwrite)
            index=False       # voorkomt dat pandas index als kolom wordt weggeschreven
        )

        logging.info(f"{len(df)} records loaded into silver_orders")  # aantal geladen rijen voor tracking

    except Exception as e:
        logging.error(f"Load failed: {e}")  # foutmelding bij database of insert issues