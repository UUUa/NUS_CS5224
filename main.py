# -*- coding: utf-8 -*-
import requests
import time
import json


from flask_cors import *
from flask import Flask, render_template, request, Response, redirect, url_for, jsonify

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return render_template('show.html')

@app.route('/data',methods=['POST'])
def show():
    data = request.form.to_dict()
    data['img'] = ""
    fileData = request.files
    if fileData:
        fileData = request.files['fileData']
        print("fileData===",fileData)
        t = time.strftime('%Y%m%d%H%M%S')
        new_fname = r'static/img/' + t + fileData.filename
        fileData.save(new_fname)  #save img
        data['img'] = new_fname

    returnData = {}
    returnData['code'] = 200
    returnData['msg'] = data
    print("returnData===",returnData)
    return returnData

if __name__ == "__main__":
    #change host->aliyun delete debug=true
    app.run(host='127.0.0.1', port=5000,debug=True)

