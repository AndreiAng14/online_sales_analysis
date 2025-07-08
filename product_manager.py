class ProductManager:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)
        print(f'Produsul {product.name}, cu prețul de {product.price}$, a fost adăugat cu succes!')
    
    def show_all(self):
        for prod in self.products:
            print(f"Produsul {prod.name} are prețul de {prod.price} $ iar în stoc sunt {prod.quantity} de bucăți.")
        
    def average(self):
        print(f'Valoarea totală a inventarului este de {sum(product.price * product.quantity for product in self.products):.2f}$.')