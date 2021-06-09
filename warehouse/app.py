from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def title():
    return f"Witaj"


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("First_Name.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")


@app.route("/warehouse", methods = ['GET'])
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    error = ["hammer is broken!"]
    return render_template("Warehouse_Child.html", items=items, errors = error)



@app.route('/greeting')
def greeting():
    return render_template('greeting.html')
