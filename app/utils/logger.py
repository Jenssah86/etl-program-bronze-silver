import logging
from pathlib import Path

# locatie logbestand om naar toe te schrijven
LOG_FILE = Path(__file__).resolve().parents[2] / "logs" / "app.log"

# Configure logging
logging.basicConfig( 
    filename=LOG_FILE, # Logbestand in de hoofdmap van het project
    level=logging.INFO, # Logniveau instellen op INFO (kan worden aangepast naar DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s" # Logberichtformaat: tijdstempel - logniveau - bericht
)

logging.info("Logger gestart")