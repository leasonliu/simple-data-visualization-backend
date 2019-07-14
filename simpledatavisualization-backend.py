from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pymysql.cursors
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'Simple Data Visualization'

@app.route('/data', methods=['GET', 'POST'])
@cross_origin()
def data():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Simple-data-visualization',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `activity`(`position`, `activity`, `duration`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (request.form['position'], request.form['activity'], request.form['duration']))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            return {"res": "success"}
        finally:
            connection.close()
    else:
        try:
            with connection.cursor() as cursor:
                # Read records
                sql = "select * from activity"
                cursor.execute(sql)
                result = cursor.fetchall()
            return jsonify(result)
        finally:
            connection.close()

@app.route('/data', methods=['PUT'])
@cross_origin()
def dataPut():
    return update(request.form)

@app.route('/data', methods=['DELETE'])
@cross_origin()
def dataDelete():
    return delete(request.form)

@app.route('/summary', methods=['GET'])
@cross_origin()
def getSummary():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Simple-data-visualization',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    result = []
    try:
        with connection.cursor() as cursor:
            # Read records
            sql = "select a.activity AS Activity, SUM(a.duration) AS Duration from activity a group by a.activity"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        cursor.close()
    return jsonify(result)

def update(data):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Simple-data-visualization',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "UPDATE activity SET `activity` = %s, `duration` = %s WHERE `position` = %s"
            cursor.execute(sql, (request.form['activity'], request.form['duration'], request.form['position']))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            return {"res": "success"}
    finally:
        connection.close()

def delete(data):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Simple-data-visualization',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "DELETE FROM activity WHERE `position` = %s"
            cursor.execute(sql, (request.args.get('position')))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            return {"res": "success"}
    finally:
        connection.close()
