import regex as re
import pandas as pd

from src.ProcessorTemplate import ProcessorTemplate

class ArrivalsProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__()

    def clean_text(self, text):
        """Limpieza de texto para arrivals (implementar si es necesario)"""
        pass

    def format_df(self, dataframe):
        """Formateo del DataFrame (implementar si es necesario)"""
        pass

    def extract_information(self):
        if not self.pages:
            return "No hay imágenes cargadas. Ejecuta convert_pdf_to_text() primero."

        self.ask_question("Lista los huéspedes con su número de habitación, notas si existen, tipo de cliente, y cantidad a cobrar solo si es en efectivo.")
        
        if not self.answers:
            return "No se generaron respuestas del modelo."
        
        return {"huéspedes": self.answers}
        

class DeparturesProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__()

    
    def clean_text(self, text):
        # 1️⃣ Eliminar encabezados hasta la PRIMERA fecha que contenga más datos después
        clean_text = re.sub(r"^.*?(\d{2}/\d{2}/\d{4} lu\.)", r"\1", text, flags=re.DOTALL)

        # 2️⃣ Eliminar artefactos de texto con guiones bajos y caracteres extraños
        clean_text = re.sub(r"\b(?:_?[A-Za-z]{1,2}[_]+){2,}\b", "", clean_text)  # Palabras fragmentadas
        clean_text = re.sub(r"_{5,}", "", clean_text)  # Bloques de guiones bajos largos

        # 3️⃣ Normalizar espacios
        clean_text = re.sub(r"\s+", " ", clean_text).strip()

        return clean_text

    def format_df(self, dataframe):
        dataframe['name'] = dataframe['name'].str.upper()

        return dataframe


    def extract_information(self):
        """Extrae Arrival, Departure, Name y Room del texto limpio"""

        pattern = re.compile(
            r"(?:\d{2}/\d{2}/\d{4})\s*(?:\w{2}\.)?\s+"  # Ignora la fecha de llegada
            r"(?:\d{2}/\d{2}/\d{4})\s*(?:\w{2}\.)?\s+"  # Ignora la fecha de salida
            r"\d+\s+"  # Ignora el número de pasajeros
            r"(?P<name>[^\d\n]+?)\s+"  # Captura el nombre del titular de la reserva (hasta un número o salto de línea)
            r"(?:Unconfirmed|Owner usage|Transient Advance|Cash|international Payment).*?"  # Ignora detalles de pago
            r"(?P<room>\b(?:1A|10[1-9]|11[0-9]|12[0-5]|20[1-8])\b)",  # Captura el número de habitación
            re.MULTILINE  # 🔥 Permite búsqueda en todas las líneas
        )



        matches = pattern.finditer(self.stringified_text)
        data = []

        for match in matches:
            room_number = match.group("room")
            if room_number == "1A":
                room_number = "100"  # Mapear 1A como 100
            data.append({
                "name": match.group("name").strip(),
                "room_number": room_number,
            })

        df_departures = pd.DataFrame(data)
        df_departures = self.format_df(df_departures)
        

        return df_departures

        

class RoomReportProcessor(ProcessorTemplate):
    def __init__(self):
        super().__init__()

    def clean_text(self, text):
        # 1.A Busca cualquier secuencia de 5 o más guiones y los sustituye con ""
        clean_text = re.sub(r"_{5,}", "", text)

        # 1.B Se elimina todo desde la coincidencia de Playa Amadores hasta el primer salto de línea
        clean_text = re.sub(r"Playa Amadores.*?\n","", clean_text, flags=re.DOTALL) # Así .*? puede capturar incluso varias líneas

        # 1.C Eliminación de la fecha  con formato dd/mm/yyyy
        clean_text = re.sub(r"Date: \d{2}/\d{2}/\d{4}.*?\n", "", clean_text)

        # 1.D Eliminación de la numeración de Página 
        clean_text = re.sub(r"Page: \d+", "", clean_text)

        # 1.E Normalización de espacios
        clean_text = re.sub(r"\s+", " ", clean_text).strip()
        return clean_text
    
    def format_df(self, dataframe):
        dataframe['name'] = dataframe['name'].str.split().str[::-1].str.join(' ').str.upper()
        return dataframe

    def extract_information(self):
        """ Process stringified pdf and  returns the desired data as a list o"""
        # Here I have to implement reg expression to extract the desired information 
        # Desiref Information: room_number, name, arr_date, dep_date

       

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

        pattern = re.compile(
            r"(?P<room>\d+A?)\s+"  # Captura la habitación (Ej: 101, 1A, 203)
            r"(?:2 BR Private Pool|1 BR Suite|2 BR Courtyard|2 BR Jacuzzi)\s+"  # Captura la categoría de la habitación
            r"(?P<names>[^\d]+?)\s+"  # Captura el primer nombre (evita números que podrían indicar fechas)
            r"(?P<arrival>\d{2}/\d{2}/\d{4})\s+"  # Captura la fecha de llegada
            r"(?P<departure>\d{2}/\d{2}/\d{4})"  # Captura la fecha de salida
        )



        # 3. Aplicar el regex al texto limpio
        matches = pattern.finditer(self.stringified_text)

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
        
        df_roomreport = pd.DataFrame(data)
        df_roomreport = self.format_df(df_roomreport)

        # 5. Devolver data
        return df_roomreport
        
    

