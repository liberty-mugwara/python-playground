import json


def prettyPrint(data, indent=2):
    print(json.dumps(data, indent=indent))
