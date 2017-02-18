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

    def __init__(self, id, name,psw):
        self.id = id
        self.name = name
        self.psw = psw

    def __repr__(self):
        return '<User %r>' % self.name

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

    def __init__(self, id, book_name, user_id):
        self.id = id
        self.book_name = book_name
        self.user_id = user_id


    def __repr__(self):
        return '<User %r>' % self.name

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/user')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='1', name='Bob0')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).outerjoin(Book).filter(Book.user_id == '2').one()#连表查询  定义好主键
user = session.query(User).join(Book, Book.user_id == User.id).filter(Book.user_id == '2').one()#连表查询  自己指定连接
book = session.query(Book).join(User, Book.user_id == User.id).filter(Book.user_id == '2').one()#连表查询  自己指定连接
print user.name
print book.book_name
# user = session.query(User).filter(User.id=='5').one()
# # 打印类型和对象的name属性:
# print 'type:', type(user)
# print 'name:', user.name
# user_add = User(id='6', name='lilix11')
# new_user = Book(id='5', name='lilix111', user_id='5')
# # 添加到session:
# session.add(user_add) #增加操作
# session.add(new_user)
# session.query(User).filter(User.id == 1).update({User.name: '李理想'})#修改操作
# session.query(User).filter(User.id == 6).delete() #删除操作
# print session.query(User).get(1).name#通过主键获取
# for user in session.query(User): # 遍历时查询
#     print user.name
# 提交即保存到数据库:
session.commit()
# 关闭Session:
session.close()