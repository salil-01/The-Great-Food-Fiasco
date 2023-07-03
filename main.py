import random
import json
from tabulate import tabulate

foodItems = []
orders = []
order_counter = 1


def save_menu():
    with open("menu.json", "w") as file:
        json.dump(foodItems, file)


def load_menu():
    global foodItems
    try:
        with open("menu.json", "r") as file:
            foodItems = json.load(file)
    except FileNotFoundError:
        foodItems = []


def save_orders():
    with open("orders.json", "w") as file:
        mydictionary = {
            "orders": orders,
            "order_counter": order_counter
        }
        json.dump(mydictionary, file)


def load_orders():
    global orders, order_counter
    try:
        with open("orders.json", "r") as file:
            data = json.load(file)
            orders = data["orders"]
            order_counter = data["order_counter"]
    except FileNotFoundError:
        orders = []
        order_counter = 1


def display_menu():
    table = []
    headers = ["ID", "Name", "Price", "Availability", "Stock"]

    for index, item in enumerate(foodItems):
        item["id"] = index + 1
        table.append([item["id"], item["name"], item["price"],
                     item["availability"], item["stock"]])

    print(tabulate(table, headers, tablefmt="fancy_grid"))


def add_item():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    availability = "Yes"
    stock = int(input("Enter item stock: "))
    new_item = {
        "id": len(foodItems) + 1,
        "name": name,
        "price": price,
        "availability": availability,
        "stock": stock
    }
    foodItems.append(new_item)
    print(f"Item '{name}' added to the menu.")
    save_menu()


def remove_item():
    display_menu()
    item_id = int(input("Enter the ID of the item to remove: "))
    for item in foodItems:
        if item["id"] == item_id:
            foodItems.remove(item)
            print(f"Item with ID {item_id} removed from the menu.")
            save_menu()
            break
    else:
        print(f"No item found with ID {item_id}. Please enter a valid ID.")


def update_availability():
    display_menu()
    item_id = int(input("Enter the ID of the item to update availability: "))
    availability = input("Set availability (Yes/No): ")
    for item in foodItems:
        if item["id"] == item_id:
            item["availability"] = availability
            if availability == "No":
                item["stock"] = 0
            else:
                item["stock"] = int(input("Enter item stock: "))
            print(
                f"Availability for item with ID {item_id} updated to {availability}.")
            save_menu()
            break
    else:
        print(f"No item found with ID {item_id}. Please enter a valid ID.")


def take_order():
    global order_counter
    display_menu()
    print("------- New Order -------")
    customer_name = input("Enter customer name: ")
    print("Available items:")
    for item in foodItems:
        if item["availability"] == "Yes":
            print(
                f'ID: {item["id"]}, Name: {item["name"]}, Price: {item["price"]}')
    order_items = input(
        "Enter item IDs to order (separated by comma): ").split(",")
    order_items = [int(item_id) for item_id in order_items]
    total_price = 0

    for item_id in order_items:
        for item in foodItems:
            if item["id"] == item_id:
                if item["availability"] == "No":
                    print(
                        f"Item with ID {item_id} is currently unavailable for ordering.")
                    break
                if item["stock"] <= 0:
                    print(f"Insufficient stock for item with ID {item_id}.")
                    break
                item["stock"] -= 1
                total_price += item["price"]
                break
        else:
            print(f"No item found with ID {item_id}. Please enter a valid ID.")

    else:
        order = {
            "order_id": order_counter+1,
            "customer_name": customer_name,
            "items": order_items,
            "total_price": total_price,
            "status": "Received"
        }
        orders.append(order)
        order_counter += 1
        print("Order placed successfully.")
        print(f"Total Price: {total_price}")
        save_orders()


def change_status():
    display_orders()
    order_id = int(input("Enter the ID of the order to change status: "))
    for order in orders:
        if order["order_id"] == order_id:
            status = input(
                "Enter the new status (Preparing/Ready/Pickup/Delivered): ")
            if status in ["Preparing", "Ready", "Pickup", "Delivered"]:
                order["status"] = status
                print(
                    f"Status for order with ID {order_id} changed to {status}.")
                save_orders()
            else:
                print("Invalid status. Please enter a valid status.")
            break
    else:
        print(f"No order found with ID {order_id}. Please enter a valid ID.")


def display_orders():
    table = []
    headers = ["Order ID", "Customer", "Status"]

    for order in orders:
        table.append(
            [order["order_id"], order["customer_name"], order["status"]])

    print(tabulate(table, headers, tablefmt="fancy_grid"))


# Load menu and orders data
load_menu()
load_orders()

# Main menu
while True:
    print("\n------ Food Management App ------")
    print("1. Display Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Availability")
    print("5. Take Order")
    print("6. Change Order Status")
    print("7. Display Orders")
    print("8. Quit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        display_menu()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        update_availability()
    elif choice == '5':
        take_order()
    elif choice == '6':
        change_status()
    elif choice == '7':
        display_orders()
    elif choice == '8':
        print("Thank you for using the Food Management App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
