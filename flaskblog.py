from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '14c49b5eacffdba34f50bb598980f0ca' 
# Random characters/key for the app. we can use python interpreter to get one.

#secret key from  import secret // secrets.token_hex(16) gives random char with 16 bytes
# we will later convert this into an environment variable



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
@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
	app.run(debug = True)

