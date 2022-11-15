from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def my_form():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password_text')
        return f"<h1>Name: {name }, password:{password} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
