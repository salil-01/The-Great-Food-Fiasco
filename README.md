
# The Great Food Fiasco App

The Food Management App is a command-line interface (CLI) application designed to help staff manage orders and inventory for a food establishment. It provides functionality for viewing the menu, adding and removing items, taking new orders, and changing the status of orders.

## Features

- View the menu: Staff can view all the items in the inventory as a menu, displaying the ID, name, and price, and stock of each item.

- Add items to the menu: Staff can add new items to the menu, providing the necessary details such as name, price, availability, and stock.

- Remove items from the menu: Staff can remove items from the menu that are no longer served. If the stock of an item becomes zero, its availability is automatically changed to "No".

- Update item availability and stock: Staff can update the availability of an item to "No" or "Yes". If the availability is changed to "No", the stock is automatically set to 0. If the availability is changed to "Yes", staff is prompted to enter the number of stocks.

- Take new orders: Staff can take new orders from customers. Each order is associated with a unique ID automatically generated by the system. The customer's name and the selected items are recorded, and the total price is calculated.

- Change order status: Staff can change the status of orders. The available status options are "Received", "Preparing", "Ready", "Pickup", and "Delivered".

## Prerequisites

- Python 3.x: The Food Management App is implemented in Python. Make sure you have Python installed on your system.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/salil-01/The-Great-Food-Fiasco.git
   ```

2. Navigate to the project directory:

   ```
   cd The-Great-Food-Fiasco
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```
   python main.py
   ```

2. Follow the prompts displayed in the CLI to perform various operations such as viewing the menu, adding items, taking orders, and changing order status.

3. Enjoy managing your food inventory and orders with ease!

## File Structure

The file structure of the project is as follows:

```
├── main.py              # Main script to run the Food Management App
├── menu.json            # JSON file containing the menu items
├── orders.json          # JSON file containing the orders
├── README.md            # Documentation file (you're currently reading it)
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

Thanks For Reading :)
