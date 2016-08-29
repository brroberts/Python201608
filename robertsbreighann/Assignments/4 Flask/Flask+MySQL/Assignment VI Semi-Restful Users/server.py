from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'semi_restful_users')
app.secret_key = 'blahbblahblahbq98324'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')

''' Pages '''
@app.route('/users')  # Display all the users
def index():
	query = "SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') as created_at FROM users ORDER BY id"
	users = mysql.query_db(query)
	return render_template('index.html', users = users)

@app.route('/users/new')  # Create a new user
def new():
	return render_template('create_user.html')

@app.route('/users/<id>/edit')  # Edit an existing user
def edit(id):
	query = "SELECT id, first_name, last_name, email FROM users WHERE id = :id"
	data = {
		'id': id
	}
	user = mysql.query_db(query, data)
	return render_template('edit_user.html', user=user[0])

@app.route('/users/<id>')  # Show an existing user
def show(id):
	query = "SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') as created_at FROM users WHERE id = :id"
	data = {
		'id': id
	}
	user = mysql.query_db(query, data)
	return render_template('show_user.html', user = user[0])

''' Processes '''
@app.route('/users/create', methods=['POST'])  # Process creating a user
def create():
	#Validation
	error = False
	#First Name
	if len(request.form['fname']) < 1:
		flash('First Name cannot be blank', 'fname')
		error = True
	elif not LETTERS_ONLY.match(request.form['fname']):
		flash('Names can only include letters', 'fname')
		error = True
	#Last Name
	if len(request.form['lname']) < 1:
		flash('First Name cannot be blank', 'lname')
		error = True
	elif not LETTERS_ONLY.match(request.form['lname']):
		flash('Names can only include letters', 'lname')
		error = True
	#Email
	if len(request.form['email']) < 1:
		flash('Email cannot be blank', 'email')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email must be valid', 'email')
		error = True
	else:
		query = 'SELECT email FROM users WHERE email = :email'
		data = { 'email': request.form['email'] }
		check = mysql.query_db(query, data)
		if not check:
			pass
		elif request.form['email'].lower() == check[0]['email'].lower():
			flash('That email is already in use', 'email')
			error = True
	if error:
		return redirect('/users/new')

	#Insert User if Pass Validation
	query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email']
	}
	mysql.query_db(query, data)
	query = "SELECT id FROM users WHERE email = :email"
	id = mysql.query_db(query, data)
	id = str(id[0]['id'])
	show_created = '/users/'+id
	return redirect(show_created)  # Redirect to show user after creation

@app.route('/users/<id>/destroy', methods=['GET'])  # Process deleting a user
def destroy(id):
	query = "DELETE FROM users WHERE id = :id"
	data = {
		'id': id
	}
	mysql.query_db(query, data)
	return redirect('/users')  # Redirect to show all users after deletion

@app.route('/users/<id>', methods=['POST'])  # Process updating a user
def update(id):
	#Validation
	error = False
	#First Name
	if len(request.form['fname']) < 1:
		flash('First Name cannot be blank', 'fname')
		error = True
	elif not LETTERS_ONLY.match(request.form['fname']):
		flash('Names can only include letters', 'fname')
		error = True
	#Last Name
	if len(request.form['lname']) < 1:
		flash('First Name cannot be blank', 'lname')
		error = True
	elif not LETTERS_ONLY.match(request.form['lname']):
		flash('Names can only include letters', 'lname')
		error = True
	#Email
	if len(request.form['email']) < 1:
		flash('Email cannot be blank', 'email')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email must be valid', 'email')
		error = True
	#Check for errors
	if error:
		route = '/users/'+id+'/edit'
		return redirect(route)

	query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
	data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'id': id
	}
	mysql.query_db(query, data)
	show_updated = '/users/'+id
	return redirect(show_updated)  # Redirect to show user after updating

app.run(debug=True)