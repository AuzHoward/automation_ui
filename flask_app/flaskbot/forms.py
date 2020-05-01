from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskbot.models import User, TestSteps

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username is taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#---------------------------------------------------------------
class TastCaseTitle(FlaskForm):
    test_name = StringField('Test Name', validators=[DataRequired(), Length(min=2, max=20)])

class TestCaseForm(FlaskForm):
    step_name = StringField('Step Name')#, validators=[DataRequired(), Length(min=2, max=20)])
    action = StringField('Action')#, validators=[DataRequired(), Length(min=2, max=20)])
    element_type = StringField('Element Type')#, validators=[DataRequired()])
    element_id = StringField('Element ID')#, validators=[DataRequired()])
    input_string = StringField('Input')#, validators=[DataRequired()])
    submit = SubmitField('Sign Up')
