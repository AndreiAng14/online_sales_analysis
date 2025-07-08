class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def show_info(self):
        return f'Numele produsului este:{self.name} avândul prețul de {self.price} $, iar pe stoc mai avem {self.quantity} bucăți.'
    
    def update_quantity(self,quantity):
        if quantity>0:
            self.quantity=quantity
            print(f'Pentru {self.name} noua cantitate este {quantity} bucăți.')
        else:
            print('Pentru a actualiza cu succes cantitatea trebuie să introduceți un număr mai mare ca 0!')