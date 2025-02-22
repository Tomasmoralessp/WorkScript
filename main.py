import pandas as pd
from src.ProcessorFactory import ProcessorFactory
from src.FinalReport import FinalReport

# 📌 PASO 1: Definir los archivos PDF
pdf_files = {
    "arrivals": "data/arrivals.pdf",
    "departures": "data/departures.pdf",
    "roomreport": "data/roomreport.pdf"
}

# 📌 PASO 2: Definir `df_arrivals` MANUALMENTE (Opcional)
df_arrivals = pd.DataFrame([
    {
        "name": "Patricia Hogan",
        "room_number": 118,
        "guest_type": "Owner usage",
        "arr_date": "01/02/2025",
        "dep_date": "08/02/2025",
        "am_to_pay": 0.00,
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": "14:00",
            "Guest_Of_Owner": True,
            "Toppers": True,
            "Blankets": True,
            "Others": "",
            "Change": {"from": 123, "to": 118, "date": "01/02/2025"}
        }
    },
    {
        "name": "Hans Berre",
        "room_number": 200,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "05/02/2025",
        "am_to_pay": 850.00,
        "notes": {
            "Baby_Cot": True,
            "High_Chair": True,
            "Hour_Of_Arrival": "21:00",
            "Guest_Of_Owner": True,
            "Toppers": False,
            "Blankets": True,
            "Others": "",
            "Change": None
        }
    }
])

# 📌 PASO 3: Ejecutar la lógica
factory = ProcessorFactory(pdf_files, process_arrivals=False)
processed_data = factory.run_processors()

# 📌 PASO 4: Sustituir `df_arrivals` solo si se proporciona manualmente
if df_arrivals is not None:
    processed_data["arrivals"] = df_arrivals

# 📌 PASO 5: Generar el reporte final
final_report = FinalReport(processed_data)
final_report.guess_status_logic()
final_report.generate_excel()
final_report.generate_cards()

print("✅ Reporte generado exitosamente.")
