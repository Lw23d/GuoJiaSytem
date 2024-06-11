#定义配置类
class Config(object):
    #配置连接数据库
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Lyb15260072876@127.0.0.1:3306/project"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_ECHD=False #打印原生sql语句，便于观察测试
    SECRET_KEY="123456"
