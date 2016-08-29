from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_and_registration')
app.secret_key = "blahblahblabh98a2g4qiu24t"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')

@app.route('/')
def index():
	# If logged on, log off
	if 'user_id' in session:
		session.pop('user_id')
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	# Login Validation
	error = False
	if request.form['action'] == 'login':
		# Email
		if len(request.form['login_email']) < 1:
			flash("you forgot to enter an email", 'login_email')
			error = True
		elif not EMAIL_REGEX.match(request.form['login_email']):
			flash("that's not a real email address", 'login_email')
			error = True
		else:
			query = 'SELECT email FROM users WHERE email = :email'
			data = { 'email': request.form['login_email'] }
			email = mysql.query_db(query, data)
			if request.form['login_email'] != email[0]['email']:
				flash("that email doesn't match any user", 'login_email')
				error = True
		# Password
		if len(request.form['login_password']) < 1:
			flash("you can't log in if you leave this blank", 'login_password')
			error = True
		elif len(request.form['login_password']) < 8:
			flash("passwords must be at least eight characters long", 'login_password')
			error = True

	# Registration Validation
	elif request.form['action'] == 'register':
		# First Name
		if len(request.form['reg_fname']) < 2:
			flash("sorry, your name must be more than one character long", 'reg_fname')
			error = True
		elif not LETTERS_ONLY.match(request.form['reg_fname']):
			flash("your name can only have letters in it", 'reg_fname')
			error = True
		# Last Name
		if len(request.form['reg_lname']) < 2:
			flash("sorry, your name must be more than one character long", 'reg_lname')
			error = True
		elif not LETTERS_ONLY.match(request.form['reg_lname']):
			flash("your name can only have letters in it", 'reg_lname')
			error = True
		# Email
		if len(request.form['reg_email']) < 1:
			flash("you forgot to enter an email", 'reg_email')
			error = True
		elif not EMAIL_REGEX.match(request.form['reg_email']):
			flash("that's not a real email address", 'reg_email')
			error = True
		else:
			query = 'SELECT email FROM users WHERE email = :email'
			data = { 'email': request.form['reg_email'] }
			if request.form['reg_email'] == mysql.query_db(query, data):
				flash("that email is already in use", 'reg_email')
				error = True
		# Password
		if len(request.form['reg_password']) < 1:
			flash("you can't register without a password", 'reg_password')
			error = True
		elif len(request.form['reg_password']) < 8:
			flash("passwords must be at least eight characters long", 'reg_password')
			error = True
		# Confirm Password
		if not request.form['reg_password_confirm'] == request.form['reg_password']:
			flash("those passwords don't match", 'reg_password_confirm')
			error = True
	else:
		return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	
	if error:
		return redirect('/')
	else:
		if request.form['action'] == 'login':
			query = "SELECT password FROM users WHERE email = :email"
			data = { 
				'email': request.form['login_email']
			}
			stored_pw = mysql.query_db(query, data)
			if not  bcrypt.check_password_hash(stored_pw[0]['password'], request.form['login_password']):
				flash("that wasn't the right password", 'login_password')
				return redirect('/')
			else:
				query = "SELECT id FROM users WHERE email = :email"
				data = {
					"email": request.form['login_email']
				}
				user_id = mysql.query_db(query, data)
				session['user_id'] = user_id[0]['id']
				return redirect("/dashboard")
		elif request.form['action'] == 'register':
			query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
			data = {
				'first_name': request.form['reg_fname'],
				'last_name': request.form['reg_lname'],
				'email': request.form['reg_email'],
				'password': bcrypt.generate_password_hash(request.form['reg_password'])
			}
			mysql.query_db(query, data)
			return redirect('/success')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/dashboard')
def dashboard():
		query = "SELECT first_name, last_name, created_at, email FROM users WHERE id = :user_id"
		data = {
			'user_id': session['user_id']
		}
		user = mysql.query_db(query, data)
		return render_template('dashboard.html', user=user[0])


app.run(debug=True)