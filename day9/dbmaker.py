# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine=create_engine("mysql+pymysql://root:jiang123@localhost/jiang",
                                    encoding='utf-8', echo=True)
Base=declarative_base()
class Student(Base):
    __tablename__='student'
    sid=Column(Integer,primary_key=True)
    sname=Column(String(32))
    gender=Column(String(8))
    class_id=Column(Integer)
Base.metadata.create_all(engine)

def insert(session,table_obj):#table_name like---- Student
    session.add(table_obj)
    session.commit()

def query(session,table_name,**kwargs):
    result = session.query(table_name).filter_by(**kwargs).first()
    return result

def queryall(session,table_name):
    result = session.query(table_name).all()
    return result

def alter(session,table_name,new_name,**kwargs):
    my_user = session.query(table_name).filter_by(**kwargs).first()
    my_user.sname = new_name
    Session.commit()

# def delete(session,table_name,**kwargs):
#     session.

Session_class=sessionmaker(bind=engine)
Session=Session_class()
# student=Student(sname='酷'.encode(encoding='utf-8'),gender='男'.encode(encoding='utf-8'),class_id=3)
# insert(Session,student)
# result=queryall(Session,Student)
# print(result)
# alter(Session,Student,'chiang',sname='张三'.encode())
# for i in Session.query(Student).filter(Student.class_id<3).all():
#     print(i.sname)
# print(Session.query(Student).filter(Student.sname.like('张%'.encode())).count())
# for i in Session.query(Student).group_by(Student.sname).all():
#     print(i.sid,i.sname,i.gender,i.class_id)
# from sqlalchemy import func
# print(Session.query(func.count(Student.sname),Student.sname).group_by(Student.sname).all() )