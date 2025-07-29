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
from sqlalchemy import Column, Integer, Text
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Task(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    over = Column(Integer)
    role_name = Column(Text)
