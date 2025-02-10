arrivals = [
    {
        "name": "Patricia Hogan",
        "room_number": 118,
        "guest_type": "Owner usage",
        "arr_date": "01/02/2025",
        "dep_date": "08/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": "14:00",
            "Guest_Of_Owner": True,
            "Toppers": True,
            "Blankets": True,
            "Others": ""
        },
        "am_to_pay": 0.00
    },
    {
        "name": "Hans Berre",
        "room_number": 200,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "05/02/2025",
        "notes": {
            "Baby_Cot": True,
            "High_Chair": True,
            "Hour_Of_Arrival": "21:00",
            "Guest_Of_Owner": True,
            "Toppers": False,
            "Blankets": True,
            "Others": ""
        },
        "am_to_pay": 850.00
    },
    {
        "name": "Sonja Kessler",
        "room_number": 203,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "04/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": "13:30",
            "Guest_Of_Owner": False,
            "Toppers": False,
            "Blankets": False,
            "Others": "Vegan breakfast"
        },
        "am_to_pay": 645.00
    },
    {
        "name": "Johan Nielsen",
        "room_number": 102,
        "guest_type": "Owner usage",
        "arr_date": "01/02/2025",
        "dep_date": "08/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": None,
            "Guest_Of_Owner": True,
            "Toppers": False,
            "Blankets": False,
            "Others": "No housekeeping needed"
        },
        "am_to_pay": 0.00
    },
    {
        "name": "Alice Montague",
        "room_number": 105,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "07/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": None,
            "Guest_Of_Owner": False,
            "Toppers": False,
            "Blankets": False,
            "Others": "Minibar refill daily, Gluten-free food requested"
        },
        "am_to_pay": 1025.50
    },
    {
        "name": "Kristian Berg",
        "room_number": 101,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "06/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": None,
            "Guest_Of_Owner": False,
            "Toppers": False,
            "Blankets": False,
            "Others": "Quiet room requested"
        },
        "am_to_pay": 820.00
    },
    {
        "name": "Erika Lunden",
        "room_number": 100,
        "guest_type": "Transient",
        "arr_date": "01/02/2025",
        "dep_date": "05/02/2025",
        "notes": {
            "Baby_Cot": False,
            "High_Chair": False,
            "Hour_Of_Arrival": "12:00",
            "Guest_Of_Owner": False,
            "Toppers": False,
            "Blankets": False,
            "Others": ""
        },
        "am_to_pay": 990.00
    }
]





html = """ <!DOCTYPE html>
<html lang="en">
<head>
  <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
  <meta charset="UTF-8">
  <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Client Cards</title>
</head>

<body class="h-100 grid grid-cols-2 gap-8 p-8"> 
"""


for arrival in arrivals:
    html += f"""
    <div class="bg-white shadow-md rounded-lg overflow-hidden w-full max-w-sm mx-auto h-[200px] flex flex-col">
        <div class="p-3 flex-grow overflow-auto">
            <div class="flex justify-between items-start mb-2">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span class="text-xl font-bold text-gray-800">{arrival["room_number"]}</span>
                        <span class="text-base font-medium text-gray-700 truncate">{arrival["name"]}</span>
                    </div>
                    <div class="text-xs font-medium text-gray-600 bg-gray-100 px-2 py-0.5 rounded inline-block">
                        {arrival["guest_type"]}
                    </div>
                </div>
                <div class="text-right text-xs font-medium text-gray-600">
                    <p>
                        {arrival["arr_date"]} - {arrival["dep_date"]}
                    </p>
                </div>
            </div>
            <div class="grid grid-cols-2 gap-1 text-xs mb-2">
            {f'<p><span class="font-semibold"> Cobrar: </span> {str(arrival["am_to_pay"])} €</p>' if arrival.get("am_to_pay") else ''}

                {"<p><span class='font-semibold'>Llegada:</span> " + arrival['notes'].get('Hour_Of_Arrival', '') + "</p>" if arrival['notes'].get('Hour_Of_Arrival') else ''}
                {("<p><span class='font-semibold'>Equipo:</span> " + 
                   (" Cuna" if arrival['notes'].get('Baby_Cot') else '') +
                   (" &" if arrival['notes'].get('Baby_Cot') and arrival['notes'].get('High_Chair') else '') +
                   (" Trona" if arrival['notes'].get('High_Chair') else '') +
                   "</p>") if arrival['notes'].get('Baby_Cot') or arrival['notes'].get('High_Chair') else ''}

                {("<p> <span class='font-semibold'>Ropa Cama:</span> " + 
                  (" Extra Toppers" if arrival['notes'].get('Toppers') else '') +  
                  (" &" if arrival['notes'].get('Toppers') and arrival['notes'].get('Blankets') else '') +
                  (" Blankets" if arrival['notes'].get('Blankets') else '') +
                 "</p>" ) if arrival['notes'].get('Toppers') or arrival['notes']['Blankets'] else ''}

                {f'<p><span class="font-semibold"> Guest of Owner</span> ' if arrival["notes"]["Guest_Of_Owner"] else ''} 
            </div>
        </div>
        {("<div class='bg-gray-50 p-2 border-t border-gray-200 text-xs text-gray-600 italic overflow-auto max-h-[60px]'>" + arrival['notes'].get('Others', '') + "</div>") if arrival['notes'].get('Others') else ''}
    </div>
    """


html += """
  </body>
</html>
"""


# Escribir el contenido HTML a un archivo HTML
file_path = "client_cards.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

import webbrowser

webbrowser.open(file_path)