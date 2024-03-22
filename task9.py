import json
import xmltodict
import yaml

def to_json(function):
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)
        json_parameter = json.dumps(result)
        return json_parameter
    return wrapped

