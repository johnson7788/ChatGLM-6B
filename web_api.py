#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/3/17 17:51
# @File  : wep_api.py
# @Author: 
# @Desc  :
import logging
import os
from flask import Flask, request, jsonify, abort
from transformers import AutoModel, AutoTokenizer

app = Flask(__name__)
# 日志保存的路径，保存到当前目录下的logs文件夹中
log_path = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(log_path):
    os.makedirs(log_path)
logfile = os.path.join(log_path, "api.log")
# 日志的格式
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s -  %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(logfile, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = model.eval()

@app.route("/api/chat", methods=['POST'])
def chat():
    """
    Args: 基于aspect的情感分析，给定实体，判断实体在句子中的情感
    """
    jsonres = request.get_json()
    # 可以预测多条数据
    input = jsonres.get('text')
    if not input:
        return jsonify({"response": "请输入文本"})
    response, history = model.chat(tokenizer, input, history=[])
    result = {"response": response}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4636, debug=False, threaded=True)
    print(input)