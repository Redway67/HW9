from bag import Bag
import unittest


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        del self.bag

    def test_init(self):
        self.assertEqual(len(self.bag.barrels), 90)

    def test_is_not_empty(self):
        self.assertTrue(self.bag.is_not_empty())
