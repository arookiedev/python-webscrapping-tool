from pprint import PrettyPrinter
import json

printer = PrettyPrinter()

def print_JSON_content(response):
    try:
        response = response.json()
        printer.pprint(response)
    except json.decoder.JSONDecodeError:
        print("Le retour ne contient aucun JSON.")