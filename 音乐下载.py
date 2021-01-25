import os
from urllib.request import urlretrieve
from tkinter import *
import requests
import json
import jsonpath
from selenium import webdriver
#下载歌曲
def song_load(song_url,song_title):
    # 创建文件夹
    os.makedirs('music', exist_ok=True)
    path = 'music\{}.mp3'.format(song_title)
    text.insert(END, '歌曲：{},正在下载...'.format(song_title))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()

    urlretrieve(song_url, path)

    text.insert(END, '下载完毕：{},请试听'.format(song_title))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()
#搜索歌曲的id 名字
def get_music_name():
    # 获取输入框的歌曲名称
    name = entry.get()
    platform = var.get()
    headers = {

        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        # 'Referer': 'http://music.onlychen.cn/?name=%E4%BB%A5%E7%88%B6%E4%B9%8B%E5%90%8D&type=qq',
        # 'Origin': 'http://music.onlychen.cn',
        # 'Host': 'music.onlychen.cn',
        # 'Cookie': 'UM_distinctid=173e1b3fd7f683-018ad69a1b7ba2-3c634103-1fa400-173e1b3fd8084b; CNZZDATA1279162877=486742487-1597218425-null%7C1597462873',
        'X-Requested-With': 'XMLHttpRequest',

    }

    params = {
        'input': name,
        'filter': 'name',
        'type': platform,  # netease 网易云
        'page': '1',
    }
    # 拼接url
    url = 'http://music.onlychen.cn/'
    resp = requests.post(url,data=params,headers=headers)
    data = resp.json()
    print(data)
    title = jsonpath.jsonpath(data,"$..title")[0]
    author = jsonpath.jsonpath(data,"$..author")[0]
    url = jsonpath.jsonpath(data,"$..url")[0]
    print(title)
    print(author)
    print(url)
    # 下载歌曲
    song_load(url,title)
#搭建界面
# 1.创建画布
root = Tk()
# 2.添加标题
root.title('全网音乐下载器')
# 3.设置窗口大小
root.geometry('560x450+400+200')
# 4.标签控件
label = Label(root, text='请输入下载的歌曲：', font=('华文行楷', 20))
# 5.定位
label.grid()
# 6.输入框
entry = Entry(root, font=('隶书', 20))
# 7.定位
entry.grid(row=0, column=1)
# 单选按钮***
var = StringVar()
r1 = Radiobutton(root,text="网易云",variable=var,value='netease')
r1.grid(row=2, column=0)
# 8.列表框
text = Listbox(root, font=('楷书', 16), width=50, heigh=15)
# 9.定位 columnspan 组件横跨的列数
text.grid(row=3, columnspan=2)
# 点击下载按钮
button = Button(root, text='开始下载', font=('隶书', 15), command=get_music_name)
# 定位 sticky 对齐方式 W E N S  东南西北
button.grid(row=4, column=0, sticky=W)
# 退出程序的按钮
button1 = Button(root, text='退出程序', font=('隶书', 15), command=root.quit)
# 定位 sticky 对齐方式 W E N S  东南西北
button1.grid(row=4, column=1, sticky=E)
# 显示界面
root.mainloop()
