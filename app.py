from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def first():
    return "This is our first application for the batch of DATA SCIENCE 1.0"

@app.route('/success/<int:score>')
def success(score):
    return "Score obtained by him/her is"+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "He/She has failed exam due to less score and score is"+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks < 35:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score= marks))


if __name__ == '__main__':
    app.run(debug=True)
