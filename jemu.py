# coding=utf-8
#
# 기업 open_api 이용하기
#
# coding=utf-8
#
# 기업 open_api 이용하기
#

from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser
from html_table_parser import parser_functions as parser
url2="http://dart.fss.or.kr/report/viewer.do?rcpNo=20170811001153&dcmNo=5746981&eleId=15&offset=297450&length=378975&dtd=dart3.xsd"

report=urlopen(url2)
r=report.read()
xmlsoup=BeautifulSoup(r,'html.parser')
body=xmlsoup.find("body")
table=body.find_all("table")
p = parser.make2d(table[3])

sheet = pd.DataFrame(p[2:], columns=["구분","38기반기_3개월","38기반기_누적","37기반기_3개월","37기반기_누적"])
sheet["38기반기_3개월"]=sheet["38기반기_3개월"].str.replace(",","")
sheet["temp"]=sheet["38기반기_3개월"].str[0]

sheet.ix[sheet["temp"]=="(","38기반기_3개월"]=sheet["38기반기_3개월"].str.replace("(","-")
sheet["38기반기_3개월"]=sheet["38기반기_3개월"].str.split(")").str[0]
sheet.ix[sheet["38기반기_3개월"]=="","38기반기_3개월"]="0"
sheet["38기반기_3개월"]=sheet["38기반기_3개월"].astype(int)
sale = sheet[sheet["구분"]=="매출액"].iloc[0,1]
sale_cost = sheet[sheet["구분"]=="매출원가"].iloc[0,1]
sale_profit_ratio=(sale-sale_cost)/sale*100

# round는 반올림
sale_profit_ratio=round(sale_profit_ratio,1)
print("매출총이익률은 "+str(sale_profit_ratio)+"% 입니다")
