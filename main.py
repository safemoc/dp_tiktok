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
from scheduler import scheduler
from visualization.app import App
from modules.models.task import Task
from automation.harvester import TikTok,Transformation



@scheduler('day','11:33:00')
def hahahahha ():
    ...




if __name__ == '__main__':
    Task().all()
    cls = TikTok({
        '0': '1',
        '1': '1',
        '2': '0',
        '3': '0',
    })
    cls.search('乐陵影视城')
    cls.listen_start('/aweme/v1/web/search/item/')
    cls.tiktok_start()
    trans = Transformation(cls.tiktok_start())
    trans.save_data()
    App().start()
    ...
