import unittest
try:
    import test.support as test_support
except ImportError:
    from test import test_support 

from pokereval.card import Card, InvalidCardError
from pokereval.hand_evaluator import HandEvaluator

class CardInitTestCase(unittest.TestCase):
    def test_rank(self):
        for i in range(2, 15):
            Card(i, 1)
        for i in range(2, 10):
            Card(str(i), 1)
        for i in ("T", "J", "Q", "K", "A"):
            Card(i, 1)
            Card(i.lower(), 1)

        with self.assertRaises(TypeError):
            Card({}, 1)
        with self.assertRaises(InvalidCardError):
            Card(1, 1)
        with self.assertRaises(InvalidCardError):
            Card(15, 1)

    def test_suit(self):
        for i in range(1, 5):
            Card(2, i)
        for i in ("s", "h", "d", "c"):
            Card(2, i)
            Card(2, i.upper())

        with self.assertRaises(TypeError):
            Card(2, [])
        with self.assertRaises(InvalidCardError):
            Card(2, 0)
        with self.assertRaises(InvalidCardError):
            Card(2, 5)      

class TwoCardsTestCase(unittest.TestCase):

    def test_two_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = []
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.52337858220211153)


class FiveCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.9250693802035153)


class SixCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3), Card(5, 3)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.4405797101449275)


class SevenCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3), Card(5, 3), Card(5, 4)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.8909090909090909)


def test_main():
    test_support.run_unittest(
        CardInitTestCase,
        TwoCardsTestCase,
        FiveCardsTestCase,
        SixCardsTestCase,
        SevenCardsTestCase,
    )


if __name__ == "__main__":
    test_main()