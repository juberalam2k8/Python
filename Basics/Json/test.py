import requests

# The URL that provides the JSON data
url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    try:
        # Parse the JSON content from the response
        data = response.json()
        print(data)
    except ValueError:
        print("Error: The response is not valid JSON.")
else:
    print(f"Error: Unable to fetch data (status code: {response.status_code})")
