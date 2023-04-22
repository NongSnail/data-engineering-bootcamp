import json

import requests

def write_json(new_data, filename='data.json'):
    with open(filename, "r") as file:
        data = json.load(file)
    print(type(data)) 
    data["list"].append(data)    
    with open(filename, "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    del data['status']
    print(data)
    write_json(data)

