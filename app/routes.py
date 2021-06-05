from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, PostForm

@app.route('/')
@app.route('/index')
def index():
	#Mock object creation
	user = {"username" : "Pat", "age" : 10, "grade" : "A"}
	#More mock object creation: posts that contain an author, body of text, and date
	posts = [{'author' : {'username' : 'Em'},
			  'body' : 'I had a great day today',
			  'date' : '6/4/2021'},
			  {'author' : {'username' : 'Pat'},
			   'body': 'This is one of the first posts on this blog',
			   'date' : '6/3/2021'}]


	return render_template('index.html', title='Home Page', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))

	return render_template('login.html', title='Log In', form=form)

@app.route('/post')
def post():
	form = PostForm()
	return render_template('post.html', title='Post', form=form)