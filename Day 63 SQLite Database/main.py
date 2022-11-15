from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Creando un nuevo record con sqlalchemy
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J.K Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
#
#     db.create_all()
#
with app.app_context():
    all_books = db.session.query(Book).all()
    print(all_books)