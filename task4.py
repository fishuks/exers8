import json

input_data = input("Введите список кортежей в формате JSON: ")
tuple_list = json.loads(input_data)
sorted_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)

print(sorted_list)
