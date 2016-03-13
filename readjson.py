import json
with open('reliancejson.json', 'r') as jf:
    data = json.load(jf)
    print data['dataset']['column_names']