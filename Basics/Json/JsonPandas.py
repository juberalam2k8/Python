import requests
import json
import pandas as pd

url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"
response=requests.get(url)
response.raise_for_status()


def slicejson(response):
    try:
        data=response.json()
        try:
            df = pd.DataFrame(data)
            filtered_df=df[(df['language']=='Hindi') & (df['name']=='Sunil Kapoor')]
            print(filtered_df)
            
                  
        except json.JSONDecodeError:
            print("Json is not proper")
    except requests.exceptions.RequestException as e:
        print(f"request failed {e}")
    except Exception as e:
        print(f"error occured {e}")


slicejson(response)
    