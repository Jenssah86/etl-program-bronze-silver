from sqlalchemy import text

def is_file_processed(engine, file_name):
    result = engine.execute(
        text("SELECT COUNT(*) FROM processed_files WHERE file_name=:f"),
        {"f": file_name}
    ).scalar()

    return result > 0


def mark_file_processed(engine, file_name):
    engine.execute(
        text("INSERT INTO processed_files (file_name) VALUES (:f)"),
        {"f": file_name}
    )