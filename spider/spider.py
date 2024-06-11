import requests
from bs4 import BeautifulSoup
import os
import csv

#写入数据
def writeRow(row,path):
    with open(path,'a',encoding='utf-8',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(row)

#创建保存数据的文件
def init(path):
    if not os.path.exists(path):
        with open(path,'w',encoding='utf-8',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(([
                '年度',
                '年末总人口(万人)',
                '男性人口(万人)',
                '女性人口(万人)',
                '城镇人口(万人)',
                '乡村人口(万人)'
            ]))
#爬虫函数
def Sprider(url,path):
     #设置请求头
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    response = requests.get(url,headers=headers,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    years=[]
    sums=[]
    man=[]
    woman=[]
    city=[]
    countrised=[]
    all_th = soup.find_all('th',class_="tr-title")  #找到所有th的标签
    for th in all_th:
        strong=th.find('strong')
        years.append(strong.get_text())
    tbody=soup.find_all('tbody')[0]
    all_tr1=tbody.find_all('tr')[0]
    all_td1=all_tr1.find_all('td')
    for td in all_td1:
        sums.append(td.get_text())
    all_tr2=tbody.find_all('tr')[1]
    all_td2=all_tr2.find_all('td')
    for td in all_td2:
        man.append(td.get_text())
    all_tr3=tbody.find_all('tr')[2]
    all_td3=all_tr3.find_all('td')
    for td in all_td3:
        woman.append(td.get_text())
    all_tr4=tbody.find_all('tr')[3]
    all_td4=all_tr4.find_all('td')
    for td in all_td4:
        city.append(td.get_text())
    all_tr5=tbody.find_all('tr')[4]
    all_td5=all_tr5.find_all('td')
    for td in all_td5:
        countrised.append(td.get_text())
    i=0
    while i<len(sums):
        row=[]
        row.append(years[i])
        row.append(sums[i])
        row.append(man[i])
        row.append(woman[i])
        row.append(city[i])
        row.append(countrised[i])
        writeRow(row,path) #写入文件中
        i+=1

# init('people.csv')
# Sprider('http://data.stats.gov.cn/easyquery.htm?cn=C01','people.csv')

