from src.FinalReport import FinalReport
from src.Processors import ProcessorFactory

#  Diccionario con las rutas de los archivos PDF
pdf_files = {
    "arrivals": "data/arrivals.pdf",
    "departures": "data/departures.pdf",
    "roomreport": "data/roomreport.pdf"
}

# Inicializar la fábrica de procesadores
factory = ProcessorFactory(pdf_files)

# Ejecutar los procesadores y obtener los DataFrames procesados
processed_data = factory.run_processors()

# Pasar los datos procesados a FinalReport
final_report = FinalReport(processed_data)

# Aplicar lógica de status
final_report.guess_status_logic()

# Generar los reportes finales
final_report.generate_excel()
final_report.generate_cards()
