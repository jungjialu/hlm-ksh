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
            if graph.nodes.match('HongLouMeng',new_data_name[i][0]).first() is None:
                if read_one_details_tuple(new_data_name[i][0]) is None:
                    dayquotation_node1 = Node('HongLouMeng','人物',new_data_name[i][0],
                                              name=new_data_name[i][0],
                                              名字=new_data_name[i][0]
                                              )
                    graph.create(dayquotation_node1)
                    node_guanxi_relationship(graph.nodes.match('HongLouMeng',new_data_name[i][3]).first(),'属于',dayquotation_node1)
                    print(new_data_name[i][0] + ': ' + "***无百度百科***节点已创建")
                else:
                    dayquotation_node1 = Node('HongLouMeng','人物',new_data_name[i][0],
                                              name=new_data_name[i][0],
                                              名字=new_data_name[i][0]
                                              )
                    node_guanxi_relationship(graph.nodes.match('HongLouMeng', new_data_name[i][3]).first(), '属于',dayquotation_node1)
                    print(new_data_name[i][0] + ': ' + "***有百度百科***节点已创建")
                    create_term_node(new_data_name[i][0])
            else:
                continue
    except Exception as e:
        print(e)
        print('***' + new_data_name[i][0] + '***' + "节点创建失败")
        pass
        return



def is_have_concept_node(stock_num):
    concept_node = graph.nodes.match('HongLouMeng', stock_num).first()
    return concept_node



def create_term_node(stock):
    try:
        ihcn_node = is_have_concept_node(stock)
        if ihcn_node is None:
            return
        new_data = read_one_details_tuple(stock)
        if new_data is None:
            return
        for i in range(1,len(new_data)):
                dayquotation1_node = Node('HongLouMeng','人物详情',new_data[i][1],
                                          name=new_data[i][1]
                                          )
                graph.create(dayquotation1_node)
                rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
                new_title = re.sub(rstr, "", str(new_data[i][0]))
                new_name = new_title.replace('xa0', '').replace('[', '').replace(']', '').replace('\'', '')
                node_guanxi_relationship(ihcn_node, str(new_name), dayquotation1_node)
                print(new_data[i][1] + ': ' + "******节点详情已创建")
    except Exception as e:
        print(e)
        print('***' + new_data[i][1] + '***' + "节点详情创建失败")
        pass
        return



def node_guanxi_relationship(dayquotation_node, guanxi, basicinformation_node):
    node_1_relationship_company_region = Relationship(dayquotation_node, guanxi, basicinformation_node)
    node_1_relationship_company_region['relation'] = guanxi
    graph.create(node_1_relationship_company_region)



def read_one_details_tuple(stock):
    csv_path = 'D:/百度百科/' + stock + '.txt';
    if not os.path.exists(csv_path):
        return
    with io.open(csv_path, "r", encoding='utf-8')as g:
        g_reader = csv.reader(g)
        triples_info = []  # 用来存储三元组信息
        for one_line in enumerate(g_reader):  # 抽取迭代器内行信息
            triples_info.append(one_line[1])
    return triples_info



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



