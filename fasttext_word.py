# -*- coding: utf-8 -*-
import json
import fasttext
import os

def creat_file(path1):
    isexit = os.path.exists(path1)
    if not isexit:
        os.makedirs(path1)
        print(path1 + ' 创建成功')
    else:
        print("已经存在！")
def modul_train_test(data1,test_path,train_path,output_model_path,output_overall_path,
                     test_json_path,label_result_path,
                     learn_rate,epoch_data,dim_data,wordngrams):
    #data1：是要测试的数据起的名字，这里一定要是数字
    #test_path:是测试数据的路径，注意测试数据是txt格式的文件
    #train_path：是训练数据的路径，注意这里的数据是txt格式的文件
    #output_model_path：是模型的存储文件夹
    #output_overall_path：是整体结果的存储数据的文件夹
    #test_json_path：是测试数据的路径，注意这里的数据是json格式的，数据放在list中，结构是{"label":"","banner":""}
    #label_result_path：是测试数据每一个具体预测label的数据的存储文件夹
    all_data =[]
    print(data1)
    input_path3 = output_model_path+"\\"+"train_"+str(data1)+".bin"
    path2 = output_overall_path+"\\"+"overall_result"+str(data1)+".json"
    model = fasttext.train_supervised(input=train_path, lr=learn_rate, epoch=epoch_data
                                           , wordNgrams=wordngrams, bucket=200000, dim=dim_data, loss='hs', thread =7)
    model.save_model(input_path3)
    result =model.test(test_path)
    print(result)
    bb= {"epoch":data1,"precision":result[1],"recall":result[2]}
    all_data.append(bb)
    with open(path2,"w",encoding='utf-8') as ff:
        json.dump(all_data,ff,indent=1)
    all_data2 = []
    with open(test_json_path, "r", encoding='utf-8') as frr:
        data_list = json.load(frr)
        for data3 in data_list:
            first = data3["label"]
            second = model.predict(data3["banner"])[0][0]
            all_data2.append(first + ":" + second)
    path1 = label_result_path+"\\"+"label_result_"+str(data1)+".json"
    with open(path1, "w", encoding='utf-8') as ft:
        json.dump(all_data2, ft, indent=1)

