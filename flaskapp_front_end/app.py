# app.py - a minimal flask api using flask_restful
from flask import Flask ,jsonify
from flask_restful import Resource, Api
# import sqlalchemy as db
# import mysql.connector
# from redis import Redis
# import pymysql
import requests
# from typing import List, Dict
import json
# from rauth.service import OAuth1Service, OAuth1Session
from flask import render_template, request


# from goodreads import client

key = '97iWODxi1Wo0ZYQFoBHcw'
secret= '6GfrCQNNiWgHzuyecVafw5q5us3MaznQSESFV9h4vMg'


app = Flask(__name__)
api = Api(app)


@app.route('/connection_string/')
def connection_string():
    return "str(connection.is_connected())"

@app.route('/test_table/')
def test_table():
    return "test_table"

@app.route('/cursor/')
def mycursor():
    return mycursor

@app.route('/')
def index():
    return "HI"
    # redis.incr('hits')
    # redis.set("name", "new_data")
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


# @app.route('/search/<query>')
@app.route('/query/', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        # json_data = requests.get('http://host.docker.internal:5001/search/harry').json()        
        text = request.form['query']
        json_data = requests.get('http://host.docker.internal:5001/search/{}'.format(text)).json()
        condition = json_data['data']
        work = json_data['work'][:5]
        return render_template('query.html',condition=condition,work=work)
    if request.method == 'GET':
        condition=""
        return render_template('query.html',condition=condition)
    # return render_template('query.html',condition=condition)


@app.route('/insert/')
def insert():
    return 'The name is '
    # metadata = db.MetaData()
    # test_table = db.Table('test_table', metadata, autoload=True, autoload_with=engine)
    # return str(test_table.columns.keys())

@app.route('/clear/', methods=['GET'])
def clear_data():
    # redis.flushall()
    return "ok!"



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)



