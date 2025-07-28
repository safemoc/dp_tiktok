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
from automation.harvester import Spider

if __name__ == '__main__':
    s = Spider()
    s.open_browser('%E4%B9%90%E9%99%B5%E5%BD%B1%E8%A7%86%E5%9F%8E')
    s.filtration()
    s.turn_page()
    s.downloader_item()
    ...
