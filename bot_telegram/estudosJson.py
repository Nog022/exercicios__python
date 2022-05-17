import json

json_string = '{"First_name": "Rodrigo", "Last_name": "Nogueira"}'

json_dict = json.loads(json_string)


d = {
    "First_name": "Rodrigo",
    "Last_name": "Nogueira",
    "Titles": ['BDF', 'Developer'],
}
 
#transformando o dicionario em uma string
d_jason = json.dumps(d)

print(json_string)
print(json_dict)
print(json_dict.keys())