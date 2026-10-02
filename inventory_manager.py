import json

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            print('inventory.json found.')
            return data
    except FileNotFoundError:
        print('inventory.json not found. Using blank inventory.')
        return {}

print("=" * 50)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 50)
print()
inventory = load_inventory()
print("Inventory loaded successfully.")
