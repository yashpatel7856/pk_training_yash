import json
import json.tool
dic={
    "name":"somehting",
    "age":3,
    "city":"asdas"
}

# json_str=json.dumps(dic)
        
with open("foo.json",'a+') as file:
    file.seek(1)
    json.dump(dic,file)
    # new_dic=json.load(file)
    # print(new_dic["name"])

# json_dic=json.loads(json_str)


# print(json_dic["name"])