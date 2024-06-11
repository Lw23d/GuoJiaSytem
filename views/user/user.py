from flask import Flask,session,render_template,Blueprint,redirect,request
from model.User import User
from utils.errorRespone import errorResponse

from db import db

#创建蓝图(页面的入口)
ub=Blueprint('user',__name__,url_prefix='/user',template_folder='templates')

@ub.route('/login',methods=['GET','POST']) #methods设置允许以什么方式进行访问
def login():
    if request.method=='POST':
        user=User.query.filter_by(user_name=request.form['username'],user_password=request.form['password']).first()
        if user:
            session['username']=user.user_name
            return redirect('/page/home')
        else:
            return errorResponse("输入的密码或账号出错")
    else:
        return render_template('login.html')

@ub.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        user=User.query.filter_by(user_name=request.form['username']).first()
        if user:
            return errorResponse("改用户名已存在")
        newUser=User(user_name=request.form['username'],user_password=request.form['password'])
        db.session.add(newUser)
        db.session.commit()
        return redirect('/user/login')
    else:
        return render_template('register.html')

@ub.route('/logOut',methods=['GET','POST'])
def logOut():
    session.clear() #清空用户记录
    return redirect('/user/login')
