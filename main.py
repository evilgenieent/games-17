#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid
#from django.utils import simplejson
from google.appengine.api import modules
from google.appengine.ext import ndb
from google.appengine.api import channel
from google.appengine.api import app_identity
from google.appengine.ext.webapp import template

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        module = modules.get_current_module_name()
        instance = modules.get_current_instance_id()
        # self.response.write('Module {0}, instance {1}'.format(module, instance))
        template_values = {'current_module_name': module,
                           'current_instance_id': instance
                          }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))       

class GameModel(ndb.Model):
    """All the data we store for a game"""
    date = ndb.DateTimeProperty(auto_now_add=True)
    
class Game:
    @classmethod
    def get_game_url(cls, user_id, game_id):
        return '/' + str(user_id) + '/game/' + str(game_id)

class NewGameHandler(webapp2.RequestHandler):
    def get(self, user_id):
        game = GameModel()
        game_key = game.put()
        uri = Game.get_game_url(user_id, game_key.id())
        return webapp2.redirect(uri)
        
class GameHandler(webapp2.RequestHandler):
    def get(self, user_id, game_id):
        if not game_id:
            return 'Missing game ID'

        if not user_id:
            self.response.write('Wrong user uuid')
            return
             
        token = channel.create_channel(user_id + game_id)
        game_link = app_identity.get_default_version_hostname() + \
            Game.get_game_url(user_id, game_id)
            
        template_values = {'token': token,
                           'game_id': game_id,
                           'game_link': game_link,
                           'initial_message': ''
                          }
        path = os.path.join(os.path.dirname(__file__), 'game.html')
        self.response.out.write(template.render(path, template_values))       

class OpenedPage(webapp2.RequestHandler):
    def post(self):
        pass
    # channel.send_message(self.game.userO.user_id() + self.game.key().id_or_name(), message)

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    webapp2.Route(r'/<user_id>/game/new', handler=NewGameHandler),
    webapp2.Route(r'/<user_id>/game/<game_id>', handler=GameHandler),
    (r'/opened', OpenedPage),
], debug=True)
