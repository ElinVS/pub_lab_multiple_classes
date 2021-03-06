import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("beer", 5.00, 1, 100) #165
        self.drink_2 = Drink("wine", 6.50, 2, 10)
        self.drink_3 = Drink("tequila", 3.00, 3, 5)
        self.drink_4 = Drink("margarita", 7.50, 4, 50)
        self.customer_1 = Customer("Spike", 10.00, 17, 5)
        self.customer_2 = Customer("Chris", 100.00, 50, 2)
        self.pub = Pub("The Bulls Head", 500.00, [self.drink_1,self.drink_2, self.drink_3, self.drink_4])



    def test_pub_has_name(self):
        self.assertEqual("The Bulls Head",self.pub.name)

    def test_pub_has_money_in_till(self):
        self.assertEqual(500.00,self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(4,len(self.pub.drinks))

    def test_till_has_increased(self):
        self.pub.increase_till(self.drink_4.price)
        self.assertEqual(507.50, self.pub.till)

    def test_can_drink__true(self):
        self.assertEqual("Come on in!",self.pub.can_drink(self.customer_2.age))

    def test_can_drink__false(self):
        self.assertEqual("Get lost loser",self.pub.can_drink(self.customer_1.age))

    def test_refuse_service__True(self):
        self.customer_3 = Customer("Lucy", 200.00, 65, 15)
        self.assertEqual("You have had too many",self.pub.refuse_service(self.customer_3.drunkeness))

    def test_refuse_service__False(self):
        self.assertEqual(None, self.pub.refuse_service(self.customer_1.drunkeness))

    def test_total_stock(self):
        self.assertEqual(165, self.pub.drinks)