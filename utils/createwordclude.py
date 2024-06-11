from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="SimHei"
plt.rcParams["axes.unicode_minus"]=False
import imageio
mk = imageio.imread("../static/word.jpg")
# 构建词云的文本数据
texts=[]
with open('../static/word.txt',"r",encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        texts.append(line.strip())
#获取文本字符串
text=" ".join(texts)
# 创建WordCloud对象
wordcloud = WordCloud(font_path = "C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc",width=100, height=300,mask=mk, background_color='white').generate(text)
# 绘制词云
plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# 保存词云图到文件
wordcloud.to_file("../static/wordcloud.png")
# 显示词云图
plt.show()
