# -*- coding: utf-8 -*-
import os
import json

class SumRecallPrecision():
    def sum_recall_precision(self,data1, label):
        tp, fp, fn, tn = 0, 0, 0, 0
        sum = 0
        for data2 in data1:
            first = data2.split(":")[0]
            second = data2.split(":")[1]
            if first != label and second != label:
                tn = tn + 1
            elif first == label and second == label:
                tp = tp + 1
            elif first == label and second != label:
                fn = fn + 1
            elif first != label and second == label:
                fp = fp + 1
            if first == label:
                sum = sum + 1
        recall = tp / (tp + fn)
        precision = tp / (tp + fp)
        f_score = 2 * tp / (2 * tp + fn + fp)
        accuracy_data = (tp + tn) / (tp + tn + fn + fp)
        return {"lable": label, "result": {"recall": recall, "precision": precision, "f_score": f_score,
                                           "accuracy":accuracy_data,"tp": tp, "tn": tn, "fn": fn, "fp": fp,
                                           "sum": sum}}

    def creat_file(self,path1):
        isexit = os.path.exists(path1)
        if not isexit:
            os.makedirs(path1)
            print(path1 + ' 创建成功')
        else:
            print("已经存在！")

    def get_test_r_p(self,input_path1,output_path1):
        team=["__label__ICS","__label__VSS","__label__RSS","__label__OAS"]
        with open(input_path1,"r",encoding='utf-8') as ff:
            data_list = json.load(ff)
        resu = []
        for data1 in team:
            aa=self.sum_recall_precision(data_list,data1)
            print(aa)
            resu.append(aa)
        with open(output_path1,"w",encoding='utf-8') as ft:
            json.dump(resu,ft,indent=1)





