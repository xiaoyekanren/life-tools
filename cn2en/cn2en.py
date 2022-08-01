import pandas as pd
from pypinyin import *
import os


def readme():  # 没有作用，介绍了pandas的简单语法
    print("pandas and pypinyin's README")
    # pr = pd.read_excel("name.xlsx")  # 读excel
    # print(pd.read_excel("name.xlsx").head(10))  # 输出前10行
    # print(pd.read_excel("name.xlsx").loc[0].values)  # 输出第一行
    # print(pr.columns.size)  # 列数
    # print(pr.iloc[:, 0].size)  # 行数
    # print(pr.iloc[[0]].values[0][0])  # 第一行第一列，第二行第一列修改iloc里面的值


def twocolumn(filepath):
    pr = pd.read_excel(filepath)  # 读excel
    result = pd.DataFrame(columns=('cn_name', 'first', 'last'))  # 创建一个数据表

    line_sum = pr.iloc[:, 0].size  # 获取excel行数
    data = pr.head(line_sum)  # 读取上一条行数的这么多列

    for i in range(line_sum):
        # print(data.loc[i].values)  # 逐行读,这个地方不加[0]的话，会输出方括号
        cnname = data.loc[i].values[0]  # 逐行读,这个地方不加[0]的话，会输出方括号

        firstword = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[0]

        other = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[1:]
        otherword = ''
        for x in other:
            otherword = otherword + x

        # print(firstword, otherword)  # 打印看下姓，名
        result = result.append({'cn_name': cnname, 'first': firstword, 'last': otherword}, ignore_index=True)  # 在循环里添加一行数据到数据表

    # print('-------------------\n', result, '\n-------------------')  # 打印出来
    pd.DataFrame(result).to_excel('results.xlsx', sheet_name='Sheet1', index=False,
                                  header=True)  # 写入到excel的sheet1工作簿


def onecolumn():  # 没有作用，测试使用
    pr = pd.read_excel("name.xlsx")  # 读excel
    result2 = pd.DataFrame(columns=['name'])  # 创建一个1列数据表

    line_sum = pr.iloc[:, 0].size  # 获取行数
    data = pr.head(line_sum)  #

    for i in range(line_sum):
        firstword = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[0]

        other = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[1:]
        otherword = ''
        for x in other:
            otherword = otherword + x
        # print(firstword, otherword)  # 打印看下姓，名
        result2 = result2.append({'name': firstword + ' ' + otherword}, ignore_index=True)  # 写一列

    print('-------------------\n', result2, '\n-------------------')  # 写一列
    pd.DataFrame(result2).to_excel('C:\\Users\\MingMing\\Desktop\\cn2en\\results2.xlsx', sheet_name='Sheet1',
                                   index=False,
                                   header=True)  # 写一列


def addcolumntforexcel():  # 没有作用，另外一种写excel的方式，但是还没实现
    # 根据内容去新增两列，写英文，但是貌似不能保存在xlsx文件里，还需要改正
    pr = pd.read_excel("name.xlsx")  # 读excel
    line_sum = pr.iloc[:, 0].size  # 获取行数
    data = pr.head(line_sum)  #
    for i in range(line_sum):
        firstword = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[0]

        other = lazy_pinyin(data.loc[i].values, style=STYLE_NORMAL)[1:]
        otherword = ''
        for x in other:
            otherword = otherword + x
        print(firstword, otherword)  # 打印看下姓，名
        pr['first'] = firstword
        pr['last'] = otherword
    print(pr.head(line_sum))


inputfilepath = input('请输入excel文件路径：')  # 输入文件路径给inputfilepath，用这个在windows下路径可以不用输两个\\
twocolumn(inputfilepath)  # 调用twocolumn这个方法
current_file_path = os.path.dirname(os.path.abspath('cn2en.py'))  # 获得cn2en.py这个文件目录
print('already wrtie to ' + current_file_path + '\\results.xlsx')  # 打印一下输出的文件(results.xlsx)位置
os.system('pause')  # 使py不会自动退出，可以看到信息
