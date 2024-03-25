import json
import xmltodict
import yaml

def to_format(format='json'):
    def decorator(function):
        def wrapped(*args, **kwargs):
            result = function(*args, **kwargs)
            if format == 'json':
                json_parameter = json.dumps(result)
                return json_parameter
            elif format == 'xml':
                xml_param = xmltodict.unparse(result)
                return xml_param
            elif format == 'yaml':
                yaml_param =  yaml.dump(result)
                return  yaml_param
        return wrapped
    return decorator

@to_format(format = 'xml')
def difference_numbers(a, b):
    return {f'{a}' : a - b}

@to_format()
def squaring(num):
    return {f'{num}' : num ** 2}
