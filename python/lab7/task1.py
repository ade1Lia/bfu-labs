
import json
from jsonschema import validate, ValidationError


def check_json_against_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        return "Validation successful"
    except ValidationError as ex:
        return f"Validation error: {ex.message}"


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


true_json = load_json_file("ex_1.json")
error_json = load_json_file("ex_1_err.json")
schema = load_json_file("ex_1_schema.json")

print(check_json_against_schema(true_json, schema))
print(check_json_against_schema(error_json, schema))
