

# coding=utf-8

#

# 부동산 전월세 api 사용하기

#

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import sqlite3


if __name__ == "__main__":

    con = sqlite3.connect("./data/real_trade.db")

    cur = con.cursor()

    query = cur.execute("SELECT * From lent")

    cols = [column[0] for column in query.description]

    sil_trade = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

    con.close()

   #한글 가능 폰트 불러오기

    fm.get_fontconfig_fonts()

    font_location = '/Library/Fonts/NanumBarunGothicBold.ttf'

    font_name = fm.FontProperties(fname=font_location).get_name()

    matplotlib.rc('font', family=font_name)



    sil_trade.describe()

    sil_trade.dtypes


    sil_trade["mo_price"] = sil_trade["mo_price"].str.replace(" ","")

    sil_trade["mo_price"] = sil_trade["mo_price"].str.replace(",", "")

    sil_trade["mo_price"]=sil_trade["mo_price"].astype(int)


    sil_trade["bo_price"] = sil_trade["bo_price"].str.replace(" ","")

    sil_trade["bo_price"] = sil_trade["bo_price"].str.replace(",", "")

    sil_trade["bo_price"]=sil_trade["bo_price"].astype(int)


    sil_trade["is_j"]="월세"

    sil_trade.ix[sil_trade["mo_price"]==0,"is_j"]="전세"


    sil_trade["ym"]=sil_trade["year"].astype(int)*100+sil_trade["month"].astype(int)




    code=pd.read_excel("KIKcd_B.20180122.xlsx")

    code_seo=code[(code["시도명"]=="서울특별시") | (code["시도명"]=="경기도")]

    code_seo=code_seo[code_seo["읍면동명"].isnull()==True]

    code_seo = code_seo[code_seo["시군구명"].isnull() == False]

    code_seo["ji_code"] = code_seo["법정동코드"].astype(str).str[0:5]

    code_seo=code_seo[["ji_code","시도명","시군구명"]]


    sil_trade_1=pd.merge(sil_trade,code_seo,on="ji_code",how="left")

    temp = sil_trade_1.groupby(["시도명","ym", "is_j"]).size().reset_index(name='counts')


    temp["ym"]=temp["ym"]-201700

    temp.ix[temp["ym"]==101,"ym"]=13

    temp.ix[temp["ym"] == 102, "ym"] = 14

    temp.set_index("ym", inplace=True)
    temp.groupby(["시도명", "is_j"])["counts"].plot(legend=True, grid=True, xticks=temp.index)

