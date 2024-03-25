import json

data = input()
no_json_data = json.loads(data)
sorted_list = sorted(no_json_data, key=lambda x: x[1], reverse=True)

print(sorted_list)
