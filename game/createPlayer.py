import requests
import random


# Logical function to create the game with the API
def createPlayer():
    intRandom = random.randint(0, 10000000)
    url = "http://eliascastel.ddns.net:3001/player?name=player" + str(intRandom)
    try:
        response = requests.post(url)  # Make a POST request with JSON data

        # print(response.json())
        # print(response)
        return response.json()["id"]
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception as needed