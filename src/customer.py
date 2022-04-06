class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def buy_a_drink(self,price, strength):
        self.wallet -= price
        self.drunkeness += strength
        
    def eat_food(self, price, rejuvenation_level):
        self.wallet -= price
        self.drunkeness -= rejuvenation_level