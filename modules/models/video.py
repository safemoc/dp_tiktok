#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: video.py
@Created: 2025/7/28 00:11

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import Column, Integer, Text, String
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Video(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'video_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiktok_video_id = Column(Text)
    duration = Column(Integer)
    link = Column(Text)
    from_page = Column(Integer)
    user_id = Column(Text)
    like_nums = Column(Integer)
    discuss_nums = Column(Integer)
    collect_nums = Column(Integer)
    forward_nums = Column(Integer)
