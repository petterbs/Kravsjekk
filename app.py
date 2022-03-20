from rentekalkulator import Rentekalkulator
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, DateField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta, date

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"



mittBelop = 100
minRente = 0.085
minFraDato = datetime(2022,1,1)
minTilDato = datetime(2023,1,1)
minRentekalkulator = Rentekalkulator(mittBelop,minFraDato,minTilDato,minRente)

rentetom = ""



@app.route("/", methods=["GET", "POST"])
def home():
    form = Form(csrf_enabled=False)
    if form.validate_on_submit():
        mittBelop = float(form.belop.data)
        minFraDato = datetime.combine(form.fra.data, datetime.min.time())
        minTilDato = datetime.combine(form.til.data, datetime.min.time())
        minRentekalkulator2 = Rentekalkulator(mittBelop,minFraDato,minTilDato,minRente)
        renteskriv = str(minRentekalkulator2.forsinkelsesrente()).replace(".",",")
        return render_template("index.html", rente=renteskriv, dato=form.fra.data, form = form)
    return render_template("index.html", rente=rentetom, form = form)

class Form(FlaskForm):
    belop = StringField("Hovedstol", validators = [DataRequired()])
    fra = DateField("Fra dato")
    til = DateField("Til dato")
    regn = SubmitField("Regn!")
