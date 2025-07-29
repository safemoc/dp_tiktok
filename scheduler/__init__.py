#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: __init__.py.py
@Created: 2025/7/27 22:47

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
"""
scheduler 是 调度爬虫定时爬取的工作模块，目前建设想法是每天0. 01分开始执行任务。励志打造成像FastAPI一样的调度能力
"""
import datetime
import threading
from dateutil.relativedelta import relativedelta
from modules.models.task import Task


def scheduler(cycle, time):
    """
    调度器定时启动函数可自动执行
    :param cycle: 频率：【day、week、month、year】
    :param time: 时间：【HH:MM:ss】
    :return:
    """
    __cycle = {
        "day": lambda now: now + datetime.timedelta(days=1),
        "week": lambda now: now + datetime.timedelta(weeks=1),
        "month": lambda now: now + relativedelta(months=1),
        "year": lambda now: now + relativedelta(years=1)
    }

    if cycle not in __cycle.keys():
        print(f"@cycle 必须位于 {__cycle.keys()} 中；实际参数值为：{cycle}")
        raise TypeError

    def decorator(func):
        print(func.__name__)
        def wrapper(*args, **kwargs):
            def task_loop():
                implement = False
                while True:
                    # implement 不应该是直接确定的，而是要存储到数据库
                    if implement:
                        now = datetime.datetime.now()
                        next_time = __cycle[cycle](now)
                        h, m, s = map(int, time.split(":"))
                        next_time = next_time.replace(hour=h, minute=m, second=s, microsecond=0)
                        print(next_time)
                        sleep_seconds = (next_time - now).total_seconds()
                        print(f"等待 {sleep_seconds:.2f} 秒，直到 {next_time} 执行任务")
                        time.sleep(max(0, sleep_seconds))
                        func(*args, **kwargs)
                    else:
                        func(*args, **kwargs)
                        implement = True

            threading.Thread(target=task_loop, daemon=True).start()

        return wrapper

    return decorator
