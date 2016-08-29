from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_posts')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index_json', methods=['GET','POST'])
def index_json():
	query = "SELECT * FROM posts ORDER BY created_at DESC"
	posts = mysql.query_db(query)
	return jsonify(posts)

@app.route('/index_json/create', methods=['GET','POST'])
def create_json():
	query = 'INSERT INTO posts(post) VALUES (:post)'
	data = { 'post': request.form['new_note'] }
	mysql.query_db(query, data)
	query = "SELECT * FROM posts ORDER BY created_at DESC"
	posts = mysql.query_db(query)
	return jsonify(posts)

app.run(debug=True)