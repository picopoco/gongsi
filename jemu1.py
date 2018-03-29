

# coding=utf-8

#

# 기업 open_api 이용하기

#


from urllib.request import urlopen

import RestClient as output_last
import pandas as pd
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
from RestClient import RestClient
import csv
import json

API_KEY="2672b31cfb74118a9f7c11cfcce685bbeef77f19"
company_code="014680"

def make_report(company_code):

    url = "http://dart.fss.or.kr/api/search.xml?auth="+API_KEY+"&crp_cd="+company_code+"&start_dt=19990101&bsn_tp=A001&bsn_tp=A002&bsn_tp=A003"
    # resultXML=urlopen(url.encode("UTF-8").decode("ASCII"))
    resultXML=urlopen(url)
    result=resultXML.read()
    xmlsoup=BeautifulSoup(result,'html.parser')
    data = pd.DataFrame()
    te=xmlsoup.findAll("list")
    for t in te:

        temp=pd.DataFrame(([[t.crp_cls.string,t.crp_nm.string,t.crp_cd.string,t.rpt_nm.string,
                        t.rcp_no.string,t.flr_nm.string,t.rcp_dt.string, t.rmk.string]]),
                          columns=["crp_cls","crp_nm","crp_cd","rpt_nm","rcp_no","flr_nm","rcp_dt","rmk"])
        data=pd.concat([data,temp])
    data=data.reset_index(drop=True)
    url2="http://dart.fss.or.kr/dsaf001/main.do?rcpNo="+data['rcp_no'][0]
    # webbrowser.open(url2)
    return url2, data['rcp_no'][0]

def find_table(url2,rcpno):

    temp=urlopen(url2)
    r=temp.read()
    xmlsoup=BeautifulSoup(r,'html.parser')
    temp=xmlsoup.find_all("script",attrs={"type":"text/javascript"})
    txt=temp[7]
    a=txt.text
    b=str.find(a,"4. 재무제표")
    c=a[b:b+200]
    d=c.split(",")[4]
    e=d.replace("\"","")
    e=e.replace("\'","")
    dcmo=int(e)
    # 매출 정보 등을 가져오기
    url3="http://dart.fss.or.kr/report/viewer.do?rcpNo="+rcpno+"&dcmNo="+str(dcmo)+"&eleId=15&offset=297450&length=378975&dtd=dart3.xsd"
    # http://dart.fss.or.kr/report/viewer.do?rcpNo=20170811001153&dcmNo=5746981&eleId=15

    report=urlopen(url3)
    r=report.read()
    xmlsoup=BeautifulSoup(r,'html.parser')
    body=xmlsoup.find("body")
    table=body.find_all("table")
    p = parser.make2d(table[3])
    name_list=list()
    value_list=list()
    name_list.append("구분")

    for i in range(1,len(p[0])):
        name=p[0][i]+"_"+p[1][i]
        name=name.replace(" ","")
        name_list.append(name)
        value_list.append(name)
    sheet = pd.DataFrame(p[2:], columns=name_list)
    sheet.ix[sheet["구분"]=="수익(매출액)",["구분"]]="매출액"
    return sheet, name_list, value_list

def make_profit(sheet,name_list,value_list):

    # 매출총이익률 = 매출총이익 / 매출액 * 100

    # 매출총이익 = 매출액 - 매출원가


    #숫자로 바꾸기

    for time in value_list:

        sheet[time]=sheet[time].str.replace(",","")

        sheet["temp"]=sheet[time].str[0]
        sheet.ix[sheet["temp"]=="(",time]=sheet[time].str.replace("(","-")
        sheet[time]=sheet[time].str.split(")").str[0]
        sheet.ix[sheet[time]=="",time]="0"

        time=time.replace("요약분기포괄손익계산서_","")
        time=time.replace("(당)","")
        print('time', time)
        print ('sheet[time]',sheet[time])

        sheet[time]=sheet[time].astype(int)

    temp_list=list()
    temp_list.append("매출총이익률")

    for time in range(len(value_list)):

        sale = sheet[sheet["구분"]=="매출액"].iloc[0,time+1]

        sale_cost = sheet[sheet["구분"]=="매출원가"].iloc[0,time+1]

        sale_profit_ratio=(sale-sale_cost)/sale*100

        sale_profit_ratio = round(sale_profit_ratio, 1)

        temp_list.append(sale_profit_ratio)


    output=pd.DataFrame([temp_list],columns=name_list)

    return output



if __name__ == "__main__":

    company_list = list(["000400", "004990", "005930", "014680", "214370", "271560", "217270", "280360"])
    company_name = list(["롯데손해보험", "롯데지주", "삼성전자", "한솔케미칼", "케어젠", "오리온", "넵튠", "롯데제과"])
    output_last = pd.DataFrame(columns=["구분", "최근_분기", "최근_분기_누적", "이전_분기", "이전_분기_누적"])
    send_data =""
    for i in range(len(company_list)):
        try:
            url2, rcpno = make_report(company_list[i])
            sheet, name_list, value_list = find_table(url2, rcpno)
            output = make_profit(sheet, name_list, value_list)
            if len(output.columns) == 3:
                output.columns = ["구분", "최근_분기", "최근_분기_누적"]
            elif len(output.columns) == 5:
                output.columns = ["구분", "최근_분기", "최근_분기_누적", "이전_분기", "이전_분기_누적"]
            output["company_code"] = company_list[i]
            output["company_name"] = company_name[i]
            output["url"] = url2
            output_last = pd.concat([output_last, output])
            send_data =output
            #print("output_last", output_last)
        except Exception as e:
            print(company_name[i] + " is error")
            print(e)

    output_last.to_csv("output_last.csv")

    csvfile = open('output_last.csv', 'r')
    reader = csv.DictReader(csvfile)
    result = []
    for row in reader:
        result.append(row)
    result = json.dumps(result)
    result = json.loads(result)
    #keys = ('Entity', 'Year', 'SO2 emissions- Clio Infra')
    keys = ('company_code','company_name','url','구분','이전_분기','이전_분기_누적','최근_분기','최근_분기_누적')
    print(result)
    listData =[]
    with open('output_last.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            RestClient.SendJandiData(listData)
            print("row", row)
            listData.append(str(row)+'\n')
        print("reader",listData)

