import json
import xmltodict
import yaml

def to_json(function):
    def wrapped(format = 'json'):
        result = function(format = 'json')
        if format == 'json':
            json_param = json.dumps(result)
            return json_param
        elif format == 'xml':
            xml_param = xmltodict.unparse(result)
            return xml_param
        elif format == 'yaml':
            yaml_param =  yaml.dump(result)
            return  yaml_param
    return wrapped

