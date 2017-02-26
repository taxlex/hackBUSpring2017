from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')
 
@app.route('/about')
def login():
    return render_template('login.html')
  
@app.route('/contactUs')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
