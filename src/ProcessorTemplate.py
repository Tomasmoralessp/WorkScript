from abc import ABC, abstractmethod
import pdfplumber

class ProcessorTemplate(ABC):
    def __init__(self):
        self.stringified_text = ""

    # TODO: CHANGE TO PREPROCESS
    def convert_pdf_to_text(self, pdf_path):
        self.stringified_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    cleaned_page = self.clean_text(page_text)
                    if cleaned_page is None:  # ⚠️ Evitar concatenar None
                        cleaned_page = ""  
                    self.stringified_text += cleaned_page  # ✅ Ahora siempre es str

    @abstractmethod
    def clean_text(self, text):
        """Limpia el texto eliminando encabezados y caracteres innecesarios"""
        pass
    
    @abstractmethod
    def format_df(self, dataframe):
        pass
    
    @abstractmethod
    def extract_information(self):
        """ Método abstracto para extraer información del texto """
        pass
    
       