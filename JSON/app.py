import csv
import pandas
import requests
from flask import Flask, render_template, request
app = Flask(__name__)
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data = data[0]
data = data["rates"]
csv_columns = ['currency', 'code', 'bid', 'ask']
csv_file = 'test.csv'
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for values in data:
            writer.writerow(values)
except IOError:
    print("I/O error")

reader = csv.reader(open("test.csv"), delimiter=',')
writer = csv.writer(open("new.txt", 'w'), delimiter=';')
writer.writerows(reader)

column_code = pandas.read_csv('test.csv', names=csv_columns)
code = column_code.code.tolist()
code[0] = None

column_bid = pandas.read_csv('test.csv', names=csv_columns)
bid = column_bid.bid.tolist()
print(bid)
calculation=0

@app.route("/", methods = ['POST', 'GET'])
def currency_lib():
    global calculation
    if request.method == "POST":
        form_data = request.form
        currenc = form_data.get('currency')
        amount = form_data.get('amount')
        print(currenc)
        print(amount)
        for index, item in enumerate(code):
            if item == currenc:
                calculation = float(bid[index]) * int(amount)

    return render_template('Kantor.html', item=code, calculation=calculation)

