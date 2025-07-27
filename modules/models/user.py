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
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiktok_user_id = Column(Text)
    account = Column(Text)
    followers = Column(Integer)
    following = Column(Integer)
    liked_num = Column(Integer)
    collect_num = Column(Integer)
    url = Column(String)
