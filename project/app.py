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
	if request.form["clothing"]:
		questionnaire["clothing"] = request.form["clothing"]
	if request.form["commute"]:
		questionnaire["commute"] = request.form["commute"]
	if request.form["transport"]:
		questionnaire["transport"] = request.form["transport"]
	if request.form["diet"]:
		questionnaire["diet"] = request.form["diet"]
	if request.form["flights"]:
		questionnaire["flights"] = request.form["flights"]
	if request.form["flightfrequency"]:
		questionnaire["flightfrequency"] = request.form["flightfrequency"]
	score = calculator.calculate(questionnaire)
	output = "%.2f" %score
	#return "Carbon footprint: " + output
	return render_template("output.html", output=output)

if __name__ == "__main__":
	application.run(host='0.0.0.0')
