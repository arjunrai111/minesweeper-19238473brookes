from unittest import TestCase
from minesweeper import isMine

class TestboardClass(TestCase):
    def test_isMine(self):
        self.assertFalse(isMine(0))

    pass
