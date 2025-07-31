import sys
import time

from DrissionPage import Chromium


class TikTok(object):

    def __init__(self):
        self.browser = Chromium().latest_tab

    def search(self, search_text: str):
        """
        抖音搜索
        :param search_text: 搜索文本
        :return:
        """
        self.browser.get(url='https://www.douyin.com/')
        time.sleep(.9)
        button = self.browser.ele('css:input[data-e2e="searchbar-input"][type="text"]')
        button.input(search_text)
        self.browser.ele('css:button[data-e2e="searchbar-button"][type="button"]').click()

    def listen_start(self, xhr: str):
        """
        启动监听器
        :param xhr: 监听路径
        :return:
        """
        self.browser.listen.start(xhr)

    def listen_wait(self):
        res = self.browser.listen.wait(count=1)
        if res:
            return res.response.body
        return

    def set_search_where(self, selector, where: {str: str}):
        """
         修改搜索条件
        :param selector: 【综合、视频、用户、直播】
        :param where: 筛选条件
        :return:
        """
        time.sleep(.9)
        items = {i.text: i for i in self.browser.eles('css:span[data-key]')}
        if selector not in items.keys():
            print(f"选项必须在 {items.keys()} ")
            sys.exit()
        items[selector].click()

        self.browser.ele('css:svg.arrow').hover()
        for k, v in where.items():
            _ = self.browser.ele(f'css:span[data-index1="{k}"][data-index2="{v}"]')
            if _:
                _.click()
            else:
                ...

        ...

class Transformart():
    def __init__(self):
        ...



if __name__ == '__main__':
    cls = TikTok()
    cls.search('乐陵影视城')
    cls.listen_start('/aweme/v1/web/search/item/')


    def tiktok_start():
        ...
        ll = {
            '0': '1',
            '1': '1',
            '2': '0',
            '3': '0',
        }
        time.sleep(.9)
        cls.set_search_where('视频', ll)
        data = cls.listen_wait()
        if data:
            return data
        else:
            return tiktok_start()


    data = tiktok_start()
    print(data)


