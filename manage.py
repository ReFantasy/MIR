# coding=utf-8
from MIR import app, db
from MIR.models import SR
from flask_script import Manager

manage = Manager(app)

# 初始化数据库
@manage.command
def init_database():
     db.drop_all()
     db.create_all()

     # for i in range(0,14):
     #     use = SR(i%4,'医学图像', 'http://www.baidu.com', 'test'+str(i), 'tdl')
     #     db.session.add(use)
     # db.session.commit()




if __name__ == '__main__':
    manage.run()