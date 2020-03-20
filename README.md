# Fasttext
这个是一个利用fasttext模型实现英文的二分类和多分类的库：
其中的fasttext_word是分类类，他有以下的功能
这个类有以下的功能
(1)可以得到训练模型
（2）可以得到整体测试模型的结果
（3）可以生成每一个数据具体的预测结果
sum_recall_precision.py 文件是一个计算统计每一个分类的recall，precision，tp，tn，fp，fn，f_score，accuracy，总数的类。它的输入文件的格式是
["__label__真正的结果:__label__预测的结果","__label__真正的结果:__label__预测的结果"]
