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
from sqlalchemy import Column, Integer, Text, CheckConstraint
from modules.base import Base
from modules.mixins import TimestampMixin, CRUDMixin


class Video(Base, TimestampMixin, CRUDMixin):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(Text, comment='平台视频id', unique=True)
    user_id = Column(Integer, comment='用户id')
    link = Column(Text, comment='视频链接')
    like_count = Column(Integer, comment='点赞数')
    download_count = Column(Integer, comment='下载数')
    share_count = Column(Integer, comment='转发数')
    collect_count = Column(Integer, comment='收藏数')
    comment_count = Column(Integer, comment='评论数')
    post_time = Column(Integer, comment="发布时间")
    docs = Column(Text, comment="文案")
    comment_consumption = Column(Integer, comment='是否已收集评论')
    __table_args__ = (CheckConstraint('comment_consumption IN (0, 1)', name='check_comment_consumption_0_or_1'),)
