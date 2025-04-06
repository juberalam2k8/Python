import json
import requests  # Better than subprocess for HTTP requests

url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"
content_file = "test.json"

try:
    # Use requests to fetch the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes
    
    # Try to parse the JSON content
    try:
        json_data = response.json()
        print(json_data)

        # Write the parsed JSON data to a file
        with open(content_file, 'w') as f:
            json.dump(json_data, f, indent=4)
        
        # Print the structure of the JSON data for inspection
        print(json.dumps(json_data, indent=4))  # Pretty print the JSON structure
        
        # Check if 'name' is directly in the top-level structure
        if 'name' in json_data:
            print(f"Name found: {json_data['name']}")
        else:
            print("'name' key not found in top-level structure.")
            # Now try searching within nested structures (e.g., a list or nested dict)
            found_name = False
            # If 'json_data' contains an array or objects, loop through them
            if isinstance(json_data, list):  # If the root is a list
                for item in json_data:
                    if isinstance(item, dict) and 'name' in item:
                        print(f"Found name in nested item: {item['name']}")
                        found_name = True
                        break
            elif isinstance(json_data, dict):  # If the root is a dictionary
                # Search through possible nested dictionaries
                for key, value in json_data.items():
                    if isinstance(value, dict) and 'name' in value:
                        print(f"Found name in nested dictionary at '{key}': {value['name']}")
                        found_name = True
                        break
            if not found_name:
                print("'name' key not found anywhere in the JSON structure.")
            
    except json.JSONDecodeError:
        print(f"URL did not return valid JSON. Received content type: {response.headers['Content-Type']}")
        print("Saving raw content for inspection")
        with open(content_file, 'w') as f:
            f.write(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
