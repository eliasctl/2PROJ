import requests

def deleteGame(idGame):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001"

    try:
        # Make the API request
        requests.delete(url+'/game/?id='+str(idGame))

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")
