from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, my name is akash and this is my docker project'

@app.route('/akash')
def akash():
    return 'Server is up and running'
