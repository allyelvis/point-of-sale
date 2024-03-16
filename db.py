import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

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
        self.connection = sqlite3.connect('pos_database.db')
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.populate_initial_data()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products
                               (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)''')

    def populate_initial_data(self):
        # Sample data for demonstration
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))
        self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", ('T-shirt', 20.0, 50))
        self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", ('Jeans', 50.0, 30))
        self.connection.commit()

    def authenticate_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def add_product_to_inventory(self, product):
        self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                            (product.name, product.price, product.quantity))
        self.connection.commit()

    def display_inventory(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        for product in products:
            print(f"{product[0]}: {product[1]} - ${product[2]}")

    def process_sale(self, shopping_cart):
        total_amount = shopping_cart.calculate_total()
        print(f"Total amount: ${total_amount}")
        # Implement payment processing logic here

    def __del__(self):
        self.connection.close()

# Example usage:
pos_system = POSSystem()

username = input("Enter username: ")
password = input("Enter password: ")

if pos_system.authenticate_user(username, password):
    print("Authentication successful!")
    pos_system.display_inventory()

    cart = ShoppingCart()
    product_id = int(input("Enter product ID to add to cart: "))
    quantity = int(input("Enter quantity: "))

    pos_system.add_product_to_inventory(Product(3, "Socks", 5.0, 20))

    product = pos_system.cursor.execute("SELECT * FROM products WHERE id=?", (product_id,)).fetchone()
    cart.add_item(Product(product[0], product[1], product[2], product[3]), quantity)

    print("Items in the shopping cart:")
    for item in cart.items:
        print(f"{item['product'].name} - Quantity: {item['quantity']}")

    pos_system.process_sale(cart)
else:
    print("Authentication failed!")
