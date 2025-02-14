import regex as re

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

class DeparturesProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__() # Llamar al constructor de la clase padre
    def extract_information(self):
        # Here I have to implement reg expression to extract the desired information 
        # Desired Information: room_number, name, arr_date, dep_date



        # 1. Limpieza del texto eliminando encabezados y guiones

        # 1.A Busca cualquier secuencia de 5 o más guiones y los sustituye con ""
        clean_text = re.sub(r"_{5,}", "", self.stringified_text)

        # 1.B Se elimina todo desde la coincidencia de Playa Amadores hasta el primer salto de línea
        clean_text = re.sub(r"Playa Amadores.*?\n","", clean_text, flags=re.DOTALL) # Así .*? puede capturar incluso varias líneas

        # 1.C Eliminación de la fecha  con formato dd/mm/yyyy
        clean_text = re.sub(r"Date: \d{2}/\d{2}/\d{4}/.*?\n", "", clean_text)

        # 1.D Eliminación de la numeración de Página 
        clean_text = re.sub(r"Page: \d+", "", clean_text)

        # 1.E Normalización de espacios
        clean_text = re.sub(r"\s+", "", clean_text).strip()

        return clean_text


class RoomReportProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__()
    
    def extract_information(self):
        """ Process stringified pdf and  returns the desired data as a list o"""
        # Here I have to implement reg expression to extract the desired information 
        # Desiref Information: room_number, name, arr_date, dep_date

        # 1. Limpieza del texto eliminando encabezados y guiones

        # 1.A Busca cualquier secuencia de 5 o más guiones y los sustituye con ""
        clean_text = re.sub(r"_{5,}", "", self.stringified_text)

        # 1.B Se elimina todo desde la coincidencia de Playa Amadores hasta el primer salto de línea
        clean_text = re.sub(r"Playa Amadores.*?\n","", clean_text, flags=re.DOTALL) # Así .*? puede capturar incluso varias líneas

        # 1.C Eliminación de la fecha  con formato dd/mm/yyyy
        clean_text = re.sub(r"Date: \d{2}/\d{2}/\d{4}.*?\n", "", clean_text)

        # 1.D Eliminación de la numeración de Página 
        clean_text = re.sub(r"Page: \d+", "", clean_text)

        # 1.E Normalización de espacios
        clean_text = re.sub(r"\s+", " ", clean_text).strip()


        # 2. Aplicar la expresión regular para extraer la información deseada
        
        # 2.1 (?P<room>....) asigna el nombre room a este grupo para poder acceder a él fácilmente
        # \d+ --> Captura uno o más dígitos
        # [A-Z] captura opcionalmente una letra mayúscula 

        # 2.2 \s+ para capturar los espacios entre el número de habitación y categoría (no importe el número de espacios el regex funcione)

        # 2.3 (?: ) grupo no capturador no se guarda en resultados sólo sirve para hacer la búsqueda

        # 2 BR Private Pool | 1 BR Suite | 2 BR Courtyard | 2 BR Jacuzzi -> captura la categoría de la habitación 

        # 2.4 \s+(?P<names>.+?)\s+ -> Captura los nombres de los huéspedes
        # \s+ -> Captura los espacios entre la categoría de habitación y el primer nombre
        # (?P<names>.+?) -> Captura de manera perzosa todos los caracteres posibles del nombre

        # 2.5 Capturar la fecha de llegada
        # (?P<arrival>\d{2}/\d{2}/d{4})\s+

        # 2.6 Capturar la fecha de salida
        # (?P<departure>\d{2}/\d{2}/d{4})

        pattern = re.compile(r"(?P<room>\d+[A-Z]?)\s+(?:2 BR Private Pool|1 BR Suite|2 BR Courtyard|2 BR Jacuzzi)\s+(?P<names>.+?)\s+(?P<arrival>\d{2}/\d{2}/\d{4})\s+(?P<departure>\d{2}/\d{2}/\d{4})")


        # 3. Aplicar el regex al texto limpio
        matches = pattern.finditer(clean_text)

        # 4. Almacenar los datos extraídos
        data = []

        for match in matches:
            room_number = match.group("room")
            if room_number == "1A":
                room_number = "100" # Manejar el caso de la 100 directamente
            name = match.group("names").strip()
            arr_date = match.group("arrival")
            dep_date = match.group("departure")
            data.append({"name": name, "room_number": room_number, "arr_date": arr_date, "dep_date": dep_date})

        
        return data
        
    

