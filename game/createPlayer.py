import requests


# Logical function to create the game with the API
def createPlayer():
    url = "http://eliascastel.ddns.net:3001/player/"
    try:
        datatest = {"name": "Omaiwa"}
        response = requests.post(url, json=datatest)  # Make a POST request with JSON data
        # Handle the response as needed
        print(response.json())  # Assuming the response is in JSON format
        print(response)
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception as needed

createPlayer()