import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Vicky", 50.00, 52, 0)
        self.drink = Drink("beer", 5.00, 1)

    def test_customer_has_name(self):
        self.assertEqual("Vicky",self.customer.name)

    def test_customer_has_money_in_wallet(self):
        self.assertEqual(50.00,self.customer.wallet)

    def test_customer_drunkeness(self):
        self.assertEqual(0, self.customer.drunkeness)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.drink.price,self.drink.strength) 
        self.assertEqual(45.00, self.customer.wallet)
        self.assertEqual(1, self.customer.drunkeness)
        