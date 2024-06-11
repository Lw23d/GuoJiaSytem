from flask import Flask, session, render_template, Blueprint, request
from utils.getPageData import *
#创建蓝图(页面的入口)
pb=Blueprint('page',__name__,url_prefix='/page',template_folder='templates')

@pb.route('/home')
def home():
    username=session.get('username')
    xcharData=getHomeCharData()[1][10:20]
    ycharData=getHomeCharData()[0][10:20]
    tags=getTagsData()
    pie=getPie()
    predictNumber=getPredictSum()
    sexs=getPredictSex() #返回一个二维数组
    if sexs[0][0]>sexs[1][0]:
        sex='男'
    elif sexs[0][0]<sexs[1][0]:
        sex='女'
    else:
        sex='均等'
    predictData=getPredicts()
    return render_template('index.html',username=username,xcharData=xcharData,
                           ycharData=ycharData,today=2024,predtoday="2024~2028",peopleNumber=predictNumber[0],sex=sex,maxPopulation=tags['最高人口数量'],manRate=tags['男性平均占比']*100,womanRate=tags['女性平均占比']*100,
                           avgAge=tags['平均预期寿命'],v1=pie['city'],v2=pie['countriside'],
                           predict_datas=predictData)

@pb.route('/tableData',methods=['GET','POST'])
def tableData():
     username=session.get('username')
     result=getTable()
     return render_template('tableData.html',username=username,datas=result)

@pb.route('/tableDataRate',methods=['GET','POST'])
def tableDataRate():
     username=session.get('username')
     result=getTableRate()
     return render_template('tableDataRate.html',username=username,datas=result)

@pb.route('/tableDataEducation',methods=['GET','POST'])
def tableDataEducation():
     username=session.get('username')
     result=getTableEnducation()
     return render_template('tableDataEducation.html',username=username,datas=result)

@pb.route('/tableDataStruct',methods=['GET','POST'])
def tableDataStruct():
     username=session.get('username')
     result=getTableStruct()
     return render_template('tableDataStruct.html',username=username,datas=result)

@pb.route('/Char',methods=['GET','POST'])
def Char():
    username=session.get('username')
    year_list=getYear()
    defaultyear=request.args.get('defaultyear') if request.args.get('defaultyear') else year_list[19]
    singleyear=getSingleYear(int(defaultyear))
    ages=getAgeData(int(defaultyear))
    bringData=getBring(int(defaultyear))
    enducationData=get_Enducation(int(defaultyear))
    rate=getRate(int(defaultyear))
    return render_template('Char.html',username=username,years=year_list,defaultyear=int(defaultyear),xdata=singleyear[0],
                           ydata=singleyear[1],age=ages,bringData=bringData,eData=enducationData,rate=rate)

@pb.route('/Page',methods=['GET','POST'])
def Page():
    return render_template('Page.html')
