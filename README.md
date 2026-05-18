# **Bronze → Silver ETL Tool**





!\[afbeelding](./image/1.png)





**Beschrijving:**

Desktop ETL applicatie gebouwd in Python voor het verwerken van Bronze CSV data naar een opgeschoonde Silver layer in MySQL.





**Features:**

* CSV upload via GUI
* ETL verwerking
* Data cleaning
* Logging
* Incremental loading
* MySQL integratie
* EXE distributie





**Technologieën:**

* Python
* Pandas
* Tkinter
* SQLAlchemy
* MySQL
* PyInstaller





**Installatie:**



pip install -r requirements.txt







**Starten van applicatie:**



python app/main.py





**EXE Build:**



pyinstaller --onefile --windowed --clean --name etl\_bronze\_silver\_v1 --icon app/assets/logo.ico --add-data "app/assets/company\_logo.png;assets" --add-data "app/assets/logo.ico;assets" app/main.py





**Architectuurdiagram:**



┌──────────────────────┐

│   **Bronze CSV Files**           │

└──────────┬───────────┘

&#x20;          │

&#x20;          ▼

┌──────────────────────┐

│      **Extract.py**              │

└──────────┬───────────┘

&#x20;          │

&#x20;          ▼

┌──**────────────────────┐**

**│    Transform.py              │**

**│  Cleaning \& Logging**          │

└──────────┬───────────┘

&#x20;          │

&#x20;          ▼

┌──────────────────────┐

│       **Load.py                │**

**│  MySQL Silver Table**          │

└──────────┬───────────┘

&#x20;          │

&#x20;          ▼

┌──────────────────────┐

│  **processed\_files             │**

**│ Incremental Loading**          │

└──────────────────────┘















