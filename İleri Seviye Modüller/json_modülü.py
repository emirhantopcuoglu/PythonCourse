import json

person_string = '{"name":"Ali","languages":["Python","C"]}'

# JSON string to dictionary
# result =  json.loads(person_string) # string ifadeci dictionary'e çevirme
# print(type(result))

# with open("person.json") as f:
#     data = json.load(f)
#     print(data)

# Dict to JSON string
person_dict = {
    "name":"Ali",
    "languages":["Python","C++"]
}
# result = json.dumps(person_dict) # dictionary ifadeyi stringe çevirme
# print(type(result))
# print(result)

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

# person_dict = json.loads(person_string)
# result = json.dumps(person_dict,indent=4,sort_keys=True)
# print(result)