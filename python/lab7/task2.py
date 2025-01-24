import json

def fix_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            try:
                data = json.loads(file_content)
                print("JSON is already valid.")
                return data
            except json.JSONDecodeError:
                print("Attempting to fix the extra data issue...")
                fixed_content = f"[{file_content}]"
                data = json.loads(fixed_content)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"File '{file_path}' has been fixed and saved.")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
file_path = "ex_2.json"
data = fix_json_file(file_path)
print(data)