from abc import ABC, abstractmethod
import pdfplumber

class ProcessorTemplate(ABC):
    def __init__(self):
        self.stringified_text = ""

        # Cargar modelos de Hugging Face
        self.qa_pipeline = None

    def convert_pdf_to_images(self, pdf_path):
        """ Convertir un PDF a imágenes """
        pass
    
    def convert_pdf_to_text(self, pdf_path):
        self.stringified_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    cleaned_page = self.clean_text(page_text)
                    self.stringified_text += cleaned_page 
    @abstractmethod
    def clean_text(self, text):
        """Limpia el texto eliminando encabezados y caracteres innecesarios"""
        pass
    
    @abstractmethod
    def format_df(self, dataframe):
        pass

    
    def ask_question(self, question):
        """ Realizar preguntas sobre cada página del PDF """
        pass
    
    @abstractmethod
    def extract_information(self):
        """ Método abstracto para extraer información de las imágenes """
        pass
    
       