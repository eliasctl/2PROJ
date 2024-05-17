import time
import requests

url = "http://eliascastel.ddns.net:3001"
while True:
    try:
        # Make the API request
        response = requests.get(url+'/game/background')

        # Process the response
        data = response.json()
        
        # Print the data
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data received")

    # Wait for 0.1 second
    time.sleep(0.1)
