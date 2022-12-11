# print("hello world")
from flask import Flask, render_template , request   
# import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/signup', methods= ['POST', 'GET'])
def signup():
    return render_template('signup.html')


@app.route('/validation', methods = ['POST', 'GET'])
def login_validation():
    if request.method == "POST":
        result = request.form 
        return f"email id is : {result['email']}"





if __name__ == '__main__':
    app.run(debug=True)




