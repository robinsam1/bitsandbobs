from flask import Flask,request,render_template
from calculator import calculator
calculator = calculator()
application = Flask(__name__)

@application.route('/')
def my_form():
    return render_template("my-form.html")

@application.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    x = calculator.calculate(float(text))
    return "%.2f" %x

if __name__ == "__main__":
     application.run(host='0.0.0.0')
