import requests

url = "http://eliascastel.ddns.net:3001/game/"

# Logical function to create the game with the API
def createGame(url):
    
    try:
        data = "?player=1"
        response = requests.post(url+data)  # Make a POST request with JSON data
        # Handle the response as needed
        print(response.json())  # Assuming the response is in JSON format
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception as needed

# Example usage
createGame(url)
