from flask import Flask
application = Flask(__name__)

@application.route('/')

def hello_world():
    return 'Deploy flask to AWS'