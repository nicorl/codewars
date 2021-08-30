import json

with open("datos.json") as jsonFile:
    infodelJson = json.load(jsonFile)
    jsonFile.close()

if infodelJson["autor"]["nombre"] == "Manolo Bergillos":
    print(infodelJson["config2"]["otro"])
else:
    pass
