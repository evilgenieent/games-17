'''
Created on 4 Nov 2013

@author: burnevsk
'''

import random

class CardsDeck(object):
    '''
    Represents a deck of playing cards, with utilities
    '''
    Suits = ['s','c','d','h']
    Faces = ['a','k','q','j','10','9','8','7','6','5','4','3','2']
    Jokers = ['r','b']

    def __init__(self, size):
        self.deck = CardsDeck.create_deck(size)
        random.shuffle(self.deck)
        
    def deal_one(self):
        return self.deck.pop()
        
    def deal_many(self, count):
        if count < len(self.deck):
            raise IndexError
        cards = []
        for k in range(count):
            cards.append(self.deck.pop())
        return cards

    @classmethod
    def create_deck(cls, size):
        '''
        Size should be one of:
            24 - from 9 to ace
            36 - from 6 to ace
            52 - full deck
            54 - full deck with jokers
        '''
        useJokers = (size == 54)
        family = size // 4
        cards = []
        for s in CardsDeck.Suits:
            for f in range(family):
                cards.append(s + CardsDeck.Faces[f])
        if useJokers:
            cards.append(CardsDeck.Jokers)
        return cards
            
        