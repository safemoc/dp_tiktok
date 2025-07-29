#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: utils.py
@Created: 2025/7/27 22:57

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
from modules.base import Session
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime
session = Session()

class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class CRUDMixin(object):
    def save(self):
        session.add(self)
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        return obj.save()

    @classmethod
    def get(cls, pk):
        return cls.query.get(pk)

    @classmethod
    def filter(cls, *args, **kwargs):
        return cls.query.filter(*args, **kwargs)

    @classmethod
    def all(cls):
        return cls.query.all()
