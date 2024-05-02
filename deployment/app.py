from flask import Flask, render_template, request, redirect, url_for
from .utils.make_prediction import MakePredictions

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/check', methods = ['GET', 'POST'])
def check_eligibility():

    if request.method == 'POST':
        AGE = int(request.form['age_value'])
        REALTY = str(request.form['realty_value'])
        CNT_CHILD = str(request.form['children_value'])
        INCOME = int(request.form['income_value'])
        INCOME_TYPE = str(request.form['IncomeType_value'])
        EDUCATION = str(request.form['education_value'])
        MEMBER = int(request.form['FamilyMem_value'])
        OVERDUES = str(request.form['overdues_value'])
        EMPLOYMENT = int(request.form['emp_value'])
        OCCUPATION = str(request.form['Occupation_value'])
        HOUSE = str(request.form['house_value'])

        output = MakePredictions(AGE = AGE, REALTY = REALTY, CNT_CHILD = CNT_CHILD,
                        INCOME=INCOME, INCOME_TYPE=INCOME_TYPE, EDUCATION=EDUCATION, MEMBER=MEMBER,
                        OVERDUES=OVERDUES, EMPLOYMENT=EMPLOYMENT, OCCUPATION=OCCUPATION, HOUSE=HOUSE)


        return redirect(url_for('result', predicted_value = output))

    return render_template("eligibility.html")

@app.route('/result', methods = ['GET', 'POST'])
def result():

    predicted_value = request.args.get('predicted_value')
    return render_template("result.html", predicted_value=predicted_value)

if __name__ == "__main__":
    app.run(debug = True)
