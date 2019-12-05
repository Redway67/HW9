from classes.bag import Bag, QUANTITY_BARRELS
from classes.card import Card
from classes.player import Player, Human, Computer
from classes.game import Game

import unittest
from unittest.mock import patch
import random
from io import StringIO


class TestGame(unittest.TestCase):

    def setUp(self):
        self.loto = Game()

    def tearDown(self):
        del self.loto

    def test_loto_init(self):
        self.assertEqual(self.loto.lap, 1)
        self.assertTrue(self.loto.is_running)

    def test_loto_pull_out_barrel(self):
        self.assertTrue(self.loto.pull_out_barrel() in range(1, QUANTITY_BARRELS + 1))


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def tearDown(self):
        del self.player

    def test_player_init(self):
        self.assertEqual(self.player.number, 1)
        self.assertEqual(self.player.who, 0)
        self.assertTrue(self.player.is_playing)

    def test_player_show_cards(self):
        with patch('sys.stdout', new=StringIO()) as print_text:
            self.player.show_cards()
            self.assertTrue(print_text)

    def test_player_move_on(self):
        self.assertEqual(self.player.move_on(1), 0)


class TestComputer(unittest.TestCase):

    def setUp(self):
        self.comp_player = Computer(1)

    def tearDown(self):
        del self.comp_player

    def test_move_on(self):
        self.assertFalse(self.comp_player.move_on(70))


class TestHuman(unittest.TestCase):

    def setUp(self):
        self.hum_player = Human(1)

    def tearDown(self):
        del self.hum_player

    def test_move_on(self):
        self.assertFalse(self.hum_player.move_on(70))


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
        with patch('sys.stdout', new=StringIO()) as print_text:
            self.card.show_card()
            self.assertTrue(print_text)