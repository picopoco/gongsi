#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='ggoggoma',
                       db='admin_console', charset='utf8')

# Connection 으로부터 Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

# SQL문 실행
sql = "select * from LMS where menuId=%s "
curs.execute(sql, ('1k1e2w'))

# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)
    # 출력 : {'category': 1, 'id': 1, 'region': '서울', 'name': '김정수'}
   # print(row['id'], row['name'], row['region'])
    # 1 김정수 서울

# Connection 닫기
conn.close()