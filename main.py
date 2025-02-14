from Processors import ArrivalsProcessor, DeparturesProcessor, RoomReportProcessor

# Ruta al PDF de prueba
arrivals = "arrivals.pdf"
departures = "departures.pdf"
roomreport = "roomreport.pdf"

# Crear una instancia del procesador
processor = RoomReportProcessor()
processor.convert_pdf_to_text(roomreport)
print(processor.extract_information())