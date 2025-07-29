#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File: harvester.py
@Created: 2025/7/28 23:49

@Author: safemoc
@Email: safemoc@gmail.com

@Description:
@Version: @1.0

@Statement: 本脚本仅供学习与研究使用，严禁用于商业用途（For educational and non-commercial use only）。
"""
import time
from lxml import etree
from DrissionPage import Chromium
from scheduler import scheduler





class Spider(object):
    def __init__(self,search):
        self.div_main = None
        self.browser = Chromium().latest_tab
        self.open_browser(search)
        self.filtration()
        self.turn_page()
        self.downloader_item()

    def open_browser(self,search=''):
        url = f'https://www.douyin.com/root/search/{search}?type=video'
        self.browser.get(url=url)

    def filtration(self):
        screen = self.browser.ele('css:.QfeM8ow3')
        screen.hover()
        self.browser.ele('css:span.eXMmo3JR[data-index1="0"][data-index2="1"]').click()
        self.browser.ele('css:span.eXMmo3JR[data-index1="1"][data-index2="1"]').click()

    def turn_page(self):
        for i in range(8):
            time.sleep(3)
            self.browser.actions.key_down('\ue00f')

    def downloader_item(self):
        item = etree.HTML(self.browser.html)
        element_div = item.xpath("//div[@id='root']")[0]
        self.div_main = etree.tostring(element_div,encoding='utf-8',pretty_print=True).decode('utf-8')








if __name__ == "__main__":


    @scheduler('day','00:00:00')
    def 抖音评论():
        Spider().start()













