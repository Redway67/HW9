from classes.bag import Bag
import unittest


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        del self.bag

    def test_init(self):
        self.assertEqual(len(self.bag.barrels), 90)
