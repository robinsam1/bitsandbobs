from flask import Flask,request,render_template
from calculator import calculator
calculator = calculator()
application = Flask(__name__)

@application.route('/')
def my_form():
    return render_template("my-form.html")

@application.route('/', methods=['POST'])
def my_form_post():
    questionnaire = {}
    if request.form["commute"]:
    	questionnaire["commute"] = request.form["commute"]
    questionnaire["transport"] = request.form["transport"]
    questionnaire["diet"] = request.form["diet"]
    score = calculator.calculate(questionnaire)
    return "Carbon footprint: %.2f kg CO2/day" %score

if __name__ == "__main__":
     application.run(host='0.0.0.0')
