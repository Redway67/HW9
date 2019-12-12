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

    def test___str__(self):
        self.assertTrue(self.loto.__str__())


    class TestPlayer(unittest.TestCase):

        def setUp(self):
            self.player = Player('', 1, 0)

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

        def test___str__(self):
            self.assertTrue(self.player.__str__())

    class TestComputer(unittest.TestCase):

        def setUp(self):
            self.comp_player = Computer(1)

        def tearDown(self):
            del self.comp_player

        def test_computer_move_on(self):
            barrel = 70
            if self.comp_player.cards.is_empty():
                self.assertEqual(self.comp_player.move_on(barrel), 0)

    class TestHuman(unittest.TestCase):

        def setUp(self):
            self.hum_player = Human(1)

        def tearDown(self):
            del self.hum_player

        def test_human_move_on(self):
            barrel = 90
            if self.hum_player.cards.is_empty():
                self.assertLessEqual(self.hum_player.move_on(barrel), 0)

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

        def test___str__(self):
            self.assertTrue(self.bag.__str__())

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

        def test___str__(self):
            self.assertTrue(self.card.__str__())
