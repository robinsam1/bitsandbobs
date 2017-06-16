from flask import Flask, render_template

@application.route('/')
def showMachineList():
     return render_template('list.html')

if __name__ == "__main__":
     application.run(host='0.0.0.0')
