from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector

app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'myownapi')


@app.route('/quotes')
def index():
    return render_template('index.html')

@app.route('/quotes/index_json')
def index_json():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return jsonify(quotes)

app.run(debug=True)