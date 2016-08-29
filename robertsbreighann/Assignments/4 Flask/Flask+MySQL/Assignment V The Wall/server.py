from flask import Flask, render_template,redirect,session, flash,request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secretKey"
mysql = MySQLConnector(app,'wall')

@app.route("/")
def index():
	session['logged'] =False
	session['data'] ={}
	return render_template('index.html')

@app.route("/register")
def reg():
	return render_template('registration.html')

@app.route("/login", methods=['POST'])
def login():
	email = request.form['email']
	pwd = request.form['password']	
	query = "select * from users where email = :email limit 1"	
	
	if mysql.query_db(query,{"email": email}):
		data = mysql.query_db(query,{"email": email})
	else:
		return redirect("/register")

	if bcrypt.check_password_hash(data[0]['password'],pwd):
		session['logged'] = True
		session['data'] = data[0]
		return redirect('/success')
	else: 
		flash("Invalid Password")
		return redirect("/")

@app.route("/registration", methods=['POST'])
def registration():	
	email = request.form['email']
	query = "select * from users where email = :email limit 1"	
	
	if mysql.query_db(query,{"email": email}):
		flash("Email already exists")
		return redirect('/register')

	def validate():	
		count = 0	
		if len(request.form['email'])<1:
			flash("Email cannot be empty")
			count+=1
		if len(request.form['first_name'])<2:
			flash("First name should be atleast two charachters long")
			count+=1		
		if len(request.form['last_name']) < 2:
			flash("Last name should be atleast two charachters long")
			count+=1			
		if len(request.form['password'])<8:
			flash("Password must be at least 8 characters")
			count+=1				
		if request.form['confirm'] != request.form['password']:
			flash("Confirm password must match password")
			count+=1
		if count ==0:
			return False
		else: 
			return True					
	
	if validate():
		return redirect("/register")
	else:
		query = "insert into users (email, first_name, last_name, password, created_at, updated_at) values (:email, :first_name, :last_name, :password, now(), now())"
		data = {
		'email':request.form['email'],
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'password': bcrypt.generate_password_hash(request.form['password']),				
		}	
		mysql.query_db(query,data)	
		session['logged'] = True
		query = "select * from users where email = :email limit 1"	
		data = data = {'email':request.form['email']}
		session['data'] =mysql.query_db(query,data)[0]
		return redirect('/success')	

@app.route("/logout")
def logout():
	return redirect("/")

@app.route('/success')
def sucess():
	if session['logged']:
		fname = session['data']['first_name']
		
		query = "select messages.id, messages.message, messages.created_at, users.first_name, users.last_name from wall.messages join wall.users on wall.users.id = wall.messages.user_id order by wall.messages.created_at desc;"
		
		messages = mysql.query_db(query)
		for message in messages:
			query = "select comments.id, comments.comment, comments.created_at, users.first_name, users.last_name from comments join users on users.id = comments.user_id join messages on comments.message_id = messages.id where messages.id = :message_id order by comments.created_at;"
			data = {"message_id": message['id']}
			message['comments'] = mysql.query_db(query,data)
		print messages[0]
		return render_template("success.html",fname=fname,messages=messages)
	else:
		flash("Not so easy brvah. You gotta login first.")
		return redirect("/")		

@app.route('/message', methods=['POST'])
def message():
	
	query = "insert into wall.messages (message,created_at,updated_at,user_id) values (:message,NOW(),NOW(),:id)"
	data = {
		'message':request.form['message'],
		'id': session['data']['id']
	}
	key = mysql.query_db(query,data);
	return redirect('/success')

@app.route('/comment', methods=['POST'])
def comment():	
	query = "insert into wall.comments (comment,created_at,updated_at,user_id,message_id) values (:comment,NOW(),NOW(),:user_id,:message_id)"
	data = {
		'comment':request.form['comment'],
		'user_id': session['data']['id'],
		'message_id': request.form['message_id'] 
	}
	key = mysql.query_db(query,data);
	return redirect('/success')	
app.run(debug=True)
