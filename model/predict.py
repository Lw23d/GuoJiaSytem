from sklearn.linear_model import LinearRegression
import os
#保留两位小数
def Round2(v,index):
    result=[]
    for i in v:
        if index==1:
          result.append(round(i,2))
        else:
          result.append(round(i))
    return result
#保留整数
def Round(v):
    result=[]
    for i in v:
        result.append(round(i))
    return result

def Path(s):
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # 获取当前文件所在目录的上一级目录
    parent_dir = os.path.dirname(current_dir)
    # # 获取当前文件所在目录的上两级目录
    # grandparent_dir = os.path.dirname(parent_dir)
    file_path = parent_dir+s
    return file_path
import pandas as pd

#通过机器学习来补充缺失值
def predict(x,y,pred_x,index):
    model=LinearRegression()
    model.fit(x,y)
    predict_y=model.predict(pred_x)
    predict_y=Round2(predict_y,index)
    return predict_y

#利用预测值来填充缺失值
def fillNull():
    path=Path('\static\data\people1.xls')
    data=pd.read_excel(path)
    data['年份']=data['年份'].astype(str) #将数据转为字符串型
    data['年份']=data['年份'].apply(lambda x:x[:-1])
    data['年份']=data['年份'].astype(int)
    columns=['0-14岁人口(万人)','15-64岁人口(万人)','总抚养比(%) ','少儿抚养比(%)','老年抚养比(%)'] #待填补的数据列
    x=data['年份'][1:].tolist()
    X=[]
    for i in x:
        a=[]
        a.append(i)
        X.append(a)
    for s in columns:
        Y=data[s][1:].tolist()
        pred_y=predict(X,Y,[[2023]],1)
        data.at[0,s]=pred_y
    return  data

def sumPeope():
    path1=Path('\static\data\people.csv')
    path2=Path('\static\data\people4.xls')
    data1=pd.read_csv(path1,encoding='utf-8')
    data2=pd.read_excel(path2)
    data=pd.DataFrame()
    data['年份']=data1['年度']
    data['年末总人口(万人)']=data1['年末总人口(万人)']
    data['出生率(‰)']=data2['人口出生率(‰)'][::-1].values
    data['死亡率(‰)']=data2['人口死亡率(‰)'][::-1].values
    X=data[['出生率(‰)','死亡率(‰)']]
    Y=data[['年末总人口(万人)']]
    # 建立线性回归模型
    model = LinearRegression()
    model.fit(X,Y)
    rates=People_rate()
    # 预测未来5年的人口总数
    future_data = pd.DataFrame({'出生率(‰)':rates[0], '死亡率(‰)':rates[1]})
    x_text=future_data[['出生率(‰)','死亡率(‰)']]
    future_predictions = model.predict(x_text)
    result=[]
    for i in range(len(future_predictions)):
        result.append(future_predictions[i][0])
    return  Round(result)

def People_rate():
    path=Path('\static\data\people4.xls')
    data=pd.read_excel(path)
    data['时间']=data['时间'].astype(str) #将数据转为字符串型
    data['时间']=data['时间'].apply(lambda x:x[:-1])
    data['时间']=data['时间'].astype(int)
    x=data['时间'][::-1].tolist()
    X=[]
    for i in x:
        a=[]
        a.append(i)
        X.append(a)
    Y1=data['人口出生率(‰)'][::-1].tolist()
    Y2=data['人口死亡率(‰)'][::-1].tolist()
    pred_y1=predict(X,Y1,[[2024],[2025],[2026],[2027],[2028]],1)
    pred_y2=predict(X,Y2,[[2024],[2025],[2026],[2027],[2028]],1)
    return [pred_y1,pred_y2]

def predict_Sex():
    path=Path('\static\data\people.csv')
    data=pd.read_csv(path,encoding='utf-8')
    data['年度']=data['年度'].astype(str) #将数据转为字符串型
    data['年度']=data['年度'].apply(lambda x:x[:-1])
    data['年度']=data['年度'].astype(int)
    x=data['年度'].tolist()
    X=[]
    for i in x:
        a=[]
        a.append(i)
        X.append(a)
    Y1=data['男性人口(万人)'].tolist()
    Y2=data['女性人口(万人)'].tolist()
    pred_y1=predict(X,Y1,[[2024],[2025],[2026],[2027],[2028]],0)
    pred_y2=predict(X,Y2,[[2024],[2025],[2026],[2027],[2028]],0)
    pred_y1=Round(pred_y1)
    pred_y2=Round(pred_y2)
    return [pred_y1,pred_y2]

