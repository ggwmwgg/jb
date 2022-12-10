import json
import itertools

json_data = json.loads(input())
register = {}
for data in json_data:
    #initialising the value of dict to be an empty list for each bus id
    register.setdefault(data["stop_type"], [])
    #appending
    register[data["stop_type"]].append(data["stop_name"])

    mid = []
    for name in set(itertools.chain(*register.values())):
        if list(itertools.chain(*register.values())).count(name) > 1:
            mid.append(name)

    print("On demand stops test:")
    out = set(register.get("O", [])) & set(itertools.chain(register.get("S", []),register.get("F", []),register.get("", []),mid,))
    print("Wrong stop type:", sorted(out)) if out else print("OK")