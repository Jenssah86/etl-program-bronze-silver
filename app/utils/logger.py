import logging

# Configure logging
logging.basicConfig( 
    filename="app.log", # Logbestand in de hoofdmap van het project
    level=logging.INFO, # Logniveau instellen op INFO (kan worden aangepast naar DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s" # Logberichtformaat: tijdstempel - logniveau - bericht
)

logging.info("Logger gestart")