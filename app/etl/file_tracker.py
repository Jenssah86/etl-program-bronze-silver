from sqlalchemy import text  # gebruikt voor veilige SQL queries met parameters (voorkomt SQL injection)

def is_file_processed(engine, file_name):
    # controleert of een bestand al eerder is verwerkt (incremental ETL check)
    result = engine.execute(
        text("SELECT COUNT(*) FROM silver_processed_files WHERE file_name=:f"),  # zoekt file in tracking tabel
        {"f": file_name}  # parameter binding voor veilige query uitvoering
    ).scalar()  # haalt 1 enkele waarde op (COUNT result)

    return result > 0  # True = al verwerkt, False = nog niet verwerkt


def mark_file_processed(engine, file_name):
    # registreert dat een bestand succesvol verwerkt is
    engine.execute(
        text("INSERT INTO silver_processed_files (file_name) VALUES (:f)"),  # slaat filename op in tracking tabel
        {"f": file_name}  # parameter binding voor veiligheid en stabiliteit
    )