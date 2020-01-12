from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '810d083debd24bc368c77dbfb25e8022'

posts = [
	{
		'author': 'Go to URL',
		'title': 'navigate to',
		'content': 'selector',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'click link',
		'title': 'click',
		'content': 'xpath',
		'date_posted': 'submit'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

"""@app.route('/template')
def index():
	return render_template('template.html', posts=posts)"""

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
			flash(f'Account created for {form.username.data}!', 'success')
			return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!!!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unssuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)
