import json


def get_value(filename, key):
    try:
        if 
    handle = open(filename)
    file_contents = handle.read()
    js_text = json.loads(file_contents)
    return js_text[key]