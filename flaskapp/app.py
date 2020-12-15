# app.py - a minimal flask api using flask_restful
from flask import Flask ,jsonify
from flask_restful import Resource, Api
# import sqlalchemy as db
import mysql.connector
from redis import Redis
# import pymysql
import requests
# from typing import List, Dict
import json
# from rauth.service import OAuth1Service, OAuth1Session
from flask import render_template


# from goodreads import client

key = '97iWODxi1Wo0ZYQFoBHcw'
secret= '6GfrCQNNiWgHzuyecVafw5q5us3MaznQSESFV9h4vMg'

# gc = client.GoodreadsClient(key, secret)

import xmltodict,json
import urllib.request
keyword = 'harry potter'.replace(" ","%20")

api_url =  urllib.request.urlopen("https://www.goodreads.com/search.xml?key="+key+"&q="+keyword)
data = api_url.read()
a = xmltodict.parse(data)
a_data= json.dumps(a)


config = {
    # 'host': 'host.docker.internal',
    'host': 'db',
    # 'host': '172.20.0.2',
    # 'host': 'mysql',
    'port': '3306',
    'user': 'newuser',
    'password': 'newpassword',
    'database': 'test_db'
}
db=mysql.connector.connect(**config)
mycursor = db.cursor()
mycursor.execute('use test_db;')







redis = Redis(host='redis', port=6379)

app = Flask(__name__)
api = Api(app)


@app.route('/connection_string/')
def connection_string():
    return str(connection.is_connected())

@app.route('/test_table/')
def test_table():
    return test_table

@app.route('/cursor/')
def mycursor():
    return mycursor

@app.route('/')
def index():
    redis.incr('hits')
    # redis.incr('hits')
    redis.set("name", "new_data")
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    # return 'db_name'


@app.route('/search/<query>')
def search(query=None,results=None):
    # sql_query="select data_keyword from query_results where keyword='{}'".format(query)
    # try:
    # mycursor = db.cursor()
    # mycursor.execute(sql_query)
    # result=mycursor.fetchall()
    # database_valid = True

    # db_results=None

    # for i in result:    
    #     db_results=i[0]
    # except:
    #     database_valid = False

    if query:
        # try:
        if redis.get(query):
            redis.get(query).decode()
            results = json.loads(redis.get(query).decode())
            display = {"data":"loads data from redis"}
            display.update(results)

        # elif database_valid:
        # elif db_results!=None:
        else:
            # try:  
                
                # mycursor.execute("select data_keyword from query_results")#Execute SQL Query to select all record   
                # result=mycursor.fetchall() #fetches all the rows in a result set
                # 
            sql_query="select data_keyword from query_results where keyword='{}'".format(query)
            # try:
            mycursor = db.cursor()
            mycursor.execute(sql_query)
            result=mycursor.fetchall()
            database_valid = True

            db_results=None

            for i in result:    
                db_results=i[0] 

            if db_results!=None:  
                display = {"data":"loads data from MYSQL"}
                results = json.loads(db_results)
                display.update(results)
                return jsonify(display)
            
        # else:
            keyword =  query.replace(" ","%20")
            api_url =  urllib.request.urlopen("https://www.goodreads.com/search.xml?key="+key+"&q="+keyword)
            data = api_url.read()
            xml_data = xmltodict.parse(data)
            raw_xml= json.dumps(xml_data)
            json_data = json.loads(raw_xml)
            results = json_data['GoodreadsResponse']["search"]['results']
            redis.set(query,json.dumps(results))
            # insert in database
            mycursor = db.cursor()
            sql_result = str(json.dumps(results).replace("'","''"))
            str_query = '''INSERT INTO query_results (keyword, data_keyword) VALUES ('{}', '{}' )'''.format(query,sql_result)
            try:
                mycursor.execute(str_query)
            except Exception as e :
                return str(e)
            db.commit()
            display = {"data":"loads data from API"}
            display.update(results)
            

        # return jsonify(results)
        return jsonify(display)
        # redis.set(keyword,json.dumps(results))
    else:
        query=""
        results=""

    return render_template('query.html',query=query,results=results)


@app.route('/insert/')
def insert():
    return 'The name is  %s' % redis.get('name')
    # metadata = db.MetaData()
    # test_table = db.Table('test_table', metadata, autoload=True, autoload_with=engine)
    # return str(test_table.columns.keys())

@app.route('/clear/', methods=['GET'])
def clear_data():
    redis.flushall()
    return "ok!"



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)



