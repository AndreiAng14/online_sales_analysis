from product_manager import ProductManager
from product import Product
from cart import Cart
import random

product_manager=ProductManager()
cart=Cart()

products=[
    Product('Laptop Gaming Asus',2_3455.56,100),
    Product('Televizor Samsung',1_1234,10),
    Product('Cuptor Microunde Beko',455.01,54),
    Product('Frigider Artic',6_3455.99,40),
    Product('Tastatura Logitech',34,166),
]

def add_product(products):
    for p in products:
        product_manager.add_product(p)

def show_products():
    print('')
    product_manager.show_all()

def show_total():
    print('')
    product_manager.average()

def remove_product(name):
    print('')
    product_manager.remove_by_name(name)

def add_3_random_products():
    print('')
    random_prod=random.sample(range(len(products)),3)
    for r in random_prod:
        cart.add_product(products[r])

def total_cart():
    print('')
    cart.total_value()

def view_cart():
    print('')
    cart.show()

# add_product(products)
# show_products()
# show_total()
# remove_product()
add_3_random_products()
total_cart()
view_cart()