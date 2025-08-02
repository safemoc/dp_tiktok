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


# @scheduler('day', '11:55:59')
def tiktok(search_content, search_type, search_filter, listen_item='/aweme/v1/web/search/item/'):

    cls = Harvester(search_type, search_filter)
    print(f"========>搜索<========")
    cls.search(search_content)
    print(f"========>开始监听<========")
    cls.listen_start(listen_item)
    print(f"========>修改筛选<========")
    cls.set_search_where(search_filter)
    print(f"========>获取数据<========")
    data = cls.tiktok_video_data()
    print(f"========>矫正数据<========")
    trans = Transformation(data)
    print(f"========>保存数据<========")
    trans.save_data()
    print(f"========>获取评论<========")
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
