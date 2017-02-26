from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'this is the homepage'
	
@app.route('/profile/<username>')
def profile(username):
	return "Hey there %s" % username
if __name__ == "__main__":
	app.run(debug=True)
