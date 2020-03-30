# -*- coding: utf-8 -*-
#从的得到的整体数据中，对数据进行分割，按照每5%进行分割得到train和test
#2.把得到的train和test进行合并，得到相应的整体数据train和test
#3.把整体的train数据进行训练得到相应的模型
#4.对test进行预测，得到相应的label
#注：在这个过程中要创建文件夹
import json
import os
from sklearn.model_selection import train_test_split
def creat_file(path1):
    isexit = os.path.exists(path1)
    if not isexit:
        os.makedirs(path1)
        print(path1 + ' 创建成功')
    else:
        print("已经存在！")

input_path1 =r"D:\third_project\data\data\news_all_orig_data"
output_path1 = r"D:\third_project\data\data2\train2"
output_path2 = r"D:\third_project\data\data2\test2"
output_path3 = r"D:\third_project\data\data2\merage_train2"
output_path4 = r"D:\third_project\data\data2\merage_test2"

def split_data(data1,nu,path_train,path_test):
    path1 = input_path1+"\\"+data1+".json"
    print(data1)
    with open(path1,"r") as ff:
        data_list = json.load(ff)
        train, test = train_test_split(data_list, test_size=nu, random_state=42)
    with open(path_train+"\\"+"train_"+data1+".json","w",encoding='utf-8') as ft:
        json.dump(train,ft,indent=1)
    with open(path_test+"\\"+"test_"+data1+".json","w",encoding='utf-8') as ft:
        json.dump(test,ft,indent=1)
    print(data1)

def merage_data(input_path1,output_path1):
    files_list = os.listdir(input_path1)
    all_data = []
    for data in files_list:
        path1 = input_path1 + "\\" + data
        with open(path1, "r") as ff:
            data_list = json.load(ff)
            for data1 in data_list:
                all_data.append(data1)
    with open(output_path1, "w") as fd:
        json.dump(all_data, fd, indent=1)


type_data = ["M_ICS","M_RSS","M_VSS","M_OAS"]
num = [0.94,0.93,0.92,0.91,0.88,0.86,0.83,0.81,0.78,0.76,0.67,0.63,0.61,0.53,0.51]
for data2 in num:
    path_train = output_path1+"\\"+str(data2)
    creat_file(path_train)
    path_test = output_path2 +"\\"+str(data2)
    creat_file(path_test)
    for data3 in type_data:
        split_data(data3,data2,path_train,path_test)
    merage_train = output_path3+"\\"+"train"+str(data2)+".json"
    merage_data(path_train,merage_train)
    merage_test = output_path4 + "\\" +"test"+str(data2)+".json"
    merage_data(path_test,merage_test)
