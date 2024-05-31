import requests

def updateData(data):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001/game/data"
    print(type(data))
    try:
        for elements in data:
            data[elements] = str(data[elements])
        
        print(data)
        # Make the API request
        request = requests.put(url, json=data)

        # Process the response
        response = request.json()
        
        # Print the response
        print("Data tried to update XD")
        print(response)
        return response
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")