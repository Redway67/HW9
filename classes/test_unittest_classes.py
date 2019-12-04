from bag import Bag, QUANTITY_BARRELS
import unittest
import random


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        del self.bag

    def test_init(self):
        self.assertEqual(len(self.bag.barrels), 90)

    def test_is_not_empty(self):
        self.assertTrue(self.bag.is_not_empty())

    def test_bag_get_barrel(self):
        self.assertTrue(random.choice(self.bag.barrels) in range(1, QUANTITY_BARRELS + 1))
