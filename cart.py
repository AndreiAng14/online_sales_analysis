class Cart:
    def __init__(self):
        self.cart_items=[]

    def add_product(self,product):
        self.cart_items.append(product)
        print(f'Produsul {product.name} adăugat cu succes!')
        
    
    def total_value(self):
        print(f'Totalul este în valoare de {sum(p.price * p.quantity for p in self.cart_items):.2f}$.')

    def show(self):
        print('Coșul dvs conține următoarele produse:')
        for i in self.cart_items:
            print(f'Nume produs: {i.name}, preț: {i.price}$, cantitatea dorită:{i.quantity} de bucăți.')