## This is a simple flask application to demonstrate the use of redirect and url_for
## The app will run on the local server and will display the message on the browser
## this is for rendering templates/index.html 

from flask import Flask,render_template

app = Flask(__name__)

### This route will render the index.html template
@app.route('/')
def hello():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
