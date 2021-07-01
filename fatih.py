import json
file=open("fatih.json","r")
json_file=json.load(file)
obj=json_file["kimlik"]
print(obj["Ad"],obj["Soyad"],sep="\n")
