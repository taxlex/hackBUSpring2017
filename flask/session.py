from flask import Flask, session, render_template, request, redirect, g, url_for
import os
class Account:
	def __init__(self, userName, passwordu):
		self.userName = userName
		self.passwordu = passwordu
	def validAccount(self, uname, passW):
		if(uname == self.userName and passW == self.passwordu):
			return True
		return False

usr1 = Account('lex','pass')

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = ''
	if request.method == 'POST':
		session.pop('user',None)
		if usr1.validAccount(request.form['username'], request.form['password']):
			session['user'] = request.form['username']
			return redirect(url_for('ourDevs'))
		else:
			error = 'Invalid username or password'
	return render_template('login.html', error=error)
  
@app.route('/getsession')
def getsession():
	if 'user' in session:
		return session['user']
		
	return 'not logged in' 
	
	
@app.route('/dropsession')
def dropsession():
	session.pop('user', None)
	return 'dropped'
	
	
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
