from flask import render_template

#处理请求报错的函数
def errorResponse(errorMsg):
    return render_template('error.html',errorMsg=errorMsg)


