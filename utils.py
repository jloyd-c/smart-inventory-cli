import json
import os

#json to python loader
def load_form_json(filename):
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as file:
        content = file.read().strip()
        if not content: 
            return []
        return json.loads(content)
    
#python to json saver and return empty
def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)