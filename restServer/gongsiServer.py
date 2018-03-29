#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from flask import Flask
from flask_restful import Resource, Api
from flaskext.mysql import MySQL
from flask_restful import reqparse
from flask import request
import data


app = Flask(__name__)
api = Api(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ggoggoma'
app.config['MYSQL_DATABASE_DB'] = 'admin_console'
app.config['MYSQL_DATABASE_HOST'] = '10.122.64.107'
mysql.init_app(app)


class LmsRepeatPlay(Resource):
    def post(self):
        response = {}
        result = {}
        try:
            conn = mysql.connect()
            cursor = conn.cursor()


            print " intent:" , request.json['body']['intent']
            reqstr = request.json
            MenuCode = reqstr['body']['slot']['lvl1']['value']
            moveType = reqstr['body']['slot']['moveType']
            intent = reqstr['body']['intent']

            if intent == 'lmsRepeatPlay':
                if moveType =='next':
                   sql = "SELECT * FROM EngSamsungLms WHERE repeatSeq =(SELECT  MIN(repeatSeq) AS repeatSeq FROM EngSamsungLms WHERE repeatSeq > (SELECT repeatSeq FROM EngSamsungLms WHERE menuId =%s))"
                else:
                    sql = "select * from EngSamsungLms where menuId=%s "

            elif intent == 'lmsRepeatPosition':
                result;

            cursor.execute(sql, (MenuCode))
            response = [dict((cursor.description[i][0], value)
                             for i, value in enumerate(row)) for row in cursor.fetchall()]
            result = data.getlmsRepeatData(response)
            print('lms response:', response)
            print('lms result:', result)

        except:
            print('lms server error %s ', sys.exc_info()[0])
        return result

api.add_resource(LmsRepeatPlay, '/coif/lms')

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0',port=5000)
