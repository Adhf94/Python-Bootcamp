from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = 'e,mail'
MY_PASSWORD = 'password'


posts = requests.get('https://api.npoint.io/95daf9ec24e7ca833d6c').json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        print(blog_post["id"])
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)