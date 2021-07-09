from unittest import TestCase

from app import app, games

import json

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            ...
            # test that you're getting a template
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board">', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            # write a test for this route
            response = client.get('/api/new-game')
            response_data = json.loads(response.get_data(as_text=True)) 

            """This tests that the route is working properly"""
            self.assertEqual(response.status_code, 200)

            """This tests that the response data has a key of 'gameId'"""
            self.assertIn('gameId', response_data)
            # self.assertIn('gameId', response_data.keys())

            """This tests that game_id is a string"""
            self.assertIsInstance(response_data['gameId'], str)

            """This tests that game.board is a list"""
            self.assertIsInstance(response_data['board'], list)

            """This tests that the game instance exists in the games dictionary"""
            self.assertIn(response_data['gameId'], games)

