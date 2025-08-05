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
import time

"""
scheduler 是 调度爬虫定时爬取的工作模块，目前建设想法是每天0. 01分开始执行任务。励志打造成像FastAPI一样的调度能力
"""
import datetime
import threading
from dateutil.relativedelta import relativedelta
from modules.models.task import Task


def scheduler(cycle, exec_time):
    """
    调度器定时启动函数可自动执行
    :param cycle: 频率：【day、week、month、year】
    :param exec_time: 时间：【HH:MM:ss】
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
        def wrapper(*args, **kwargs):
            def task_loop():
                h, m, s = map(int, exec_time.split(":"))
                next_time = datetime.datetime.now().replace(hour=h, minute=m, second=s, microsecond=0)
                while True:
                    now = datetime.datetime.now()
                    if next_time<now:
                        next_time = __cycle[cycle](next_time)
                        next_time = next_time.replace(hour=h, minute=m, second=s, microsecond=0)
                    sleep_seconds = (next_time - now).total_seconds()
                    if sleep_seconds >= 2:
                        print(f"等待 {sleep_seconds:.2f} 秒，直到 {next_time} 执行任务")
                        time.sleep(sleep_seconds)
                    _ = Task.create(role_name=func.__name__, over=0)
                    func(*args, **kwargs)
                    _.over = 1
                    _.save()
            threading.Thread(target=task_loop, daemon=True).start()
        return wrapper
    return decorator
