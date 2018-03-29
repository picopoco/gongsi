
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import sqlite3
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser
from html_table_parser import parser_functions as parser

def collect_lent(ym,lawd_cd):

    API_KEY = ('제공받은 API키')


    url="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent"


    # &numOfRows=1000"+

    url=url+"?&LAWD_CD="+lawd_cd+"&DEAL_YMD="+ym+"&serviceKey="+API_KEY


    # webbrowser.open(url)


    resultXML = urlopen(url)

    result = resultXML.read()

    xmlsoup = BeautifulSoup(result, 'lxml-xml')


    te=xmlsoup.findAll("item")


    sil=pd.DataFrame()


    for t in te:

        build_y=t.find("건축년도").text

        year=t.find("년").text

        month=t.find("월").text

        day=t.find("일").text

        dong=t.find("법정동").text

        bo_price=t.find("보증금액").text

        mo_price=t.find("월세금액").text

        apt_nm=t.find("아파트").text

        size=t.find("전용면적").text


        try:

            jibun=t.find("지번").text

        except:

            jibun=""


        ji_code=t.find("지역코드").text

        floor=t.find("층").text


        temp = pd.DataFrame(([[build_y,year,month,day,dong,bo_price,mo_price,apt_nm,size,jibun,ji_code,floor]]), columns=["build_y","year","month","day","dong","bo_price","mo_price","apt_nm","size","jibun","ji_code","floor"])

        sil=pd.concat([sil,temp])


    sil=sil.reset_index(drop=True)


    return sil




if __name__ == "__main__":


    # 지역코드 가져오기


    code=pd.read_excel("KIKcd_B.20180122.xlsx")


    code_seo=code[(code["시도명"]=="서울특별시") | (code["시도명"]=="경기도")]

    code_seo=code_seo[code_seo["읍면동명"].isnull()==True]

    code_seo = code_seo[code_seo["시군구명"].isnull() == False]

    code_seo["ji_code"] = code_seo["법정동코드"].astype(str).str[0:5]


    sil_trade=pd.DataFrame()

    ym=list(["201701","201702","201703","201704","201705","201706","201707","201708","201709","201710","201711","201712","201801"])

    for m in ym:

        for co in code_seo["ji_code"]:

            temp=collect_lent(m,co)

            sil_trade=pd.concat([sil_trade,temp])

            print(co+", "+str(len(temp))+" is compleded")

        print("*"+str(m)+" is completed")


    con = sqlite3.connect("./data/real_trade.db")

    sil_trade.to_sql('lent', con, if_exists='append', index=False)

    con.close()


