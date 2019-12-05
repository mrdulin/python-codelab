import unittest
from FrenchDeck import Card, FrenchDeck, spades_high


class TestFrenchDeck(unittest.TestCase):
    def setUp(self):
        self.deck = FrenchDeck()

    def test_len(self):
        self.assertEqual(len(self.deck), 52)

    def test_getitem(self):
        self.assertTupleEqual(self.deck[0], Card(rank='2', suit='spades'))
        self.assertTupleEqual(self.deck[1], Card(rank='3', suit='spades'))
        self.assertTupleEqual(self.deck[-1], Card(rank='A', suit='hearts'))

    def test_slice(self):
        self.assertEqual(self.deck[:2], [Card(
            rank='2', suit='spades'), Card(rank='3', suit='spades')])

        # get rank=A cards
        self.assertEqual(self.deck[12::13], [
            Card(rank='A', suit='spades'),
            Card(rank='A', suit='diamonds'),
            Card(rank='A', suit='clubs'),
            Card(rank='A', suit='hearts')
        ])

    def test_iterate(self):
        count = 0
        for card in self.deck:
            count += 1
        self.assertEqual(count, 52)

    def test_reversed_iterate(self):
        count = 0
        for car in reversed(self.deck):
            count += 1
        self.assertEqual(count, 52)

    def test_in_operator(self):
        self.assertEqual(Card(rank='Q', suit='hearts') in self.deck, True)
        self.assertEqual(Card(rank='7', suit='beasts') in self.deck, False)


class Test_spade_high(unittest.TestCase):
    def test_several_cards(self):
        deck = FrenchDeck()
        # spades: 2, 3, 4, 5
        self.assertEqual(spades_high(deck[0]), 3)
        self.assertEqual(spades_high(deck[1]), 7)
        self.assertEqual(spades_high(deck[2]), 11)
        self.assertEqual(spades_high(deck[3]), 15)
        # diamonds: 2
        self.assertEqual(spades_high(deck[13]), 0 * 4 + 1)

        cards_sorted = []
        for card in sorted(deck, key=spades_high):
            cards_sorted.append(card)
        self.assertEqual(cards_sorted[:4], [
            Card(rank='2', suit='clubs'),
            Card(rank='2', suit='diamonds'),
            Card(rank='2', suit='hearts'),
            Card(rank='2', suit='spades')
        ])


unittest.main()
