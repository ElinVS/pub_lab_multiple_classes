class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, price):
        self.till += price

    def can_drink(self, age):
        
        if age >= 18:
            return "Come on in!"

        return "Get lost loser"