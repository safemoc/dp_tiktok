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
from automation.Tiktok import Harvester, Transformation


@scheduler('day', '23:58:59')
def tiktok(search_content, search_type, search_filter, listen_item='/aweme/v1/web/search/item/'):
    cls = Harvester(search_type, search_filter)
    cls.search(search_content)
    cls.listen_start(listen_item)
    cls.set_search_where(search_filter)
    trans = Transformation(cls.tiktok_video_data())
    trans.save_data()
    cls.recycle()


if __name__ == '__main__':
    tiktok('乐陵影视城', "综合", {
        '0': '1',
        '1': '1',
        '2': '0',
        '3': '0',
    })
    App().start()
    ...
