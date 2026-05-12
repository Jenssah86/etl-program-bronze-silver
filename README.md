Python ETL program

In dit project maken we een klein programmatje in Python welke een ETL proces uitvoert voor specifieke CSV-bestanden van een dataset van een bedrijf. Het moet de data opschonen/transformeren en vervolgens wegschrijven naar mySQL-server (XAMPP, lokaal)
Dit zetten we in een UI zodat een eindgebruiker dit proces zelf kan uitvoeren.

Architectuur:

[CSV Bestanden]
        ↓
[Python GUI Applicatie]
        ↓
[ETL Proces]
  - Extract
  - Transform
  - Load
        ↓
[MySQL Database (XAMPP)]
