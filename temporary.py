import pandas as pd

from src.ProcessorFactory import ProcessorFactory
from src.FinalReport import FinalReport

# ✅ Definir los datos de df_arrivals correctamente
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
            "Change": {"from": 123, "to": 118, "date": "01/02/2025"}  # ✅ Cambio de habitación
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
            "Change": None  # ✅ No cambia de habitación
        }
    }
])

# ✅ Crear df_roomreport correctamente
df_roomreport = pd.DataFrame([
    {"name": "Patricia Hogan", "room_number": 123},
    {"name": "Alberto LaCabra", "room_number": 540}
])

# ✅ Crear df_departures correctamente
df_departures = pd.DataFrame([
    {"name": "Perico Hogan", "room_number": 500},
    {"name": "La LaCabra", "room_number": 800}
])

# ✅ Crear el diccionario con los DataFrames procesados
processed_data = {
    'arrivals': df_arrivals,
    'departures': df_departures,
    'roomreport': df_roomreport
}

# ✅ Inicializar la clase
report = FinalReport(processed_data)

# ✅ Ejecutar la lógica para determinar cambios y estancias
report.guess_status_logic()

# ✅ Generar el Excel con las habitaciones
report.generate_excel()

# ✅ Generar las tarjetas HTML de clientes
report.generate_cards()

print("✅ Reporte generado exitosamente.")
