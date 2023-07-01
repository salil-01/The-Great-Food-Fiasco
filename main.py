from tabulate import tabulate

foodItems = [
    {"id": 1, "name": "Samosa", "price": 250, "availability": "Yes", "stock": 10},
    {"id": 2, "name": "Chips", "price": 50, "availability": "Yes", "stock": 10},
    {"id": 3, "name": "Lassi", "price": 100, "availability": "Yes", "stock": 10}
]

orders = []
order_counter = 1


def display_menu():
    table = []
    headers = ["ID", "Name", "Price", "Availability", "Stock"]

    for item in foodItems:
        table.append([item["id"], item["name"], item["price"],
                     item["availability"], item["stock"]])

    print(tabulate(table, headers, tablefmt="fancy_grid"))


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
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


def remove_item():
    display_menu()
    item_id = int(input("Enter the ID of the item to remove: "))
    for item in foodItems:
        if item["id"] == item_id:
            foodItems.remove(item)
            print(f"Item with ID {item_id} removed from the menu.")
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
    item_id = int(input("Enter item ID to order: "))
    quantity = int(input("Enter quantity: "))
    for item in foodItems:
        if item["id"] == item_id:
            if item["availability"] == "No":
                print("Sorry, this item is currently unavailable for ordering.")
                return
            if item["stock"] < quantity:
                print("Insufficient stock for this item.")
                return
            item["stock"] -= quantity
            break
    else:
        print(f"No item found with ID {item_id}. Please enter a valid ID.")

    order = {
        "order_id": order_counter,
        "customer_name": customer_name,
        "item_id": item_id,
        "quantity": quantity,
        "status": "Received"
    }
    orders.append(order)
    order_counter += 1
    print("Order placed successfully.")


def change_status():
    display_orders()
    order_id = int(input("Enter the ID of the order to change status: "))
    for order in orders:
        if order["order_id"] == order_id:
            status = input(
                "Enter the new status (Preparing/Ready/Pickup/Delivered): ")
            order["status"] = status
            print(f"Status for order with ID {order_id} changed to {status}.")
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
