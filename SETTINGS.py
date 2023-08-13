import json
asb = open('settings.json')
d = json.load(asb)
asb.close()
das = open('config.json')
e = json.load(das)
das.close()
print(d, e)