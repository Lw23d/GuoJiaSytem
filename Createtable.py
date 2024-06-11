from app import app
from db import db
from model.User import User
app.app_context().push()
db.create_all() #创建数据库
