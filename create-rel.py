from py2neo import Graph, Node, Relationship
from query.config import graph
import json
import re
import os
import io
import csv

'''         
            人物及人物介绍节点
'''




def create_dayquotation_node(csv_path):
    try:
        new_data_name = read_one_three_tuple(csv_path)
        for i in range(len(new_data_name)):
            node_guanxi_relationship(graph.nodes.match('人物',new_data_name[i][1]).first(),new_data_name[i][2],graph.nodes.match('人物',new_data_name[i][0]).first())
            print(new_data_name[i][2] + ': ' + "******关系节点已创建")
    except Exception as e:
        print(e)
        print('***' + new_data_name[i][0]+ new_data_name[i][1]+ new_data_name[i][2]+'***' + "节点创建失败")
        pass
        return





def node_guanxi_relationship(dayquotation_node, guanxi, basicinformation_node):
    node_1_relationship_company_region = Relationship(dayquotation_node, guanxi, basicinformation_node)
    node_1_relationship_company_region['relation'] = guanxi
    graph.create(node_1_relationship_company_region)





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



