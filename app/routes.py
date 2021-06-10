from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, PostForm

@app.route('/')
@app.route('/index')
def index():
	user = {"username" : "Pat", "age" : 10, "grade" : "A"}
	header = "Home Page"
	return render_template('index.html', header=header, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	header="Log In"
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))

	return render_template('login.html', header=header, form=form)

@app.route('/post')
def post():
	header="Post"
	form = PostForm()
	return render_template('post.html', header=header, form=form)

@app.route('/about')
def about():
	header="About Me"
	return render_template('about.html', header=header)

@app.route('/sideprojects')
def sideprojects():
	header="Side Projects"
	#Mock object creation
	user = {"username" : "Pat", "age" : 10, "grade" : "A"}
	#More mock object creation: posts that contain an author, body of text, and date
	posts = [{'project_name' : 'Spotify API Project',
			  'project_body' : 'This project used Spotify\'s API to dump Spotify\'s \"Made For You\" playlist',
			  'project_date' : '6/4/2021',
			  'project_link': 'https://github.com/patoro7247/SpotifyAPIPythonProject'},
			  {'project_name' : 'Python Dictionary API Game',
			   'project_body': 'This game lets the user guess antonyms to random words',
			   'project_date' : '6/3/2021',
			   'project_link': 'https://github.com/patoro7247/DictionaryAPIgame'},
			   {'project_name' : 'Bike Inventory Manager in C++',
			   'project_body': 'This bike inventory manager allows a user to input a txt file',
			   'project_date' : '6/10/2021',
			   'project_link': 'https://github.com/patoro7247/Assignment-7.0'}]

	return render_template('sideprojects.html', user=user, posts=posts, header=header)