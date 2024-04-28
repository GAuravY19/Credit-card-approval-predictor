from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/check')
def check_eligibility():
    return render_template("eligibility.html")

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True)
