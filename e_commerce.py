
import time
# Available products (id, name, price)
products = {
    1: {"name": "Laptop", "price": 15000},
    2: {"name": "Mouse", "price": 300},
    3: {"name": "Keyboard", "price": 800},
    4: {"name": "Monitor", "price": 4500}
}

# Shopping cart (list of product IDs)
cart = []

def show_products():
    print("\n=== Available Products ===")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ${info['price']}")

def add_to_cart(pid):
    if pid in products:
        cart.append(pid)
        print(f"{products[pid]['name']} added to cart.")
    else:
        print("Error: Product does not exist.")

def view_cart():
    if not cart:
        print("\nCart is empty")
        return
    
    print("\n=== Shopping Cart ===")
    total = 0
    for i, pid in enumerate(cart, 1):
        product = products[pid]
        print(f"{i}. {product['name']} - ${product['price']}")
        total += product["price"]
    print(f"Total: ${total}")

def checkout():
    if not cart:
        print("\nCannot checkout: the cart is empty.")
        return
    
    view_cart()
    print("Checkout completed. Thank you for your purchase!")
    cart.clear()

def menu():
    while True:
        print("\nOptions: products, add, cart, checkout, exit")
        option = input("Choose an option: ")

        start = time.time()

        if option == "products":
            show_products()
        elif option == "add":
            try:
                pid = int(input("Enter the product ID: "))
                inner_start = time.time() 
                add_to_cart(pid)
                inner_end = time.time()
                print(f"Response time (add): {inner_end - inner_start:.3f} seconds")
            except ValueError:
                print("Error: ID must be numeric.")
        elif option == "cart":
            view_cart()
        elif option == "checkout":
            checkout()
        elif option == "exit":
            print("Exiting system...")
            break
        else:
            print("Invalid option.")

        end = time.time()
        if option != "add":
            print(f"Response time: {end - start:.3f} seconds")

if __name__ == "__main__":
    # Se mide el tiempo de respuesta
    menu()
