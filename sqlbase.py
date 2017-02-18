#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    psw = Column(String(20))
    books = relationship('Book')

    def __init__(self, id, name ,psw):
        self.id = id
        self.name = name
        self.psw = psw

    def __repr__(self):
        return '<User %r>' % self.name

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id


    def __repr__(self):
        return '<User %r>' % self.name

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/user')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()