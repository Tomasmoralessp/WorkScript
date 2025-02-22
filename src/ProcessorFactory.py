from src.Processors import DeparturesProcessor, RoomReportProcessor, ArrivalsProcessor

class ProcessorFactory():
  def __init__(self, pdf_files, process_arrivals=True):
    """ 
    pdf_files: Diccionario con los archivos pdf a procesar.
    Formato esperado:
      'arrivals': 'arrivals.pdf',
      'departures': 'departures.pdf',
      'roomreport': 'roomreport.pdf'
    """
    self.pdf_files = pdf_files
    self.processors = {
            'departures': DeparturesProcessor(),
            'roomreport': RoomReportProcessor()
        }
    if process_arrivals:
          self.processors['arrivals'] = ArrivalsProcessor()

    # Aquí se almacenarán los distintos dataframes resultantes
    self.results = {}

  def run_processors(self):
    """
    Ejecutar cada procesador con su respectivo PDF y almacena los resultados .
    """
    for key, processor in self.processors.items():
      if key in self.pdf_files: # Se verifica que haya un archivo para el procesador

        # 1. Extrae la información del PDF en el formato adecuado
        # TODO: ARRIVALS? 
        # WRAP WITH PREPROCESSOR 
        processor.convert_pdf_to_text(self.pdf_files[key]) 

        # 2. Se extrae la información
        self.results[key] = processor.extract_information()
    
    # Devuelve los dataframes ya formateados
    return self.results 


