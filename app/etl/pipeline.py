import logging
from etl.extract import read_csv
from etl.transform import transform_data
from etl.load import load_to_mysql
from etl.file_tracker import (is_file_processed,mark_file_processed)

def run_pipeline(file_path, file_name, engine):

    if is_file_processed(engine, file_name):
        logging.info(f"Skipping already processed file: {file_name}")
        return

    try:
        logging.info(f"Processing file: {file_name}")

        # ======================
        # 1. EXTRACT
        # ======================
        df = read_csv(file_path)

        if df is None:
            logging.error("Extract failed - no data loaded")
            return

        # ======================
        # 2. TRANSFORM
        # ======================
        df_clean = transform_data(df)

        if df_clean is None:
            logging.error("Transform failed - skipping load")
            return

        # ======================
        # 3. LOAD
        # ======================
        load_to_mysql(df_clean, engine)

        # ======================
        # 4. TRACK FILE
        # ======================
        mark_file_processed(engine, file_name)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")