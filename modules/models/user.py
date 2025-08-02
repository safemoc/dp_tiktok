#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: user.py
@Created: 2025/7/27 23:57

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import Column, Integer, Text, String
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class User(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer,unique=True,comment="用户id")
    account = Column(String(255), comment='账号')
    sec_uid = Column(Text,unique=True)
    self_url = Column(String(500), comment='个人主页链接')
    followers = Column(Integer, comment='粉丝数')
    following = Column(Integer, comment='关注数')
    name = Column(String(300), comment='用户名')
    avatar = Column(Text,comment="头像")
