import requests


# Logical function to create the game with the API
def gameBegin(idPlayer):
    url = "http://eliascastel.ddns.net:3001/game?player=" + idPlayer
    try:
        response = requests.post(url)  # Make a POST request with JSON data
        # Handle the response as needed
        return response.json()["id"]  # Assuming the response is in JSON format
    except Exception as e:
        print(f"An error occurred: {e}")
        print(response)
        # Handle the exception as needed

gameBegin("1")