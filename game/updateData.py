import requests

def updateData(data):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001/game/data"

    try:
        
        # Make the API request
        response = requests.put(url, data=data)

        # Process the response
        data = response.json()
        
        # Print the data
        print("Data updated successfully")
        print(data)
        return data
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")
