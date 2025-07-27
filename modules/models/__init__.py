#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: __init__.py.py
@Created: 2025/7/27 23:57

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from modules.base import Base, engine

from .video import Video
from .origin import Origin
from .user import User
from .comment import Comment

Base.metadata.create_all(engine)
