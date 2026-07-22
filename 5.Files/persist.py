import shelve
with shelve.open("my_shelf") as db:
    db["id"] = {"name": "alex", "aadhaar": 1234455 }
    db["address"] = [32, 'shalimar garden', 'injambakkam', 'chennai']

with shelve.open("my_shelf") as db:
    print("Identity:",db["id"])
    print("Address :", db["address"])

# import pickle
# data = {"name":"alex", "age": 54, "city":"chennai"}
# # Pickling (serialization)
# with open("test.pkl", "wb") as f:
# 	pickle.dump(data, f)
# # Unpickling (deserialization)
# with open("test.pkl", "rb") as f:
# 	loaded_data = pickle.load(f)
# print(data)
# print(loaded_data)

# import json
# import os
#
# # Step 1: Create a Python object (dictionary)
# data = {
#     "name": "Alex",
#     "location": 'Chennai',
#     "skills": ["Python", "C/C++", "Linux"],
# }
#
# # Step 2: Serialize Python object to JSON string
# json_string = json.dumps(data)
# print("Serialized JSON string:")
# print(json_string)
#
# # Step 3: Deserialize JSON string back to Python object
# python_obj = json.loads(json_string)
# print("\nDeserialized Python object:")
# print(python_obj)
#
# # Accessing values
# print("\nName:", python_obj["name"])
# print("Skills:", python_obj["skills"])
#
# print(os.getcwd())