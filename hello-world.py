from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!!!'

a = "Sri Rama"
@app.route('/welcome')
def welcome():
    return a



if __name__ == '__main__':
    app.run(debug=True)
