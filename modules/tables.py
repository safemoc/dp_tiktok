#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: tables.py
@Created: 2025/7/27 22:56

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import Column, Integer, String, Text, CheckConstraint
from utils import AuthCommitMixin
from base import Base


class OriginData(Base, AuthCommitMixin, object):
    __tablename__ = 'origin_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Integer)
    origin = Column(Text)
    page = Column(Text)
    record = Column(Integer, CheckConstraint('is_active in (0,1)'), nullable=False, default=0)


class VideoData(Base, AuthCommitMixin, object):
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


class CommentsData(Base, AuthCommitMixin, object):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(Integer)
    user_id = Column(Integer)
    content = Column(Text)
    timestamp = Column(Integer)


class UserData(Base, AuthCommitMixin, object):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiktok_user_id = Column(Text)
    account = Column(Text)
    followers = Column(Integer)
    following = Column(Integer)
    liked_num = Column(Integer)
    collect_num = Column(Integer)
    url = Column(String)
