#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: main.py
@Created: 2025/7/27 23:18

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""

from modules.models import User

if __name__ == '__main__':
    user = User.create(tiktok_user_id='123abc',
                           account='demo_user',
                           followers=1000,
                           url='https://example.com')

    all_users = User.all()

    ...
