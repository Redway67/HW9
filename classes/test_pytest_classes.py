from bag import Bag


class TestBag:

    def setup(self):
        self.bag = Bag()

    def teardown(self):
        pass

    def test_bag_init(self):
        assert len(self.bag.barrels) == 90

    def test_bag_is_not_empty(self):
        assert self.bag.is_not_empty()
