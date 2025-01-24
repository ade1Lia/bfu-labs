
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def create_new_invoice(original_invoice):
    new_invoice = original_invoice.copy()
    new_invoice["id"] = 3
    new_invoice["total"] = 150.0
    new_invoice["items"] = []

    item_4 = {"name": "item 4", "quantity": 1, "price": 60.0}
    item_5 = {"name": "item 5", "quantity": 2, "price": 90.0}

    new_invoice["items"].append(item_4)
    new_invoice["items"].append(item_5)

    return new_invoice

data = load_json("ex_3.json")
original_invoice = data['invoices'][0]

new_invoice = create_new_invoice(original_invoice)
data["invoices"].append(new_invoice)

save_json(data, "ex_3_new.json")
