from DrissionPage import Chromium


class TikTok(object):
    def __init__(self):
        self.browser = Chromium().latest_tab


    def search(self, search_text: str):
        self.browser.get(url='https://www.douyin.com/')
        button = self.browser.ele('css:input[placeholder="搜索你感兴趣的内容"]')
        button.input(search_text)

        self.browser.ele('css:button[data-e2e="searchbar-button"][type="button"]').click()

    def listen_pipeline(self, xhr: str = "XHR"):
        self.browser.listen.start(xhr)

    def set_search_where(self,selector,where):
        items = {i.text:i for i in self.browser.eles('css:span[data-key]')}
        if selector not in items.keys():
            raise f"选项必须在 {items.keys()} "
        items[selector].click()

        # shaixuan 鼠标悬停 后选择 相关的标签。
        # 开启 监听 分析数据包 然后将数据包相关数据 存储在 mydata.db 中


        ...



if __name__ == '__main__':
    cls = TikTok()
    # cls.listen_pipeline('/aweme/v1/web/search/item/')
    # cls.search('乐陵影视城')
    cls.set_search_where(None,None)