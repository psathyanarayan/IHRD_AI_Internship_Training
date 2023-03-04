'''
Given JSON contains key value pair as "data_type": "str".
We have to print out child jsons with "data_type": "str" an

'''
import json
file_obj = open("test1.json","r")
data = json.load(file_obj)
extractList = []
 # dumps prettify the output
print(json.dumps([k for i in data  for k in i["child"]  if(k.get("data_type","") == "str")],indent=1)) # dumps prettify the output
