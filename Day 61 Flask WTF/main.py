from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, ValidationError, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = 'clave-secreta'
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log in')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)