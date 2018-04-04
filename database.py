# -*- coding: utf-8 -*-
"""
Created on Mon May 22 08:51:22 2017

@author: Cher
"""
import sys
import math
from neo4j.v1 import GraphDatabase
import json

#进度条：
def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 40)
    rate_nums = math.ceil(rate * 100)
    r = '\r[%s%s]%d%%' % (">"*rate_num, " "*(40-rate_num), rate_nums, )
    sys.stdout.write(r)
    sys.stdout.flush()

#生成存储节点的Cypher代码
def geneNode(session, dic):
    cypher = "CREATE (a:Persons {name:"
    cypher += "\'" + dic["name"] + "\'})"
    #cypher = cypher + "," + "url" + ":\'" + dic["url"] + "\'})"
    # cypher = CREATE(a:Persons{name: '范冰冰', url: '……'
    session.run(cypher)
    
def geneNewnode(session, name):
    cypher = "CREATE (a:Persons {name:"
    cypher += "\'" + name + "\'})"
    #cypher = cypher + "," + "url" + ":\'" + dic["url"] + "\'})"
    # cypher = CREATE(a:Persons{name: '范冰冰', url: '……'
    session.run(cypher)

#生成存储关系的Cypher代码
def geneRela(session, dic):
    # dic={"张传美": "母亲", "name": "范冰冰", "黄晓明": "搭档", "冯绍峰": "搭档", "葛优": "搭档", "李晨": "男友", "范丞丞": "弟弟"}
    node1 = dic["name"]
    all_relations = dic.keys()
    relation_length = len(all_relations)
    if(relation_length < 2): #如果只包含name，直接返回
        return;
        
    for relation in all_relations:
        if relation != "name":
            #先判断后续节点是否在图中了（xxx是否已经存在）
            if(not isInGraph(session, relation)):   
                geneNewnode(session, relation)  #不在图中,则创建节点
            relation = relation.replace('（', '');   relation = relation.replace('）', '');
            relation = relation.replace('、', '');   relation = relation.replace('，', '');
            relation = relation.replace('《', '');   relation = relation.replace('》', '');
            relation = relation.replace('：', '');   relation = relation.replace('；', '');
            relation = relation.replace('“', '');    relation = relation.replace('”', '');
            relation = relation.replace('！', '');    relation = relation.replace('？', '');
            relation = relation.replace('【', '');    relation = relation.replace('】', '');
            relation = relation.replace(' ', ''); 
                                   
#            if(len(relation) == 0):
#                relation = '关系';
                                    #然后建立节点间的关系
            cypher = "MATCH (node1:Persons {name:" + "\'" + node1 + "\'" + "}) " + "MATCH (node2:Persons {name:" + "\'" + relation + "\'" +"}) " + "CREATE (node1)-[relation:"+ dic[relation] +"]->(node2)";
        
            session.run(cypher);

#判断节点是否在图中
def isInGraph(session, name):
    result = session.run("MATCH (a:Persons{name:" + "\'" + name + "\'" + "}) RETURN a.name")      
    
    count = 0;    
    for i in result.records():
        count += 1;
    return count;

#登录数据库，生成会话
reload(sys) 
sys.setdefaultencoding('utf-8')
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "ChenJing"))
session = driver.session()

session.run('MATCH (n:Persons) DETACH DELETE n')



#从本地读取节点数据
print('Loading Nodes and Features....')
f = open('nodes.json', 'r')
nodes_data = json.load(f)
f.close()

#插入节点数据
print('Insert Nodes and Features to Neo4j:')
# len(nodes_info),得到nodes_info[],这个数组的长度，也就是里面元素的个数
for i in range(0,len(nodes_data)):
    geneNode(session, nodes_data[i])
#    view_bar(i, len(nodes_data))


#从本地读取关系数据
print('\n\nLoading Relationships....')
f = open('relation.json', 'r')
relations_data = json.load(f)
f.close()

#插入关系
print('Insert Relationships to Neo4j:')
for i in range(0,len(relations_data)):
#    view_bar(i, len(relations_data))
    geneRela(session, relations_data[i])

session.close()

