from flask import Flask, request, render_template, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

""" Forex Converter """
c = CurrencyRates()
s = CurrencyCodes()

URL = "http://127.0.0.1:5000"


@app.route("/")
def home():
    """Home Page"""

    # r = requests.get(URL)
    # print(r.status_code)
    return render_template("index.html")

# TODO: redirect 500 status code
# TODO: display error messages when status code response is 500


@app.route("/convert")
def calc_page():
    """Converts currencies"""

    r = requests.get(URL)

    if r.status_code == 500:
        return redirect("/")
    else:
        cur1 = request.args["cur1"].upper()
        cur2 = request.args["cur2"].upper()
        sym1 = s.get_symbol(cur1)
        sym2 = s.get_symbol(cur2)

        amount = float(request.args["amount"])

        convert = round(c.convert(cur1, cur2, amount), 2)

        amount = round(amount, 2)

        return render_template("results.html",
                               cur1=cur1,
                               cur2=cur2,
                               sym1=sym1,
                               sym2=sym2,
                               amount=amount,
                               convert=convert)
