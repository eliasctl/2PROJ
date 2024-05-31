import requests


# Logical function to create the game with the API
def gameBegin(idPlayer):
    url = "http://eliascastel.ddns.net:3001/game/"
    try:
        data = "?player=" + idPlayer
        response = requests.post(url+data)  # Make a POST request with JSON data
        # Handle the response as needed
        return response.json()["id"]  # Assuming the response is in JSON format
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception as needed