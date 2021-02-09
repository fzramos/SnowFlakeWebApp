from flask import Flask

app = Flask("my website")

@app.route('/')
def homepage():
    return 'Welcome to my website!'

app.run()
