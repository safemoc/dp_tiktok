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
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(base_dir, 'mydata.db')

engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = scoped_session(sessionmaker(bind=engine, autoflush=False, expire_on_commit=False))

Base = declarative_base()
Base.query = Session.query_property()
