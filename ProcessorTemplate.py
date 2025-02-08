from abc import ABC, abstractmethod
from pdf2image import convert_from_path
from transformers import pipeline
from PIL import Image

# TODO: Rewrite using hugging face pipelines 

class ProcessorTemplate(ABC):
    def __init__(self):
        self.pages = None  # Almacena las imágenes del PDF
        self.answers = []  # Almacena las respuestas del modelo

        # Cargar modelos de Hugging Face
        self.qa_pipeline = pipeline("document-question-answering", model="impira/layoutlm-document-qa")

    def convert_pdf_to_images(self, pdf_path):
        """ Convertir un PDF a imágenes """
        self.pages = convert_from_path(pdf_path)
        if not self.pages:
            raise ValueError(f"No se pudieron convertir las imágenes del PDF: {pdf_path}")
    
    def ask_question(self, question):
        """ Realizar preguntas sobre cada página del PDF """
        if not self.pages:
            raise ValueError("No se han convertido las imágenes del PDF")

        self.answers = []
        for i, page in enumerate(self.pages):
            answer = self.qa_pipeline(image=page, question=question)
            response = answer[0]["answer"] if answer else "No se encontró una respuesta."
            self.answers.append(response)
    
    @abstractmethod
    def extract_information(self):
        """ Método abstracto para extraer información de las imágenes """
        pass
    
       