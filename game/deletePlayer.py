import requests

def deletePlayer(idPlayer):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001"

    try:
        # Make the API request
        requests.delete(url+'/player/?id='+str(idPlayer))

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")
