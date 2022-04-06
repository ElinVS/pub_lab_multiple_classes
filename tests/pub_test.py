import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Bulls Head", 500.00)


    def test_pub_has_name(self):
        self.assertEqual("The Bulls Head",self.pub.name)

    def test_pub_has_money_in_till(self):
        self.assertEqual(500.00,self.pub.till)