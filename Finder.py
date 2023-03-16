import json
import scripts.Coordinate as cord

map = {}
properties = {}
validInput = False

with open('map.json', 'r') as f:
    map = json.load(f)

with open('properties.json', 'r') as f:
    properties = json.load(f)

while not validInput:
    print("Please enter a property you want to find. Seperate multiple properties with a '|'")

    search = input().split('|')

    hasFalse = False
    for x in search:
        if not (x in properties):
            print(x + " is not a valid property")
            hasFalse = True
    if not hasFalse:
        validInput = True

mapWeight = []

xCoord = 0
yCoord = 0
for x in map:
    for y in x:
        propAmm = 0
        propMax = 0
        oldProp = []
        for res in y["ressources"]:
            for prop in res["properties"]:
                if prop["type"] in search and prop["type"] not in oldProp:
                    propAmm += 1
                if prop["type"] not in oldProp:
                    oldProp.append(prop["type"])
                    propMax += 1
        if propAmm / propMax > 0:
            mapWeight.append(cord.Coord(xCoord, yCoord, propAmm / propMax, y["cost"], y["name"]))
        yCoord += 1
    xCoord += 1

mapWeight.sort(reverse=True, key=lambda x: x.weight)
print("\nThese are the best systems for getting this ressource:")

for x in range(10):
    try:
        print("\n" + mapWeight[x].name + "\nCoords: " + str(mapWeight[x].x - 60000) + '|' + str(60000 - mapWeight[x].y) + "\nCost: " + str(mapWeight[x].cost) + "\nEfficiency: " + str(mapWeight[x].weight))
    except:
        break