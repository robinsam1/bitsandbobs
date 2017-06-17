from flask import Flask,render_template
from calculator import calculator
calculator = calculator()
application = Flask(__name__)

@application.route('/')
def showMachineList():
     #return render_template('list.html')
     input = raw_input("Choose a number")
     x = calculator.calculate(input)
     return "%.2f" %x

if __name__ == "__main__":
     application.run(host='0.0.0.0')
