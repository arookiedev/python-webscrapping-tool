from data import data_getting, action_function_call
from data.actions import HTML_printer, JSON_printer
from pystyle import Colorate, Colors
from pycenter import center
import os

logo = """
__  _  __ ____\_ |__   ______ ________________  ______ ______ |__| ____    ____  
\ \/ \/ // __ \| __ \ /  ___// ___\_  __ \__  \ \____ \\____ \|  |/    \  / ___\ 
 \     /\  ___/| \_\ \\___ \\  \___|  | \// __ \|  |_> >  |_> >  |   |  \/ /_/  >
  \/\_/  \___  >___  /____  >\___  >__|  (____  /   __/|   __/|__|___|  /\___  / 
             \/    \/     \/     \/           \/|__|   |__|           \//_____/  


"""

help_message = """
__  _  __ ____\_ |__   ______ ________________  ______ ______ |__| ____    ____  
\ \/ \/ // __ \| __ \ /  ___// ___\_  __ \__  \ \____ \\____ \|  |/    \  / ___\ 
 \     /\  ___/| \_\ \\___ \\  \___|  | \// __ \|  |_> >  |_> >  |   |  \/ /_/  >
  \/\_/  \___  >___  /____  >\___  >__|  (____  /   __/|   __/|__|___|  /\___  / 
             \/    \/     \/     \/           \/|__|   |__|           \//_____/


        Une réponse a été reçue, quelle action voulez vous réaliser ?

        1 : Afficher le contenu JSON    2 : Afficher le code HTML   
"""

def get_url_and_data(error = False):
    global data
    os.system("cls")

    if error:
        print("L'url n'existe pas, entrez une autre url")
    
    print(Colorate.Horizontal(Colors.purple_to_blue, center(logo)))
    print("Entrez l'url sur laquelle vous voulez faire du scrapping.")

    url = input("Scrap -> ")
    data = data_getting.get_data(url)

    if data == "url not found":
        get_url_and_data(True)

    else:
        convert_and_exploit()

def convert_and_exploit():
    os.system("cls")
    print(Colorate.Horizontal(Colors.purple_to_blue, center(help_message)))
    action = input("Scrap ->")

    if action == "1":
        JSON_printer.print_JSON_content(data)
        
    elif action == "2":
        HTML_printer.print_HTML_code(data)

get_url_and_data()