import unittest

from src.food import Food
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("burger", 10.00, 5)

    def test_food_has_name(self):
        self.assertEqual("burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(10.00, self.food.price)

    def test_food_has_rejuvenation(self):
        self.assertEqual(5, self.food.rejuvenation_level)

    

