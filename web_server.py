from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return ("Hello Flask!")

@app.route("/mmecoco")
def homepage_mmecoco():
    return (render_template("test.html"))

@app.route("/user/<user_name>/<int:user_id>")
def dynamic_page(user_name, user_id):
    return f'Hello, {user_name}({user_id})'

if __name__ == "__main__":
    app.run()