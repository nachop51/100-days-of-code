from flask import Flask, render_template
from random import randint
import requests
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    random = randint(1, 100)
    date = datetime.now()
    copy = f"Copyright {date.year}. Built by Nacho Peralta"
    return render_template('index.html', num=random, copy=copy)


@app.route('/guess/<name>')
def guess(name):
    name = name.capitalize()
    response = requests.get(f'https://api.agify.io?name={name}')
    age = response.json()['age']
    response = requests.get(f'https://api.genderize.io?name={name}')
    gender = response.json()['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
