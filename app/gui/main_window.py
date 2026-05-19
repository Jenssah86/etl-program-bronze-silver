# GUI framework
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# Bestands- en pad handling
from pathlib import Path
import os, sys

# Afbeeldingen laden voor GUI (logo + icoon)
from PIL import Image, ImageTk

# ETL pipeline en database engine
from etl.pipeline import run_pipeline
from database.connection import engine

# ============================================================
# APP DIRECTORY (Voor logbestand)
# ============================================================
def app_dir():
    # In PyInstaller: directory van de .exe
    if hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)

    # Tijdens development: directory van dit script
    return os.path.dirname(os.path.abspath(__file__))

# ============================================================
# LOGGING CONFIGURATIE (centrale logger voor GUI + ETL)
# ============================================================
import logging

# Logbestand in dezelfde map als de .exe of het script
LOG_FILE = os.path.join(app_dir(), "app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()  # handig tijdens development
    ]
)

logging.info("Logger gestart")

# ============================================================
#  RESOURCE PATH (PyInstaller)
#  Zorgt ervoor dat assets (icoon, logo) ook werken in .exe
# ============================================================
def resource_path(relative_path):
    # PyInstaller pakt bestanden tijdelijk in sys._MEIPASS
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    # Tijdens development: normale pad structuur gebruiken
    return os.path.join(os.path.abspath("."), relative_path)


# ============================================================
#  APP DIRECTORY (BELANGRIJK VOOR LOGGING)
#  In Python → projectmap
#  In .exe → map waar de .exe staat
# ============================================================
def app_dir():
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller: directory van de .exe
        return os.path.dirname(sys.executable)
    else:
        # Development: directory van dit script
        return os.path.dirname(os.path.abspath(__file__))


# Absoluut pad naar logbestand
LOG_FILE = os.path.join(app_dir(), "app.log")


# ============================================================
#  MAIN WINDOW INITIALISATIE
# ============================================================
root = tk.Tk()
root.title("Bronze to Silver ETL Tool")
root.geometry("700x500")

# Icoon in taakbalk / window header
root.iconbitmap(resource_path("assets/logo.ico"))

# Houdt geselecteerd bestand globaal bij
selected_file = None


# ============================================================
#  LOGGING HELPER
#  Schrijft naar zowel GUI als app.log
# ============================================================
def write_log(message):
    # Naar GUI
    log_box.insert(tk.END, message + "\n")

    # Naar centrale logger
    logging.info(message)

# ============================================================
#  BESTAND SELECTEREN
# ============================================================
def select_file():
    global selected_file

    # Open file dialog voor CSV selectie
    file_path = filedialog.askopenfilename(
        title="Selecteer CSV bestand",
        filetypes=[("CSV Files", "*.csv")]
    )

    # Als gebruiker een bestand kiest
    if file_path:
        selected_file = file_path

        # Update UI status
        status_label.config(text=f"Geselecteerd: {Path(file_path).name}")

        # Log naar GUI + bestand
        write_log(f"Geselecteerd bestand: {file_path}")


# ============================================================
#  ETL STARTEN
# ============================================================
def start_etl():
    global selected_file

    # Controle: geen bestand = stop
    if not selected_file:
        status_label.config(text="Geen bestand geselecteerd")
        write_log("Geen bestand geselecteerd")
        return

    try:
        # Bestandsnaam extraheren
        file_name = Path(selected_file).name

        # UI feedback start proces
        status_label.config(text="ETL pipeline aan het draaien...")
        write_log(f"ETL gestart voor {file_name}")

        # Pipeline uitvoeren (bron → silver laag)
        run_pipeline(selected_file, file_name, engine)

        # Succes feedback
        status_label.config(text="ETL proces succesvol voltooid")
        write_log("ETL proces succesvol voltooid")

    except Exception as e:
        # Foutafhandeling + logging
        status_label.config(text="ETL proces gefaald")
        write_log(f"Fout: {e}")


# ============================================================
#  UI OPBOUW (MAIN APP)
# ============================================================
def run_app():
    global status_label
    global log_box

    # -------------------------
    # HEADER CONTAINER
    # -------------------------
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)

    # -------------------------
    # LOGO LADEN (PyInstaller safe)
    # -------------------------
    logo_path = resource_path("assets/company_logo.png")

    # Afbeelding openen en schalen
    logo = Image.open(logo_path)
    logo = logo.resize((100, 100), Image.LANCZOS)

    # Belangrijk: referentie bewaren anders verdwijnt image
    root.logo_image = ImageTk.PhotoImage(logo)

    # Logo in UI plaatsen
    logo_label = tk.Label(header_frame, image=root.logo_image)
    logo_label.grid(row=0, column=0, padx=10)

    # -------------------------
    # TITEL
    # -------------------------
    title_label = tk.Label(
        header_frame,
        text="Bronze → Silver ETL Tool",
        font=("Arial", 18, "bold")
    )
    title_label.grid(row=0, column=1, sticky="w")

    # -------------------------
    # BESTAND UPLOAD KNOP
    # -------------------------
    select_button = tk.Button(
        root,
        text="Upload CSV-bestand",
        command=select_file, # hierdoor start de functie select_file()
        width=20,
        height=2
    )
    select_button.pack(pady=10)

    # -------------------------
    # ETL START KNOP
    # -------------------------
    run_button = tk.Button(
        root,
        text="Draai ETL proces",
        command=start_etl, # hierdoor start de functie start_etl()
        width=20,
        height=2
    )
    run_button.pack(pady=10)

    # -------------------------
    # STATUS LABEL (live feedback)
    # -------------------------
    status_label = tk.Label(root, text="Wachtend op bestand...", fg="blue")
    status_label.pack(pady=10)

    # -------------------------
    # LOG OUTPUT VENSTER
    # -------------------------
    log_box = ScrolledText(root, width=80, height=15)
    log_box.pack(pady=10)

    # Start GUI event loop
    root.mainloop()
