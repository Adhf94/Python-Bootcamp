from flask import Flask, render_template, request, session
import datetime as dt
from api_calls import api_call
import requests

app = Flask(__name__)


@app.route('/')
def home():
    date_copy = dt.date.today().year
    return render_template('index.html', year=date_copy)


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form.get('text')
        llamado = api_call(text)
        nombre = text
        edad = llamado[0]
        gender = llamado[1]
        return render_template('guess.html', nombre=nombre,edad=edad,gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

