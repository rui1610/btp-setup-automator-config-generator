import json

filename = "trial_entitledServices.json"
f = open(filename)
# returns JSON object as a dictionary
data = json.load(f)

for item in data.get("entitledServices"):
    print(item.get("displayName") + " ; " + item.get("description") )
