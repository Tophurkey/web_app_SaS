from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/register/')
def register():
	return render_template("register.html")

@app.route('/scientist/')
def scientist():
	return render_template("scientist.html")

@app.route('/teacher/')
def teacher():
	return render_template("teacher.html")

@app.route('/dashboard/')
def dashboard():
	return render_template("dashboard.html")

@app.route('/header/')
def header():
	return render_template("header.html")

if __name__ == "__main__":
	app.run()
