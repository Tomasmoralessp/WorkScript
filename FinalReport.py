# Constantes para idear la lógica 
import pandas as pd

arrivals = [
    {"name": "Sonny Hansen", "room_number": 101, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Gail Pamela Oswald", "room_number": 208, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Ann-Kristin Brudvik", "room_number": 201, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "General", "am_to_pay": 1396.50},
    {"name": "Per Jensen", "room_number": 106, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Patricia Hogan", "room_number": 118, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Frank Kjelsvik", "room_number": 107, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "05/02/2025", "notes": "General", "am_to_pay": 758.50},
    {"name": "Astrid Naess", "room_number": 114, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "General", "am_to_pay": 1265.41},
    {"name": "Jan Erik Karlsen", "room_number": 102, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Karl Ingvar Mikael Mårtensson", "room_number": 105, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Arve Fjeld", "room_number": 124, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
    {"name": "Natalia Zielinska", "room_number": 202, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "04/02/2025", "notes": "General", "am_to_pay": 486.00},
    {"name": "Olava Åmlid Breiland", "room_number": 111, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "General", "am_to_pay": 945.00},
    {"name": "Jesper Brochmann", "room_number": 204, "guest_type": "Transient", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "General", "am_to_pay": 1033.20},
    {"name": "Beverley Yates", "room_number": 203, "guest_type": "Owner usage", "arr_date": "01/02/2025", "dep_date": "08/02/2025", "notes": "No Charge", "am_to_pay": 0.00},
]


departures = [
    {"name": "Sonny Hansen", "room_number": 101},
    {"name": "Gail Pamela Oswald", "room_number": 208},
    {"name": "Ann-Kristin Brudvik", "room_number": 201},
    {"name": "Per Jensen", "room_number": 106},
    {"name": "Patricia Hogan", "room_number": 118},
    {"name": "Frank Kjelsvik", "room_number": 107},
    {"name": "Astrid Naess", "room_number": 114},
    {"name": "Jan Erik Karlsen", "room_number": 102},
    {"name": "Karl Ingvar Mikael Mårtensson", "room_number": 105},
    {"name": "Arve Fjeld", "room_number": 124},
    {"name": "Natalia Zielinska", "room_number": 202},
    {"name": "Olava Åmlid Breiland", "room_number": 111},
    {"name": "Jesper Brochmann", "room_number": 204},
    {"name": "Beverley Yates", "room_number": 203},
]

room_report  = [
    {"name": "GARCIA ANTONIO JOSE", "room_number": 100},
    {"name": "OVRID MONA KRISTIN", "room_number": 101},
    {"name": "Huntington Jeffrey", "room_number": 201},
    {"name": "DYRSTAD Ståle", "room_number": 205},
    {"name": "NILSSON TOMMY", "room_number": 206},
    {"name": "SIGURDARDÒTTIR TÒRDIS", "room_number": 207},
    {"name": "GREEN KARL", "room_number": 208},
    {"name": "Karlsen SOLFRID", "room_number": 102},
    {"name": "TAYEB FATIHA", "room_number": 103},
    {"name": "vereyken anita", "room_number": 104},
    {"name": "SCHOBECK LINE", "room_number": 105},
    {"name": "WALLENIUS SUSANNE", "room_number": 106},
    {"name": "Henrik Eilsøe Jens", "room_number": 107},
    {"name": "SCHMIDLIN-GROGG", "room_number": 108},
    {"name": "SKJERVHEIM KJELL", "room_number": 109},
    {"name": "LEHTONEN TIMO", "room_number": 110},
    {"name": "WALLENIUS MELEA", "room_number": 111},
    {"name": "WIBERG ANNIKA", "room_number": 112},
    {"name": "MYRVOLL AUD MARIT", "room_number": 113},
    {"name": "Gans Leo", "room_number": 114},
    {"name": "hodge gillian", "room_number": 115},
    {"name": "Aho Tapani", "room_number": 116},
    {"name": "JORDET ODRUN", "room_number": 117},
    {"name": "Hogan Patricia", "room_number": 118},
    {"name": "Berre Hans", "room_number": 119},
    {"name": "RASK MARIA", "room_number": 120},
    {"name": "Halvorsen Vidar", "room_number": 121},
    {"name": "HEMMING", "room_number": 122},
    {"name": "VAEAETAEJAE PIA", "room_number": 123},
    {"name": "MYROLD BAANN AUD", "room_number": 124},
    {"name": "Howson Michael", "room_number": 125},
    {"name": "MCCAFFERTY IIAN", "room_number": 202},
    {"name": "JULIUSDOTTIR", "room_number": 203},
    {"name": "KRANTZ JORUN", "room_number": 204}
]

# Create df 
df_arrivals = pd.DataFrame(arrivals)
df_departures = pd.DataFrame(departures)
df_room_report = pd.DataFrame(room_report)

# Format the names so they share the same structure and are comparable
df_room_report['name'] = df_room_report['name'].str.split().str[::-1].str.join(' ').str.upper()
df_arrivals['name'] = df_arrivals['name'].str.upper()

# Report Class para manejar la lógica ha de recibir todos los data frame,

class FinalReport():
  def __init__(self, df_arrivals, df_departures, df_room_report):
    self.df_arrivals = df_arrivals
    self.departures = df_departures
    self.room_report = df_room_report
    self.df_room_changes = None
    self.df_stayovers  = None

  # Implementar lógica para los ENTRADAS, SALIDAS, YA AQUÍ, CAMBIOS
  def guess_status_logic(self):
    # YA AQUI LOS CAMBIOS, LAS ENTRADAS NORMALES SON LO RESTANTE
    # REvisar personas room report == df.nombre.llegada, habitacion misma -> YA AQUI
    # Revisa persona room report == df.nombre.llegada, en otra habitación --> CAMBIO
    # != YA AQUI AND != CAMBIO ENTRADA


    # Salida,
    # Revisar salidas.df, ya aqui se ignora, cambios la habitación de la que sale



    # Entradas, si hay que cobrar, cantidad cobrar, notas


    # Output:
    



    
 # Implementar la creación de un documento de Excel en el formato que quiero
 # Para esto vamos a utilizar openpyxl
 # https://openpyxl.readthedocs.io/en/stable/#introduction
    def generate_excel(self):
        pass





  # Implementar la creación de fichas
  # Usar el html y los componentes

    def generate_cards(self):
      pass


# 1. Ver si hay alguna coincidencia entre las personas que llegan y las que ya están usando el merge un join por la izquierda
stays_over = pd.merge(df_arrivals, df_room_report, on=['name', 'room_number'], how='inner')

# 2. Si hay coincidencia y se queda en la misma habitación son un YA AQUI
df_staysover = stays_over
print(df_staysover)
# 3. Si hay coincidencia pero se quedan en otra habitación son un cambio


# 4. Si no hay coincidencia son una entrada normal


# 5. Salida


# Salida,
# Revisar salidas.df, ya aqui se ignora, cambios la habitación de la que sale



# Entradas, si hay que cobrar, cantidad cobrar, notas


# Output:
    