from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
	"""form fields will be defined as classes as well. 
	they will be compiled to html later automatically"""
	username = StringField('Username', 
		validators = [DataRequired(), Length(min= 2, max= 20)])
	'''Username must be small. not longer than 20 char with other 
	conditions as well. and such conditions are given by validators'''
	
	email = StringField("Email", validators= [DataRequired(), Email()])

	password = PasswordField("Password", validators= [DataRequired()])
	confirm_password = PasswordField("Confirm password", validators= [DataRequired(), EqualTo('password')])

	submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):
	"""fCan use username to login but better to use email bcs they are less likely to forget 
	"""
	
	
	email = StringField("Email", validators= [DataRequired(), Email()])

	password = PasswordField("Password", validators= [DataRequired()])
	remember = BooleanField('Remember me') # will allow users to stay logged in for a while after their browser closes. 
	# using a secure cookie


	submit = SubmitField('Log in')







