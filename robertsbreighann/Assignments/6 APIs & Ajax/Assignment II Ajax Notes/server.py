from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_notes')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index_json', methods=['GET', 'POST'])
def index_json():
	query = 'SELECT * FROM notes ORDER BY created_at DESC;'
	notes = mysql.query_db(query)
	return jsonify(notes)

@app.route('/index_json/create', methods=['POST'])
def create():
	query = 'INSERT INTO notes (title) VALUES (:title);'
	data = { 'title': request.form['new_title'] }
	mysql.query_db(query, data)
	return index_json()

@app.route('/index_json/update', methods=['POST'])
def update():
	query = 'UPDATE notes SET description=:description, updated_at=NOW() WHERE id = :id'
	data = {
		'description': request.form['note_desc'],
		'id': request.form['note_id']
	}
	mysql.query_db(query, data)
	return index_json()

@app.route('/<id>/delete')
def destroy(id):
	query = 'DELETE FROM notes WHERE id = :id;'
	data = { 'id': id }
	mysql.query_db(query, data)
	return index_json()


app.run(debug=True)