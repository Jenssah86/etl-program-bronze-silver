from sqlalchemy import text

# controleren of input bestand al eerder verwerkt is
def is_file_processed(engine, file_name):

    # Open database connectie
    with engine.connect() as connection:

        result = connection.execute(
            text(
                """
                SELECT COUNT(*)
                FROM silver_processed_files
                WHERE file_name = :f
                """
            ),
            {"f": file_name}
        ).scalar()

    return result > 0

# markeert het input bestand als verwerkt
def mark_file_processed(engine, file_name):

    # Open database transactie
    with engine.begin() as connection:

        connection.execute(
            text(
                """
                INSERT INTO silver_processed_files (file_name)
                VALUES (:f)
                """
            ),
            {"f": file_name}
        )