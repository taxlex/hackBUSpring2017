from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')
  
  
@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/ourDevs')
def ourDevs():
    return render_template('ourDevs.html')


if __name__ == '__main__':
    app.run(debug=True)
