from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return (render_template("index.html"))

@app.route("/game")
def homepage_game():
    print("출력")
    return (render_template("game.html"))

if __name__ == "__main__":
    app.run()