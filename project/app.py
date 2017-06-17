from flask import Flask,render_template
from calculator import calculator
calculator = calculator()
application = Flask(__name__)

@application.route('/')
def showMachineList():
     #return render_template('list.html')
     x = calculator.calculate(0)
     return "%.2f" %x

if __name__ == "__main__":
     application.run(host='0.0.0.0')
