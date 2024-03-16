class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_id):
        for item in self.items:
            if item['product'].id == product_id:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

class POSSystem:
    def __init__(self):
        self.inventory = []

    def add_product_to_inventory(self, product):
        self.inventory.append(product)

    def display_inventory(self):
        for product in self.inventory:
            print(f"{product.id}: {product.name} - ${product.price}")

    def process_sale(self, shopping_cart):
        total_amount = shopping_cart.calculate_total()
        print(f"Total amount: ${total_amount}")
        # Implement payment processing logic here

# Example usage:
pos_system = POSSystem()

product1 = Product(1, "T-shirt", 20.0, 50)
product2 = Product(2, "Jeans", 50.0, 30)

pos_system.add_product_to_inventory(product1)
pos_system.add_product_to_inventory(product2)

pos_system.display_inventory()

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)

print("Items in the shopping cart:")
for item in cart.items:
    print(f"{item['product'].name} - Quantity: {item['quantity']}")

pos_system.process_sale(cart)
