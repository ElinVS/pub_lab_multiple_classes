class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks   # or empty list [] - either works

    def increase_till(self, price):
        self.till += price

    def can_drink(self, age):

        if age >= 18:
            return "Come on in!"

        return "Get lost loser"

    def refuse_service(self, drunkenness):
        if drunkenness > 10:
            return "You have had too many"
        
    # def count_total_stock(self):
    #     total = 0

    #     for stock in self.drinks[stock_level]:

               
        