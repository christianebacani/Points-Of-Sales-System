class Product:
    def __init__(self):
        # Initialize an empty dictionary to store products and their quantities
        self.inventory = {}

    def addProduct(self, productName, quantity):
        # Check if the product is not already in the inventory
        if productName not in self.inventory:
            # If not, add the product with its name and quantity
            self.inventory[productName] = {"Product Name": productName, "Quantity": quantity}
        else:
            # If the product is already in the inventory, print a message indicating so
            print("'" + productName + "' already added to the inventory!")

    def displayProduct(self):
        # Display current inventory
        print("\nCurrent Inventory\n")

        # Loop through each product in the inventory
        for product, details in self.inventory.items():
            # Print product name and quantity
            print(f"Product Name : {product}\nQuantity : {details['Quantity']}")


class PointsOfSales:
    def __init__(self):
        # Initialize an empty dictionary to store product sales
        self.inventory = {}

    def addSales(self, productName, sales):
        # Add the sales data for a specific product
        self.inventory[productName] = sales

    def displaySales(self):
        # Display previous sales data
        print("\nPrevious Sales\n")

        # Loop through each product in the sales inventory
        for product, previousSales in self.inventory.items():
            # Print the product name and its previous sales
            print(f"Previous Product Name : {product}\nPrevious Sales of the Product P : {previousSales}")

# Instantiate Product and PointsOfSales objects
productSystem = Product()
pointsOfSalesSystem = PointsOfSales()

# Welcome message and user input for name
print("Welcome to the Points of Sales System!")
username = str(input("Enter your name to start : "))

# Add products to inventory
while True:
    productName = str(input("Enter the name of the product to be added to the inventory : "))
    quantity = int(input("Enter the quantity of the product to be added to the inventory : "))

    productSystem.addProduct(productName, quantity)

    userAddProductAgain = str(input("Do you want to add more product to the inventory again (y/n)?: ")).lower()

    if userAddProductAgain != "y":
        break

# Display current inventory
productSystem.displayProduct()

# Add previous sales data
while True:
    previousProductName = str(input("Enter the name of the previous product to view the previous sales : "))
    salesOfThePreviousProduct = int(input("Enter the previous sales of the specific product : P "))

    pointsOfSalesSystem.addSales(previousProductName, salesOfThePreviousProduct)

    userAddPreviousSalesAgain = str(input("Do you want to view more product name/sales to the inventory again (y/n)?: ")).lower()

    if userAddPreviousSalesAgain != "y":
        break

# Display previous sales data
pointsOfSalesSystem.displaySales()























