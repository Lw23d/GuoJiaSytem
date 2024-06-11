from utils.getPublicData import *

def Path(s):
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # 获取当前文件所在目录的上一级目录
    parent_dir = os.path.dirname(current_dir)
    # # 获取当前文件所在目录的上两级目录
    # grandparent_dir = os.path.dirname(parent_dir)
    file_path = parent_dir+s
    return file_path

#用于传输给首页数据
def getHomeCharData():
    data=get_yearData()
    return data
#用于获取人口数据信息的函数
def getTagsData():
    ptah=Path('\static\data\people.csv')
    result=get_TagsData(ptah)
    return result
def getPie():
    ptah=Path('\static\data\people.csv')
    result=get_Pie(ptah)
    return result

def getTable():
    ptah=Path('\static\data\people.csv')
    result=get_Table(ptah)
    return result

def getYear():
    ptah=Path('\static\data\people.csv')
    years=get_years(ptah)
    return years

def getSingleYear(year):
    result=getYearpopultion(year)
    return result

def getAgeData(year):
    result=get_AgeData(year)
    return result

def getBring(year):
    result=get_Bring(year)
    return result

def getEnducation(year):
    result=get_Enducation(year)
    return result

def getRate(year):
    result=get_PeopleRate(year)
    return result

def getPredictSum():
    return predict_Sum()

def getPredictRate():
    return predict_Rate()

def getPredictSex():
    return predict_sex()

def getPredicts():
    return predicts()

def getTableRate():
    ptah=Path('\static\data\people4.xls')
    return get_TableRate(ptah)
def getTableEnducation():
    ptah=Path('\static\data\people3.xls')
    return get_TableEnducation(ptah)

def getTableStruct():
    ptah=Path('\static\data\people1.xls')
    return get_TableStruct(ptah)

