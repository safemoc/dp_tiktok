#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: base.py
@Created: 2025/7/27 22:58

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///mydata.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
