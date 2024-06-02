import requests

def joinGame(idPlayer, idGame, startTime):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001"

    try:
        # Make the API request
        requests.put(url+'/game/joinGame/?player='+str(idPlayer)+'&id='+str(idGame)+'&startTime='+str(startTime) )

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")

# data = getTroops()
# print(data)
# print(data[0])