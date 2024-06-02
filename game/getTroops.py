import requests

def getTroops():
    # Define the URL
    url = "http://eliascastel.ddns.net:3001"

    try:
        # Make the API request
        response = requests.get(url+'/game/troops')

        # Process the response
        data = response.json()
        
        # Print the data
        return data
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")

# data = getTroops()
# print(data)
# print(data[0])