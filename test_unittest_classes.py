from classes.bag import Bag, QUANTITY_BARRELS
from classes.card import Card, CARD_FILLED_BOX
from classes.player import Player
from classes.game import Game

import unittest
import random


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        del self.bag

    def test_bag_init(self):
        self.assertEqual(len(self.bag.barrels), 90)
        self.assertTrue(self.bag.barrels)

    def test_shake_bag(self):
        self.bag.shake_bag()
        self.assertEqual(len(self.bag.barrels), 90)

    def test_throw_out_barrel(self):
        self.bag.throw_out_barrel(70)
        self.assertTrue(self.bag.barrels)

    def test_bag_get_barrel(self):
        self.bag.get_barrel()
        self.assertTrue(random.choice(self.bag.barrels) in range(1, QUANTITY_BARRELS + 1))

    def test_bag_is_not_empty(self):
        self.assertTrue(self.bag.is_not_empty())


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(1)

    def tearDown(self):
        del self.card

    def test_card_init(self):
        self.assertEqual(self.card.number, 1)

    def test_card_close_box(self):
        self.card.close_box(3)
        self.assertLess(self.card.field[3], 91)

    def test_card_is_empty(self):
        self.assertTrue(self.card.is_empty())

    def test_show_card(self):
        pass


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def tearDown(self):
        del self.player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.loto = Game()

    def tearDown(self):
        del self.loto



