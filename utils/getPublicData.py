from os.path import join, dirname, realpath
from model.predict import *
import pandas as pd

def Path(s):
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # 获取当前文件所在目录的上一级目录
    parent_dir = os.path.dirname(current_dir)
    # # 获取当前文件所在目录的上两级目录
    # grandparent_dir = os.path.dirname(parent_dir)
    file_path = parent_dir+s
    return file_path

#获取年份总人口数：
def get_yearData():
    result=[]
    ptah=Path('\static\data\people.csv')
    data=pd.read_csv(ptah, encoding='utf-8')
    sums=data['年末总人口(万人)']
    data['年度']=data['年度'].astype(str) #将数据转为字符串型
    data['年度']=data['年度'].apply(lambda x:x[:-1])
    years=data['年度'].astype(int)
    result.append(sums.tolist())
    result.append(years.tolist())
    return result

def get_TagsData(fileName):
    result={}
    data=pd.read_csv(fileName,encoding='utf-8')
    #获取年份人口总数最大值
    max_total_population=data['年末总人口(万人)'].max()
    result['最高人口数量']=max_total_population
    sum_population=data['年末总人口(万人)'].sum()
    man_population=data['男性人口(万人)'].sum()
    woman_population=data['女性人口(万人)'].sum()
    #求出男女性占比
    man_rate=man_population/sum_population
    result['男性平均占比']=round(man_rate,2)
    woman_rate=woman_population/sum_population
    result['女性平均占比']=round(woman_rate,2)
    ptah=Path('\static\data\people2.xls')
    data2=pd.read_excel(ptah)
    avg_age=data2[data2['年份']=='2020年']['平均预期寿命(岁)'].values[0]
    result['平均预期寿命']=avg_age
    return result

def get_Pie(fileName):
    result={}
    data=pd.read_csv(fileName,encoding='utf-8')
    sum_population=data['年末总人口(万人)'].sum()
    city_rate=round(data['城镇人口(万人)'].sum()/sum_population,2)
    countriside=round(data['乡村人口(万人)'].sum()/sum_population,2)
    result['city']=city_rate
    result['countriside']=countriside
    return result

def get_Table(fileName):
     result=[]
     data=pd.read_csv(fileName,encoding='utf-8')
     data['年度']=data['年度'].astype(str) #将数据转为字符串型
     data['年度']=data['年度'].apply(lambda x:x[:-1])
     data['年度']=data['年度'].astype(int)
     years=data['年度'].tolist()
     sums=data['年末总人口(万人)'].tolist()
     manPeople=data['男性人口(万人)'].tolist()
     womanPeople=data['女性人口(万人)'].tolist()
     city=data['城镇人口(万人)'].tolist()
     countriside=data['乡村人口(万人)'].tolist()
     i=0
     while i<len(years):
         a=[]
         a.append(years[i])
         a.append(sums[i])
         a.append(manPeople[i])
         a.append(womanPeople[i])
         a.append(city[i])
         a.append(countriside[i])
         result.append(a)
         i+=1
     return result

def get_TableRate(fileName):
     result=[]
     data=pd.read_excel(fileName)
     data['时间']=data['时间'].astype(str) #将数据转为字符串型
     data['时间']=data['时间'].apply(lambda x:x[:-1])
     data['时间']=data['时间'].astype(int)
     years=data['时间'].tolist()
     sums=data['人口出生率(‰)'].tolist()
     manPeople=data['人口死亡率(‰)'].tolist()
     womanPeople=data['人口自然增长率(‰)'].tolist()
     i=0
     while i<len(years):
         a=[]
         a.append(years[i])
         a.append(sums[i])
         a.append(manPeople[i])
         a.append(womanPeople[i])
         result.append(a)
         i+=1
     return result

def get_TableStruct(fileName):
     result=[]
     data=pd.read_excel(fileName)
     data=data.dropna() #除去缺失值
     data['年份']=data['年份'].astype(str) #将数据转为字符串型
     data['年份']=data['年份'].apply(lambda x:x[:-1])
     data['年份']=data['年份'].astype(int)
     years=data['年份'].tolist()
     sums=data['0-14岁人口(万人)'].astype(int).tolist()
     manPeople=data['15-64岁人口(万人)'].astype(int).tolist()
     womanPeople=data['65岁及以上人口(万人)'].astype(int).tolist()
     i=0
     while i<len(years):
         a=[]
         a.append(years[i])
         a.append(sums[i])
         a.append(manPeople[i])
         a.append(womanPeople[i])
         result.append(a)
         i+=1
     return result

