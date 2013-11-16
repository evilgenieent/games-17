#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from google.appengine.ext import ndb

class GameModel(ndb.Model):
    """All the data we store for a game"""
    date = ndb.DateTimeProperty(auto_now_add=True)
    
class Game(object):
    def __init__(self, game_model = None, game_id = None):
        if game_model:
            self.model = game_model
        elif game_id:
            self.model = GameModel.get_by_id(game_id)
            if not self.model:
                raise KeyError
        else:
            self.model = GameModel()
            
    def save(self):
        return self.model.put().id()
    
    def get_name(self):
        return str(self.model.key.id())
    
    def get_url(self):
        return Game.get_game_url(self.model.key.id())
    
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

