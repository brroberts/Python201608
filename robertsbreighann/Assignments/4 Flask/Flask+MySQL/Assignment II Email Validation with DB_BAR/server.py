from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app,'email')

email_regex =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
	query = 'select * from email'
	data = mysql.query_db(query)

	return render_template('index.html', email_data = data)

@app.route("/email", methods=['POST'])
def email_add():
	
	email = request.form['email']
	
	if len(email) == 0 or not email_regex.match(email):
		flash("invalid email",'error') 
	else:		
		flash("The email you entered {} is valid.Thank you.".format(email),'success') 
		query = 'insert into email (email,created_at,updated_at) values (:email,now(),now())'	
		data = {'email': email}
		mysql.query_db(query,data)

	return redirect('/')	

@app.route("/del", methods=['POST'])
def delete_email():
	id = request.form['delEmail']
	query = 'delete from email where id = :id'
	data = {"id": id}
	mysql.query_db(query,data)
	return redirect("/")
app.run(debug=True)