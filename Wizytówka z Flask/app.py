from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/mypage/me")
def card():
    return render_template("Wizytówka.html")


@app.route("/mypage/contact")
def contact():
    return render_template("Contact.html")
