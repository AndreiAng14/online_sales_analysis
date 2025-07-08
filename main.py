from product_manager import ProductManager
from product import Product

product_manager=ProductManager()

products=[
    Product('Laptop Gaming Asus',2_3455.56,12),
    Product('Televizor Samsung',1_1234,10),
    Product('Cuptor Microunde Beko',455.01,5),
    Product('Frigider Artic',6_3455.99,44),
    Product('Tastatura Logitech',34,16),
]

def add_product(products):
    for p in products:
        product_manager.add_product(p)

def remove_product(name):
    print('')
    product_manager.remove_by_name(name)

add_product(products)
remove_product()

