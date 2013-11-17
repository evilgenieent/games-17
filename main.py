#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
# from django.utils import simplejson
from google.appengine.api import modules
from google.appengine.api import channel
from google.appengine.api import app_identity
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2

import games
import logs

class MainHandler(webapp2.RequestHandler):
    def get(self):
        module = modules.get_current_module_name()
        instance = modules.get_current_instance_id()
        # self.response.write('Module {0}, instance {1}'.format(module, instance))
        current_games = games.Game.find_games()
        template_values = {
            'current_module_name': module,
            'current_instance_id': instance,
            'current_games': current_games
            }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))       

class AuthHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.current_user = None
    
    def check_user(self):
        user = users.get_current_user()
        if user:
            self.current_user = user
        else:
            webapp2.redirect(users.create_login_url(self.request.url), abort = True)

class NewGameHandler(AuthHandler):
    def get(self):
        self.check_user()
        # create new game and save
        game = games.Game()
        game.save()
        # redirect client to this new game
        return webapp2.redirect(game.get_url())
        
class GameHandler(AuthHandler):
    def get(self, game_id):
        self.check_user()

        game = games.Game.load(game_id)
        player = game.add_player(self.current_user)

        token = channel.create_channel(player.user_id + game_id)
        game_link = app_identity.get_default_version_hostname() + game.get_url()
            
        template_values = {
            'token': token,
            'game_id': game_id,
            'game_link': game_link,
            'me': player.user_id,
            'game_state': game.get_user_view(player.user)
        }
        path = os.path.join(os.path.dirname(__file__), 'game.html')
        self.response.out.write(template.render(path, template_values))       

class OpenedPage(AuthHandler):
    def post(self):
        self.check_user()
        # channel.send_message(self.game.userO.user_id() + self.game.key().id_or_name(), message)

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/logs', logs.LogsPage),
    webapp2.Route(r'/game/new', handler=NewGameHandler),
    webapp2.Route(r'/game/<game_id>', handler=GameHandler),
    (r'/opened', OpenedPage),
], debug=True)

