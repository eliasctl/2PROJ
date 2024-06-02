import requests

def updateData(data):
    # Define the URL
    url = "http://eliascastel.ddns.net:3001/game/data"
    try:
        urlData = "?"
        for elements in data:
            data[elements] = str(data[elements])
            urlData += elements + "=" + data[elements] + "&"
        
        # print(data)
        print(urlData)
        # print(url + urlData)
        # Make the API request
        response = requests.put(url+urlData)

        print("Data updated")
        print(response.text)
        print(response.status_code)

        # Process the response
        
        # Print the response
        #print(response)
        #return response
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")

# data = {
#     "player1HPCamp": 100,
#     "player2HPCamp": 100,
#     "id": 67
# }

# updateData(data)