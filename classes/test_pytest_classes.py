import pytest

from classes.bag import Bag


class TestBag:

    def setup(self):
        self.bag = Bag()

    def teardown(self):
        pass

    def test_init(self):
        assert len(self.bag.barrels) == 90
