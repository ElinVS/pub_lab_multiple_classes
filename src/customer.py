class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_a_drink(self,price):
        self.wallet -= price
        