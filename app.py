import re
import requests
from flask import Flask, session, render_template, Blueprint, redirect, request
from views.page import page
from views.user import user
from config import Config
from db import db
app = Flask(__name__)
app.config.from_object(Config) #实列化配置
db.init_app(app)

#导入蓝图
app.register_blueprint(page.pb)
app.register_blueprint(user.ub)

@app.route("/")
def index():
    return redirect('/user/login')

#每个请求之前检查用户是否已登录。如果用户尚未登录，则将其重定向到登录页面
@app.before_request
def before_request():
    pat=re.compile(r'^/static')
    if re.search(pat,request.path):
        return
    if request.path=='/user/login':
        return
    if request.path=='/user/register':
        return
    username=session.get('username')
    if username:
        return None
    return redirect('/user/login')
@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
