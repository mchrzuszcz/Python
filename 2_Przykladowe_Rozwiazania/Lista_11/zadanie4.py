import json

def read_json(path):
    with open(path, "r") as f:
        json_data = json.load(f)
    return json_data

json_content = read_json('.\5_Materialy_Pomocnicze\kraje.json')
print(json_content)

for i, element in enumerate(json_content["products"]):
    print("{}. Kraj: {}".format(i+1, element.get("name")))
