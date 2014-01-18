from Rupert import Rupert
from flask import Flask, render_template
import datetime

app = Flask(__name__)
rupert = Rupert()

@app.route("/")
def homepage():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")

	templateData = {
		"title": "Rupert",
		"time": timeString
	}
	return render_template('homepage.htm', **templateData)

@app.route("/move_forward")
def forward():
	rupert.runForward(40, 1)
	return "1"

@app.route("/move_fast-forward")
def fast_forward():
	rupert.runForward(100, 1)
	return "1"

@app.route("/move_left")
def left():
	rupert.turnLeft(40, 0.1)
	return "1"

@app.route("/move_right")
def right():
	rupert.turnRight(40, 0.1)
	return "1"

@app.route("/move_backward")
def backward():
	rupert.runBackward(40, 1)
	return "1"

@app.route("/move_fast-backward")
def fast_backward():
	rupert.runBackward(100, 1)
	return "1"

@app.route("/move_stop")
def stop():
	rupert.stopMotors()
	return "1"

if __name__ == "__main__":
	print "Controller website coming up on port 81"
	app.run(host="0.0.0.0", port=81, debug=True)


