from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":


        #Checking is the user already exists
        if User.query.filter_by(email=request.form.get('email')).first():
            #user already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))


        #Encrypting Password with  Werkzeug
        hash_and_salted_pass = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        user_name = request.form.get("name")
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_pass
            #to avoid the salt&hash method to be recorded in the database
            #password = hash_and_salted_password.split($)[2]
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets", name=user_name))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #Get email & password from form
        email = request.form.get('email')
        password = request.form.get('password')
        #find user in db
        user = User.query.filter_by(email=email).first()

        #if email doesnt exist
        if not user:
            flash("That email doesnt exist, try again")
        #incorrect password

        #Check stored password  hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash("Wrong password, Try again!")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
def secrets():
    user_name = request.args.get("name")
    return render_template("secrets.html", name=user_name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static", path='files/cheat_sheet.pdf',
                               as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True)
