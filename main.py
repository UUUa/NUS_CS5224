# -*- coding: utf-8 -*-
import requests
import time
import json
import filetype  # check the filetype
import logging


from flask_cors import *
from flask import Flask, render_template, request, Response, redirect, url_for, jsonify

with open("config.json", "r") as f:
    load_dict = json.load(f)
    print(load_dict)
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return render_template('show.html')

@app.route('/data',methods=['POST']) # route('/data') show() --  #check file funtion
def show():
    data = request.form.to_dict()

    fileData = request.files

    if fileData:
        file = request.files['fileData']
        files = {
            "file": ("filename", file)
        }
        # t = time.strftime('%Y%m%d%H%M%S')
        # file_path = r'static/img/' + t + file.filename
        # file.save(file_path)  # save file
        #这里判断上传的文件是不是txt？文件
        # if filetype.guess(file_path).extension == 'txt??': # maybe it's txt?
        #     print("testFile")
        #     #在这里处理file是不是钓鱼的
        # else:
        #     logging.info("invalid file to check! please check!") #取决于我们能检测什么类型 如果全类型就不用这一步
        url = load_dict['api_url'] + ':9091/url'
        json_data = json.dump({'url': data['url']})
        r = requests.post(url, files=files)
        print(r.text)
    else:
        logging.info("no file.")

    #change data and return
    data = r.text #for test

    returnData = {}
    returnData['code'] = 200
    returnData['msg'] = data
    print("returnData===",returnData)
    return returnData

@app.route('/data1',methods=['POST'])  #check url function  route('/data1')
def show1():  #function show1()
    data = request.form.to_dict()
    print(data)
    url = load_dict['api_url'] + ':9091/url'
    json_data = json.dump({'url': data['url']})
    r = requests.post(url, data=json_data)
    print(r.text)

    # check url and change data
    data = "unsafe"   # change the data

    returnData = {}
    returnData['code'] = 200
    returnData['msg'] = r.text  #return data -- ok
    print("returnData===",returnData)
    return returnData

@app.route('/check',methods=['POST'])  #check history function  route('/check')
def show2():  #function show2()
    url = load_dict['api_url'] + ':9091/history'
    r = requests.post(url)
    print(r.text)

    returnData = {}
    returnData['code'] = 200
    returnData['msg'] = r.text  #return data -- ok
    print("returnData===", returnData)
    return returnData

if __name__ == "__main__":
    #change host->aliyun delete debug=true
    app.run(host='127.0.0.1', port=5000,debug=True)

