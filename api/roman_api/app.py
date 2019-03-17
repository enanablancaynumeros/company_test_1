import os

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import SubmitField, StringField

from .roman_calculator import roman_calculator, InvalidCalculatorInput


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = os.environ["APP_SECRET_KEY"]


@app.route("/", methods=["GET"])
def roman_calculator_get():
    form = RomanCalculatorForm()
    return render_template("roman.html", form=form)


@app.route("/", methods=["POST"])
def roman_calculator_post():
    form = RomanCalculatorForm(request.form)
    if form.validate_on_submit():
        try:
            roman_result = roman_calculator(form.data["roman_text"])
            flash(f'The result of "{form.data["roman_text"]}" is "{roman_result}"')
        except InvalidCalculatorInput:
            flash(f'Invalid input {form.data["roman_text"]}')

    return render_template("roman.html", form=form)


class RomanCalculatorForm(FlaskForm):
    roman_text = StringField("Roman input")
    submit = SubmitField("Submit")


if __name__ == "__main__":
    port = os.environ["API_PORT"]
    app.run(host="localhost", port=port)
