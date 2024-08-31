import json

# Read your file containing multiple JSON objects
with open('results.json', 'r', encoding='utf-8') as file:
    data = file.readlines()

# Convert each JSON object into a Python dictionary
json_objects = [json.loads(obj) for obj in data]

# Wrap the list of dictionaries into a JSON array
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, indent=4)
