import json
f1 = open("/Users/sathyanarayan/Desktop/test1.json","r")

data = json.load(f1)
min_list =[]
print([{"id": i["id"],"key":i["key"]} for i in data])


