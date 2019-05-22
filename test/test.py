# import pprint
# csvfileid = 'C:/Users/Administrator/Desktop/logger_26_3_2019_14_1_3.csv'
# listlines = open(csvfileid, 'r')
# lines1 = listlines.read().splitlines()
# pprint.pprint(lines1)
# list1 = {}
# for line in lines1:
#     data = 'HT-GIG:'
#     if data in line:
#         print(line)
#     else:
#         print('for循环结束')
#     # pprint.pprint(list1)
# import csv
# import pprint
# birth_data = []
# csvfileid1 = 'C:/Users/Administrator/Desktop/logger_26_3_2019_14_1_3.csv'
# with open(csvfileid1) as csvfile:
#     csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
#     # birth_header = next(csv_reader)# 读取第一行每一列的标题
#     data = 'HT-GIG:'
#     for data in csv_reader:  # 将csv 文件中的数据保存到birth_data中
#         birth_data.append(data)
#     pprint.pprint(birth_data)
# # birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式
# birth_data = np.array(birth_data)  # 将list数组转化成array数组便于查看数据结构
# birth_header = np.array(birth_header)
# print(birth_data.shape)  # 利用.shape查看结构。
# print(birth_header.shape)
#
import pandas as pd

csv_data = pd.read_csv('C:/Users/Administrator/Desktop/logger_26_3_2019_14_1_3.csv')
print(csv_data.shape)  # (189, 9)
N = 500
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data.shape)  # (5, 9)
train_batch_data = csv_batch_data[list(range(3, 6))]  # 取这20条数据的3到5列值(索引从0开始)
print(train_batch_data)