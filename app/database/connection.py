from sqlalchemy import create_engine  # SQLAlchemy wordt gebruikt om verbinding te maken met MySQL via Python

DB_USER = 'root'         # database user (standaard XAMPP user)
DB_PASSWORD = ''         # wachtwoord (leeg bij standaard XAMPP setup)
DB_HOST = 'localhost'    # lokale database server
DB_PORT = '3306'         # standaard MySQL poort
DB_NAME = 'superstore'   # database naam waarin je ETL data wordt opgeslagen

engine = create_engine(
    f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)  # maakt SQLAlchemy engine aan die gebruikt wordt voor alle database inserts/queries

print("Database connection established successfully.")  # bevestiging dat connectie werkt