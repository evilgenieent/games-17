'''
Created on 4 Nov 2013

@author: burnevsk
'''
import random

Suits = ['s','c','d','h']
Faces = ['a','k','q','j','10','9','8','7','6','5','4','3','2']
Jokers = ['r','b']

class Pack(object):
    ''' Base class, which just stores a list of cards '''
    _cards = []

    def __repr__(self):
        return ' '.join(self._cards)

class Hand(Pack):
    ''' Represents cards that a player has at hands '''
    def __init__(self, size):
        self._max_size = size
        
class Deck(Pack):
    ''' Represents a deck of playing cards, with utilities '''
    def __init__(self, size):
        self._cards = Deck.create_deck(size)
        random.shuffle(self._cards)
        
    def deal_one(self):
        return self._cards.pop()
        
    def deal_many(self, count):
        if count < len(self._cards):
            raise IndexError
        cards = []
        for k in range(count):
            cards.append(self._cards.pop())
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
        for s in Suits:
            for f in range(family):
                cards.append(s + Faces[f])
        if useJokers:
            cards.append(Jokers)
        return cards
            
