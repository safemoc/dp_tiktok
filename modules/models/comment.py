#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: comment.py
@Created: 2025/7/28 00:17

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import Column, Integer, Text
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Comment(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(Integer)
    content = Column(Text)
    user_id = Column(Integer)
    liked = Column(Integer)
    fid = Column(Integer)
    timestamp = Column(Integer)