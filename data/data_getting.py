import requests

def get_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response

        else:
            print("Hôte non trouvé, il est possible que l'hôte soit innacessible.")

    except requests.exceptions.MissingSchema:
        return "url not found"
