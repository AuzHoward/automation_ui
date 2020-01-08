from flask import Flask, render_template

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
def index():
	return render_template('template.html', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)
