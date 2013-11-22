'''
Created on 22 Nov 2013

@author: sergey.burnevsky@gmail.com
'''
import unittest
import games
import cardsdeck

class UserStub(object):
    def __init__(self, uid):
        self.uid = uid
        self.nick = 'user' + str(uid)
    def id(self):
        return self.uid
    def nickname(self):
        return self.nick

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.user1 = UserStub(1)
        self.user2 = UserStub(2)
        self.user3 = UserStub(3)
        self.deck = cardsdeck.Deck(24)
        pass

    def tearDown(self):
        pass

    def testName(self):
        player1 = games.Player(self.user1)
        hand = self.deck.deal_many(10)
        player1.hand = hand[:]
        # check outside view 
        o = player1.get_outside_view()
        self.assertEqual(o['nick'], self.user1.nickname())
        self.assertEqual(o['num_cards'], len(hand))
        # check inside view
        i = player1.get_inside_view()
        self.assertEqual(i['nick'], self.user1.nickname())
        self.assertEqual(i['num_cards'], len(hand))
        self.assertEqual(i['cards'], cardsdeck.to_string(hand))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()