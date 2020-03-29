from py2neo import Graph, Node, Relationship
from query.config import graph
import json
import re
import os
import io
import csv

'''         
            府邸
'''


def create_dayquotation_node(csv_path):
    try:
        new_data_name = read_one_three_tuple(csv_path)
        for i in range(len(new_data_name)):
            if graph.nodes.match('HongLouMeng',new_data_name[i][3]).first() is None:
                dayquotation_node = Node('HongLouMeng','府邸',new_data_name[i][3],
                                          name=new_data_name[i][3],
                                          府邸=new_data_name[i][3]
                                          )
                graph.create(dayquotation_node)
                print(new_data_name[i][3] + ': ' + "***节点已创建")
            else:
                continue
    except Exception as e:
        print(e)
        print('***' + new_data_name[i][3] + '***' + "节点创建失败")
        pass
        return





def read_one_three_tuple(path):
    with io.open(path, "r", encoding='utf-8')as g:
        g_reader = csv.reader(g)
        triples_info = []  # 用来存储三元组信息
        for one_line in enumerate(g_reader):  # 抽取迭代器内行信息
            triples_info.append(one_line[1])
    return triples_info





if __name__ == '__main__':
    path = 'D:/hlm-ksh/data/红楼梦人物.csv'
    create_dayquotation_node(path)



