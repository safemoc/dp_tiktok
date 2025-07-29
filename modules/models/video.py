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
from sqlalchemy import Column, Integer, Text
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Video(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(Text,comment='平台视频唯一id')
    user_id = Column(Integer,comment= '用户id')
    link = Column(Text,comment='视频链接')
    like_nums = Column(Integer,comment= '点赞数')
    collect_num= Column(Integer,comment = '收藏数')
    repost_num = Column(Integer,comment = '转发数')
    comment_num = Column(Integer,comment='评论数')
    # discuss_nums = Column(Integer)
    # collect_nums = Column(Integer)
    # forward_nums = Column(Integer)
