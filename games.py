#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from google.appengine.ext import ndb

import cardsdeck

class PlayerModel(ndb.Model):
    user_id = ndb.IntegerProperty(required = True)
    cards = ndb.StringProperty(indexed = False)
    
class Player(object):
    number = None   # number of the player in a game
    def __init__(self, user):
        self._user = user
        self.populate(user_id = user.id())
        
    def user_id(self):
        return self._user.id()
    
    def get_ouside_view(self):
        return {
            'nick': self._user.email(),
            'num_cards': len(self.hand)
            }

    def get_inside_view(self):
        view = self.get_inside_view()
        view.cards = self._cards
        return view
        
class GameModel(ndb.Model):
    """All the data we store for a game"""
    date = ndb.DateTimeProperty(auto_now_add=True)
    player = ndb.StructuredProperty(Player, repeated = True)
    deck = ndb.StringProperty(indexed = False)
    table = ndb.StringProperty(indexed = False)
    
class Game(object):
    _deck = None    # current deck of cards
    _players = []   # list of players
    _table = None   # cards that are not at hands nor in the deck
    _turn = 0       # index of player whose turn it is now
    
    def __init__(self):
        self._deck = cardsdeck.Deck()
        self._model = GameModel()
            
    @staticmethod
    def load(game_id):
        self = Game() 
        self._model = GameModel.get_by_id(game_id)
        if not self._model:
            raise KeyError
        return self
            
    def save(self):
        self._model.deck = str(self._deck)
        self._model.table = str(self._table)
        return self._model.put().id()
    
    def get_name(self):
        return str(self._model.key.id())
    
    def get_url(self):
        return Game.get_game_url(self._model.key.id())
    
    @staticmethod
    def get_game_url(game_id):
        return '/game/' + str(game_id)
    
    @staticmethod
    def find_games():
        current_games = GameModel.query().fetch()
        result = []
        for g in current_games:
            result.append(Game(g))
        return result
    
class Thousand(Game):
    DECK_SIZE = 24 # from 9 to Ace
    WIDOW_SIZE = 3
    PLAYERS_COUNT = 3
    INITIAL_HAND_SIZE = (DECK_SIZE - WIDOW_SIZE) / PLAYERS_COUNT
      
    def add_player(self, user):
        if len(self._players) < Game.MAX_PLAYERS:
            player = Player(user)
            player.number = len(self._players) 
            self._players.append(player)

            # TODO: cards should be dealt only when game starts
            player.cards = self._deck.deal_many(Thousand.INITIAL_HAND_SIZE)
            
            return player
        else:
            raise OverflowError('Max number of players ({0}) reached' % Game.MAX_PLAYERS)

    @classmethod
    def _get_neigbor_indexes(cls, my_index):
        if my_index == 0:
            return (1,2)
        elif my_index == 1:
            return (2,0)
        elif my_index == 2:
            return (0,1)
        else:
            raise KeyError("Index must be from 0 to {0}" % cls.PLAYERS_COUNT)

    def _get_neigbors(self, player):
        left_index, right_index = self._get_neigbor_indexes(player.number)
        left = None
        right = None
        if len(self._players) < left_index:
            left = self._players[left_index]
        if len(self._players) < right_index:
            right = self._players[right_index]
        return (left, right)
        
    def _find_player(self, user):
        for p in self._players:
            if p.user_id() == user.id():
                return p
        return None

    def get_user_view(self, user):
        player = self._find_player(user)
        left, right = self._get_neigbors(player)

        view = {
            'deck_count': len(self._cards),
            'table_cards': str(self._table),
            'left_player': left.get_outside_view(),
            'right_player': right.get_outside_view(),
            'me': player.get_inside_view()
            }
        return view 
        
        
        