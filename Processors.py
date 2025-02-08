from ProcessorTemplate import ProcessorTemplate

class ArrivalsProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre

    def extract_information(self):
        if not self.pages:
            return "No hay imágenes cargadas. Ejecuta convert_pdf_to_images() primero."

        # Realizar la pregunta
        self.ask_question("Lista los huéspedes con su número de habitación, notas si existen, tipo de cliente, y cantidad a cobrar solo si es en efectivo.")
        
        # Manejar el caso en que no haya respuestas
        if not self.answers:
            return "No se generaron respuestas del modelo."
        
        # Devolver resultados estructurados
        return {"huéspedes": self.answers}
