from flask import Flask, render_template, request, redirect, app

main = Flask(__name__)


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("First_Name.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")
