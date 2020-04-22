from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
# from flask_debugtoolbar import DebugToolbarExtension
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
# app.debug = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

""" Forex Converter """
c = CurrencyRates()
s = CurrencyCodes()

URL = "http://127.0.0.1:5000"


@app.route("/")
def home():
    """Home Page"""

    return render_template("index.html")


@app.route("/convert")
def calc_page():
    """Converts currencies"""

    r = requests.get(URL)
    print('STATUS CODE IS***********************************')
    print(r.status_code)

    cur1 = request.args["cur1"].upper()
    cur2 = request.args["cur2"].upper()
    sym1 = s.get_symbol(cur1)
    sym2 = s.get_symbol(cur2)

    amount = float(request.args["amount"])

    try:
        convert = round(c.convert(cur1, cur2, amount), 2)
    except:
        flash('Input not valid', 'danger')
        return redirect("/")

    amount = round(amount, 2)

    # flash('')
    return render_template("results.html",
                           cur1=cur1,
                           cur2=cur2,
                           sym1=sym1,
                           sym2=sym2,
                           amount=amount,
                           convert=convert)
