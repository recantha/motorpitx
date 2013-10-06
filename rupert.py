from Rupert import Rupert
from flask import Flask
import time

app = Flask(__name__)
rupert = Rupert()

@app.route("/")
def homepage():
	return "Hello world!"

@app.route("/forward")
def forward():
	rupert.runForward(40,1)
	return "Forward"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=81, debug=False)


