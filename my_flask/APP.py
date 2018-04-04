# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:00:56 2017

@author: cher
"""
import sys
import json
from flask import Flask, request, render_template, jsonify

#reload(sys) 
#sys.setdefaultencoding('utf-8')
app = Flask(__name__)


@app.route("/index1", methods=["GET"])
def index1():
    return render_template("index1.html")


@app.route("/index2", methods=["GET"])
def index2():
    return render_template("index2.html")


#
@app.route("/nodes", methods=["GET"])
def weather():
    if request.method == "GET":
        f = open('nodes.json', 'r', encoding='utf-8')
        nodes_data = json.load(f)
        f.close()
        f1 = open('relation11.json', 'r', encoding='utf-8')
        relation_data = json.load(f1)
        f1.close()
        
    return jsonify(name = [x["name"] for x in nodes_data],
                   url = [x["url"] for x in nodes_data],
                   node1 = [x["node1"] for x in relation_data],
                   node2 = [x["node2"] for x in relation_data],
                   relation = [x["relation"] for x in relation_data])


if __name__ == "__main__":
  app.run()