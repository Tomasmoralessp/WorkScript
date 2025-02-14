from abc import ABC, abstractmethod
import pdfplumber

# TODO: Rewrite using hugging face pipelines 

class ProcessorTemplate(ABC):
    def __init__(self):
        self.pages = None  # Almacena las imágenes del PDF
        self.answers = []  # Almacena las respuestas del modelo
        self.stringified_text = None

        # Cargar modelos de Hugging Face
        self.qa_pipeline = None

    def convert_pdf_to_images(self, pdf_path):
        """ Convertir un PDF a imágenes """
        pass
    
    def convert_pdf_to_text(self, pdf_path):
        self.stringified_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                self.stringified_text += page.extract_text()

    
    def ask_question(self, question):
        """ Realizar preguntas sobre cada página del PDF """
        pass
    
    @abstractmethod
    def extract_information(self):
        """ Método abstracto para extraer información de las imágenes """
        pass
    
       