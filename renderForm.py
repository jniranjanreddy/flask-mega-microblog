from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/success/<int:score>')
def success(score):
    return "<h1>The person has Passed and the marks is " + str(score) + "</h1>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has Failed and the marks is " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    # goto = ""
    if marks < 50:
        goto = 'fail'
    else:
        goto = 'success'
    return redirect(url_for(goto,score=marks))

if __name__ == '__main__':
    app.run(debug=True)
