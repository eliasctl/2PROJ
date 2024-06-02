import requests

def getSpecialCapacity():
    # Define the URL
    url = "http://eliascastel.ddns.net:3001"

    try:
        # Make the API request
        response = requests.get(url+'/game/specialCapacity')

        # Process the response
        data = response.json()
        
        # Print the data
        return data
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")
