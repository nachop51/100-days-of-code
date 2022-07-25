from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/username/<name>')
def greet(name):
    return (f'Hello, {name}!')


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run(debug=True)
