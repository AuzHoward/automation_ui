from flask import render_template, url_for, flash, redirect, request
from flaskbot import app, db, bcrypt
from flaskbot.forms import RegistrationForm, LoginForm, TestCaseForm
from flaskbot.autoscripttemp import Automate, ChromeConfig
from flaskbot.models import User, Post, TestSteps
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

#@app.route("/automation")
#def registerauto():
#    return render_template('registerauto.html', title='Automation')

@app.route("/automation", methods=['GET', 'POST'])
def registerauto():
    form = TestCaseForm()
    if form.validate_on_submit():
        user_input = 'testing123'
        ChromeConfig.chromeDriver()
        cd = ChromeConfig.chromeDriver().chrome
        #test_id = uuid.uuid1()
        #test_case = TestCase(test_id=uuid.uuid1(), test_name=form.test_name.data)
        #print("Running registerauto")
        #----------------------------------------------here is database
        #test_steps = TestSteps(step_name=form.step_name.data, action=form.action.data, element_type=form.element_type.data, element_id=form.element_id.data, input_string=form.input_string.data)
        #db.session.add(test_steps)#find out where to implement test variable like user is
        #db.session.commit()
        Automate.run(form.action.data, form.element_type.data, form.element_id.data, form.input_string.data, cd)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registerauto.html', title='Automation', form=form)
