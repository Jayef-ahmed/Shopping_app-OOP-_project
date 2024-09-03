from product import *
class Customer:
    def __init__(self) -> None:
        self.customers = {} #{'email' : 'password'}

    def add_customer(self, email, password):
        if email in self.customers:
            print('This email is already used try another')
        else:
            self.customers[email] = password

    def buy_product(self, name, quantity, amount):
        for product in Seller.products:
            if name.lower() == product.name.lower():
                if quantity <= product.quantity:
                    if amount < product.price * quantity:
                        print(f"Amount Low. Please Pay Extra {(product.price * quantity)-amount}Taka")
                        return
                    else:
                        if amount == product.price * quantity:
                            print(f'{product.name} Purchase Successfully!')
                            product.quantity -= quantity
                            return
                        else:
                            print(f'{product.name} Purchase Successfully!')
                            print(f'Return money: {amount - (product.price * quantity)}')
                            product.quantity -= quantity
                            return
                else:
                    print("Not enough quantity")
                    return
            else:
                print('Product Not Found!!')
                return

class Seller:
    products = []
    def __init__(self) -> None:
        self.sellers = {} #{'email' : 'password'}

    def add_seller(self, email, password):
        if email in self.sellers:
            print('This email is already used try another')
        else:
            self.sellers[email] = password

    def add_product(self, name, price, quantity):
        product = Product(name,price, quantity)
        self.products.append(product)
