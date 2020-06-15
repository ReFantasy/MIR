# coding=utf-8

from MIR import db
import random
from datetime import datetime

class SR(db.Model):
    '''
    SR: Source Record
    一条资源记录
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 类型：期刊=0 会议=1 项目=2 博客=3 书籍=4
    type = db.Column(db.Integer)

    # 名称
    name  = db.Column(db.String(128))

    # 地址
    source_url = db.Column(db.String(2048))

    # 描述
    description = db.Column(db.Text, nullable=False)

    # 上传者
    uploader = db.Column(db.String(256))

    # 附件地址
    appendix_name = db.Column(db.String(2048))

    # 上传日期
    upload_date = db.Column(db.DateTime)

    def __init__(self, type, name, source_url, description, uploader, appendix_name=None):
        self.type = type
        self.name = name
        self.source_url = source_url
        self.description = description
        self.uploader = uploader
        self.upload_date = datetime.now()
        self.appendix_name = appendix_name

    def __repr__(self):
        return '<Record:id %d, name %s>'%(self.id, self.name)
