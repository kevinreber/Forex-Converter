from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

""" Forex Converter """
c = CurrencyRates()
s = CurrencyCodes()


@app.route("/")
def home():
    """Home Page"""

    return render_template("index.html")


@app.route("/convert")
def calc_page():
    """Converts currencies"""

    cur1 = request.args["cur1"].upper()
    cur2 = request.args["cur2"].upper()
    sym1 = s.get_symbol(cur1)
    sym2 = s.get_symbol(cur2)

    amount = float(request.args["amount"])

    try:
        """Try to convert user inputs"""
        convert = round(c.convert(cur1, cur2, amount), 2)

    except RatesNotAvailableError:
        """If fails redirected to homescreen"""
        flash('Input not valid', 'danger')
        return redirect("/")

    amount = round(amount, 2)

    flash('Success!', 'success')
    return render_template("results.html",
                           cur1=cur1,
                           cur2=cur2,
                           sym1=sym1,
                           sym2=sym2,
                           amount=amount,
                           convert=convert)
