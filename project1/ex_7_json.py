import json

DATA = {
    'cars': [
        {'mark': 'BMW', 'model': 'E36', 'mileage': 1000000, 'addons': ['lever', 'spare wheel', 'pump']},
        {'mark': 'Ford', 'model': 'Focus', 'mileage': 200000, 'addons': ['distinguisher', 'lever']},
    ],
    'bicycles': {
        'mtb': [
            {'mark': 'Trek', 'model': 'Superfly', 'mileage': 2000, 'addons': ['pedals', 'fenders']},
            {'mark': 'Canyon', 'model': 'Exceed', 'mileage': 15000, 'addons': []},
            {'mark': 'Canyon', 'model': 'Lux World Cup', 'mileage': None}
        ],
        'road': [
            {'mark': 'Canyon', 'model': 'Ultimate', 'mileage': 9000, 'addons': ['pedals', 'mount']}
        ],
        'gravel': [
            {'mark': 'Canyon', 'model': 'Grizl', 'mileage': 17000, 'addons': ['pedals', 'fenders', 'bag'], 'extra': ('a',1.234567890, True)}
        ],
        'problems': [{
            'tuple': ("apple", "banana", "cherry"),
            #'set': {"apple", "banana", "cherry"}, #TypeError: Object of type set is not JSON serializable
        }]
    }
}

# write json
with open('data.json', 'w') as data_file:
    #data_file.write(json.dumps(DATA))
    json.dump(DATA, data_file)

with open('data.json', 'r') as data_file:
    #data = data_file.read()
    #json_data = json.loads(data)
    json_data = json.load(data_file)
    print(json_data)