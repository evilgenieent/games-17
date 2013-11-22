
import unittest
import cardsdeck

class Test(unittest.TestCase):

    def setUp(self):
        #self.deck = cardsdeck.Deck(36)
        pass 
    
    def testInit(self):
        deck24 = cardsdeck.Deck(24)
        self.assertEqual(len(deck24._cards), 24)
        self.assertNotIn('r', deck24._cards)
        self.assertNotIn('b', deck24._cards)

        deck36 = cardsdeck.Deck(36)
        self.assertEqual(len(deck36._cards), 36)
        for c in deck24._cards:
            self.assertIn(c, deck36._cards)
        self.assertNotIn('r', deck36._cards)
        self.assertNotIn('b', deck36._cards)
        
        deck52 = cardsdeck.Deck(52)
        self.assertEqual(len(deck52._cards), 52)
        for c in deck36._cards:
            self.assertIn(c, deck52._cards)
        self.assertNotIn('r', deck52._cards)
        self.assertNotIn('b', deck52._cards)
        
        deck54 = cardsdeck.Deck(54)
        self.assertEqual(len(deck54._cards), 54)
        for c in deck52._cards:
            self.assertIn(c, deck54._cards)
        self.assertIn('r', deck54._cards)
        self.assertIn('b', deck54._cards)

    def testDeal(self):
        COUNT = 36
        deck = cardsdeck.Deck(COUNT)
        # check len is requested size
        self.assertEqual(len(deck._cards), COUNT)
        # check dealt card is removed
        card = deck.deal_one()
        self.assertEqual(len(deck._cards), COUNT-1)
        self.assertNotIn(card, deck._cards)
        # check dealt cards are removed
        cards = deck.deal_many(COUNT//2)
        self.assertEqual(len(deck._cards), COUNT - 1 - COUNT//2)
        for c in cards:
            self.assertNotIn(c, deck._cards)
        # check all will be removed
        deck.deal_many(COUNT - 1 - COUNT//2)
        self.assertEqual(len(deck._cards), 0)
        
    def testConversion(self):
        deck = cardsdeck.Deck(36)
        s = cardsdeck.to_string(deck._cards)
        deck2 = cardsdeck.from_string(s)
        self.assertSequenceEqual(deck._cards, deck2)
        
        aces = cardsdeck.from_string('sa ca da ha')
        self.assertEqual(len(aces), 4)
        self.assertSequenceEqual(['sa', 'ca', 'da', 'ha'], aces)
        
        inval = cardsdeck.from_string('ss cc dd hh')
        self.assertEqual(len(inval), 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDeal']
    unittest.main()