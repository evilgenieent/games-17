'''
Created on 4 Nov 2013

@author: sergey.burnevsky@gmail.com
'''
import random

Suits = ['s','c','d','h']
Faces = ['a','k','q','j','t','9','8','7','6','5','4','3','2']
Jokers = ['r','b']

'''
Cards a represented by a list of 2-char strings, made up
by concatenating suit and face substrings, like "sq" - Queen of Spades.
Jokers a single-char strings.
'''

def to_string(cards):
    ''' Converts cards list to a single string, for serialization '''
    return ' '.join(cards)

def from_string(cards_str):
    ''' Parsers list of cards from a string created as by tostring()'''
    if isinstance(cards_str, basestring):
        cards = cards_str.split(' ')
        # TODO: check that every substring is correctly encoded card
        return cards
    else:
        raise TypeError('String is expected')

class Deck(object):
    ''' Represents a deck of cards, which should not be accessed directly '''
    def __init__(self, size):
        self._cards = Deck.create_deck(size)
        random.shuffle(self._cards)
        
    def deal_one(self):
        return self._cards.pop()
        
    def deal_many(self, count):
        if count > len(self._cards):
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
            cards.extend(Jokers)
        return cards
            
