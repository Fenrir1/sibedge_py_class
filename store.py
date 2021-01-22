import json
import os
from person import Person

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
STORE_PATH = os.path.join(THIS_FOLDER, 'phonebook.json')

class Store(object):
    def __init__(self):
        print('connected to store')     

    def readStore(self):
        result = []
        with open(STORE_PATH) as json_file:
            data = json.load(json_file)
            for person in data['person']:
                result.append(Person(**person))
        return result
    
    def writeStore(self, data):
        result = { "person": [] }
        with open(STORE_PATH, 'w') as json_file:
            for person in data:
                result["person"].append(person.toJSON())
            json.dump(result, json_file)