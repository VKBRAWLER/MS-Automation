import json

# Your new list of tuples
new_account_location = [(1094, 947), (1096, 836), (1097, 723), (1094, 614), (1097, 500), (1098, 388), (1096, 275)]

# Convert tuples to lists
new_account_location_list = [list(t) for t in new_account_location]

# Read, update, and write the JSON file in one go
with open('mouse.json', 'r+') as f:
  data = json.load(f)
  data['account_location'] = new_account_location_list
  f.seek(0)
  json.dump(data, f, indent=4)
  f.truncate()
