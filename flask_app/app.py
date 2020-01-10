from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEYS'] = '1647f99d4020bfd77af8410fda6d83be'

posts = [
	{
		'steps': 'Go to URL',
		'action': 'navigate to',
		'element': 'selector',
		'input': 'google.com'
	},
	{
		'steps': 'click link',
		'action': 'click',
		'element': 'xpath',
		'input': 'submit'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return "<h1>Home Page</h1>"

@app.route('/about')
def about():
	return "<h1>About Page</h1>"

@app.route('/')
def index():
	return render_template('template.html', posts=posts)

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)
