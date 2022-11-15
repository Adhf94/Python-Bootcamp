from flask import Flask


def make_bold(function):
    def wrapper():
        return f"<b> {function()} </b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
def say_bye():
    return "Bye"


#Creating variable paths and coverting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def name(name, number):
    return f"{name }, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
