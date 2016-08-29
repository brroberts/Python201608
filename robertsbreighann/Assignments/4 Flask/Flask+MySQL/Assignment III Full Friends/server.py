from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
  #Display all of the friends on the index.html page
  query = "SELECT * FROM friend ORDER BY created_at DESC;"
  friends = mysql.query_db(query)
  return render_template("index.html", friends=friends)


@app.route('/friends', methods=['POST'])
def create():
  # Handle the add friend form submit and create the friend in the DB
  query = "INSERT INTO friend (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());"
  data = {
    'first_name': request.form['first_name'],
    'last_name':  request.form['last_name'],
    'email':      request.form['email']
  }
  friend_id = mysql.query_db(query, data)
  print friend_id
  return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
  # Delete the friend from the DB
  query = "DELETE FROM friend WHERE id = :id"
  data = { 'id': id }
  mysql.query_db(query, data)
  return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
  # Display the edit friend page for the particular friend
  query = "SELECT * FROM friend WHERE id = :id"
  data = { 'id': id }
  friends = mysql.query_db(query, data)
  if not len(friends) == 1:
    print 'nice try suckaaa'
    return redirect('/')

  return render_template('edit.html', friend=friends[0])


@app.route('/friends/<id>', methods=['POST'])
def update(id):
  # Handle the edit friend form submit and update the friend in the DB
  query = "UPDATE friend SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id;"
  data = {
    'first_name': request.form['first_name'],
    'last_name':  request.form['last_name'],
    'email':      request.form['email'],
    'id':         id
  }
  mysql.query_db(query, data)
  return redirect('/')

app.run(debug=True)
