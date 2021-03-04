
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '14c49b5eacffdba34f50bb598980f0ca' 
# Random characters/key for the app. we can use python interpreter to get one.

#secret key from  import secret // secrets.token_hex(16) gives random char with 16 bytes
# we will later convert this into an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// represent a relative path. also get automatically 
# created if not present
# setting up an sql-lite database which would be a file in our database
db = SQLAlchemy(app)


class User(db.Model):
	"""setting up the database as a class"""
	id = db.Column(db.Integer, primary_key= True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(120), unique = True, nullable = False) # max 120 char for email
	image_file = db.Column(db.String(20), nullable = False, default= 'default.jpg') # images will be hashed into 20 char uniques
	password = db.Column(db.String(60), nullable = False)
	# one to many relationship is used bcs one user can have many posts but one post can only have one user
	posts = db.relationship('Post', backref = 'author', lazy = True)



	def __repr__(self):
		return f"User('{self.username}, {self.email}, {self.image_file})"

class Post(db.Model):
	""" DB for Posts of each user"""
	id = db.Column(db.Integer, primary_key= True)
	title = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	# here, 'user.id' is lowercase because it is referencing the table db Column name on contrary to 
	# the 'Post' in db.relationship in the User class which actually references the 'Post' class



	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"


#Dummy data for blog post

posts = [
	{
	'author': 'Nithin A R', 
	'title': 'Blog post 1', 
	'content': 'First Blog post', 
	'date_posted': 'Feb 19, 2020'
	}, 
	{
	'author': 'Deepak Das V', 
	'title': 'Blog post 1', 
	'content': 'First Blog post', 
	'date_posted': 'Feb 15, 2020'
	}, 

]





@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts = posts)

@app.route("/about")
def about():
	return render_template("about.html", title= "About")


# Registration route
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	# while submiting the form the values submited may not be valid values. inorder to verify that we 
	# can create a validate on submit method
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}! ', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)
# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in !', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful !. Please check username and password', 'danger')

	return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
	app.run(debug = True)

