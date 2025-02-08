from Processors import ArrivalsProcessor

# Ruta al PDF de prueba
pdf_path = "arrivals.pdf"

# Crear una instancia del procesador
processor = ArrivalsProcessor()

# Convertir PDF a imágenes
print("Convirtiendo PDF a imágenes...")
processor.convert_pdf_to_images(pdf_path)
print("Conversión completada.")

# Extraer información
print("Extrayendo información...")
result = processor.extract_information()

# Mostrar resultado
print("Resultados:")
print(result)
