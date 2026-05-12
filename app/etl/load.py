def load_to_mysql(df, table_name, engine):
    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"Data loaded to MySQL table '{table_name}' successfully.")