def get_TableEnducation(fileName):
     result=[]
     data=pd.read_excel(fileName)
     data=data.dropna() #除去缺失值
     data['时间']=data['时间'].astype(str) #将数据转为字符串型
     data['时间']=data['时间'].apply(lambda x:x[:-1])
     data['时间']=data['时间'].astype(int)
     years=data['时间'].tolist()
     data1=data['6岁及6岁以上未上过学人口数'].astype(int).tolist()
     data2=data['6岁及6岁以上小学人口数'].astype(int).tolist()
     data3=data['6岁及6岁以上初中人口数'].astype(int).tolist()
     data4=data['6岁及6岁以上高中人口数'].astype(int).tolist()
     data5=data['6岁及6岁以上大专及以上人口数'].astype(int).tolist()
     i=0
     while i<len(years):
         a=[]
         a.append(years[i])
         a.append(data1[i])
         a.append(data2[i])
         a.append(data3[i])
         a.append(data4[i])
         a.append(data5[i])
         result.append(a)
         i+=1
     return result

def get_years(fileName):
    data=pd.read_csv(fileName,encoding='utf-8')
    data['年度']=data['年度'].astype(str) #将数据转为字符串型
    data['年度']=data['年度'].apply(lambda x:x[:-1])
    data['年度']=data['年度'].astype(int)
    return data['年度'].tolist()

def getYearpopultion(year):
    result=[]
    ptah=Path('\static\data\people.csv')
    data=pd.read_csv(ptah,encoding='utf-8')
    year=str(year)+'年'
    data_year=data[data['年度']==year].iloc[:,1:]
    data_year_lables=data_year.columns.tolist()
    data_year_lables=[label.replace("(万人)", "") for label in data_year_lables]
    data_year_values=data_year.values[0].tolist()
    result.append(data_year_lables)
    result.append(data_year_values)
    return result

#获取年份人口各年龄阶段占比
def get_AgeData(year):
    data=fillNull()
    age1=data[data['年份']==year].iloc[:,2:5]
    age1_values=age1.values[0].tolist()
    result=[]
    sum=age1_values[0]+age1_values[1]+age1_values[2]
    for age in age1_values:
        a=round(age/sum,2)
        result.append(a)
    return result

def get_Bring(year):
    data=fillNull()
    age1=data[data['年份']==year].iloc[:,6:]
    age1_values=age1.values[0].tolist()
    return age1_values

def get_Enducation(year):
    ptah=Path('\static\data\people3.xls')
    data=pd.read_excel(ptah)
    pd.set_option('display.float_format', lambda x: '%.0f' % x) #禁用科学计数法显示数值
    # 循环处理每一列的空值
    for column in data.columns:
        if data[column].isnull().any():
            mean_value = data[column].min()
            # 用每列的最小值填充空值
            data[column].fillna(mean_value, inplace=True)
    year=str(year)+'年'
    result=data[data['时间']==year].iloc[:,1:]
    result_values=result.values[0].tolist()
    return result_values

def get_PeopleRate(year):
    ptah=Path('\static\data\people4.xls')
    data=pd.read_excel(ptah)
    year=str(year)+'年'
    rates=data[data['时间']==year].iloc[:,1:]
    rates=rates.values[0].tolist()
    return rates

def predict_Sum():
    result=sumPeope()
    return result

def predict_Rate():
    result=People_rate()
    return result

def predict_sex():
    return predict_Sex()

#计算自然增长率
def natureRate(list1,list2):
    a=[]
    for i in range(len(list1)):
        a.append(round(list1[i]-list2[i],2))
    return a

def predicts():
    result=[]
    sums=predict_Sum()
    rates=predict_Rate()
    nature_rate=natureRate(rates[0],rates[1])
    sexs=predict_sex()
    year=2024
    for i in range(len(sums)):
        a=[]
        a.append(year)
        a.append(sums[i])
        a.append(rates[0][i])
        a.append(rates[1][i])
        a.append(nature_rate[i])
        a.append(sexs[0][i])
        a.append(sexs[1][i])
        result.append(a)
        year+=1
    return result

