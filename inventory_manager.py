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

def get_menu_option():
    print("-" * 10, "MENU", "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 26)
    print()
    while True:
        option = input("Enter option: ")
        try:
            option = int(option)
            if option >= 1 and option <= 6:
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid option. Please try again.")
    return option

print("=" * 50)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 50)
print()
inventory = load_inventory()
print("Inventory loaded successfully.")
print()
while True:
    option = get_menu_option()
    if option == 1:
        pass