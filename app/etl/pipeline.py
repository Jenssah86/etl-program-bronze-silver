from extract import read_csv_file
from transform import transform_data
from load import load_to_mysql

def run_pipeline(file_path, engine):
    df = read_csv_file(file_path)

    df = transform_data(df)

    load_to_mysql(df, "orders", engine)