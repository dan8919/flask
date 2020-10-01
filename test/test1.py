from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!'


@app.route('/godjob')
def good_job():
    return "god job!"