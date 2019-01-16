# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/dbtwo?charset=utf8", max_overflow=5)

Base = declarative_base()

class ClassList(Base):
    __tablename__ = "app01_classlist"
    cid = Column(Integer, primary_key=True)
    caption = Column(String(32))

class Teacher(Base):
    __tablename__ = "app01_teacher"
    tid = Column(Integer, primary_key=True)
    tname = Column(String(32))

class Course(Base):
    __tablename__ = "app01_course"
    cid = Column(Integer, primary_key=True)
    cname = Column(String(32))
    teacher_id = Column(Integer, ForeignKey("app01_teacher.tid"))

class student(Base):
    __tablename__ = "app01_student"
    GENDER_CHOICES = {
        "男" : 0,
        "女" : 1
    }
    sid = Column(Integer, primary_key=True)
    sname = Column(String(32))
    gender = Column(Integer)
    class_obj_id = Column(Integer, ForeignKey("app01_classlist.cid"))

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

