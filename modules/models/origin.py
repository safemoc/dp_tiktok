#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: origin.py
@Created: 2025/7/28 00:19

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import Column, Integer, Text, CheckConstraint
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Origin(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'origin_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Integer)
    origin = Column(Text)
    page = Column(Text)
    record = Column(Integer, CheckConstraint('record in (0,1)'), nullable=False, default=0)
