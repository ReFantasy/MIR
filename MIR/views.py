# coding=utf-8

from MIR import app, db
from MIR.models import SR
from flask import render_template,request,send_from_directory, redirect, url_for,flash
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from datetime import datetime
import os

app.secret_key = 'random string'

@app.route('/')
def index():
    #records = SR.query.all()
    records = SR.query.order_by(SR.upload_date.desc()).all()
    page_index = 0
    return render_template('index.html', data=records,page_index=page_index)

@app.route('/<int:page_index>')
def pageindex(page_index):
    records = SR.query.order_by(SR.upload_date.desc()).all()
    return render_template('index.html', data=records, page_index=page_index)


# 指定请求方式，如果不指定，则无法匹配到请求
@app.route("/upload", methods=("GET", "POST"))
def upload():
    # GET请求
    if request.method == "GET":
        return render_template("upload.html")
    # POST请求
    if request.method == "POST":
        # 获取数据并转化成字典
        new_record = request.form.to_dict()

        # 保存附件
        file = request.files['file']
        print(file)
        filename = file.filename
        print(filename)
        if filename != None and filename!='':
            save_path = os.path.join(app.config["UPLOAD_DIR"], "static", filename)
            print(save_path)
            file.save(save_path)
        else:
            filename = None

        print(new_record['source_url'])

        URL = new_record['source_url']
        if URL.find("http://") == -1 and URL.find("https://") ==-1:
            URL = "http://"+URL
        sr = SR(new_record['type'], new_record['name'], URL,new_record['description'],new_record['uploader'], filename)
        db.session.add(sr)
        db.session.commit()

        flash(datetime.now())
        return redirect(url_for('upload'))

@app.route("/appendix/<filename>")
def appendix(filename):
    if request.method=="GET":
        if os.path.isfile(os.path.join(app.config["UPLOAD_DIR"],'static', filename)):
            return send_from_directory('static',filename,as_attachment=True)
        else:
            return "Not such file"

