from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4
import json

from flask_debugtoolbar import DebugToolbarExtension

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.route("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.route("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return {"gameId": game_id, "board": game.board}

@app.route('/api/score-word', methods=['POST'])
def score_word():
    # print(request.data)
    # request_data = json.loads(request.data)
    

    word = request.json['word']
    game_id = request.json['gameId']
    print('game ID is ', game_id)
    print(word)
    print(games)


    game = games[game_id]
    print(game)

    is_in_word_list = game.is_word_in_word_list(word)
    is_word_on_board = game.check_word_on_board(word)

    if not is_in_word_list:
        return jsonify({'result': 'not-word'})
    
    if not is_word_on_board:
        return jsonify({'result': 'not-on-board'})

    return jsonify({'result': 'ok'})