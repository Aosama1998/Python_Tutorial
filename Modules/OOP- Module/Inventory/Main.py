class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        """Displays product information."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity Available: {self.quantity}")
        print("-" * 30)

    def update_quantity(self, quantity_change):
        """Updates the quantity of a product (can be positive or negative)."""
        if self.quantity + quantity_change < 0:
            print("Not enough stock to remove that quantity.")
        else:
            self.quantity += quantity_change
            print(f"Updated quantity of {self.name}: {self.quantity}")

    def calculate_total_value(self):
        """Calculates the total value of the product in stock."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adds a new product to the inventory."""
        self.products.append(product)
        print(f"Added {product.name} to inventory.")

    def display_inventory(self):
        """Displays all products in the inventory."""
        for product in self.products:
            product.display_product_info()

    def calculate_total_inventory_value(self):
        """Calculates the total value of all products in the inventory."""
        total_value = sum(product.calculate_total_value() for product in self.products)
        print(f"Total value of inventory: ${total_value:.2f}")
        return total_value


# Create the inventory system
inventory = Inventory()

# Adding products
product1 = Product("Laptop", 1200.00, 5)
product2 = Product("Headphones", 150.00, 10)
product3 = Product("Mouse", 25.00, 20)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Display the inventory
inventory.display_inventory()

# Update quantities
product1.update_quantity(-2)  # Sold 2 laptops
product2.update_quantity(5)   # Restocked 5 headphones

# Display the inventory again
inventory.display_inventory()

# Calculate and display the total value of the inventory
inventory.calculate_total_inventory_value()
