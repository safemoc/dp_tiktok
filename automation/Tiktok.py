import time

from DrissionPage import Chromium

from modules.models.video import Video
from modules.models.user import User


class Harvester(object):

    def __init__(self, _filter):
        self.filter = _filter
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
        login_iframe = self.browser.ele('css:rect[width="36"][height="36"][fill="url(#pattern0_3645_22461)"]')
        if login_iframe:
            login_iframe.click()
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
        return None

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
            raise TypeError
        items[selector].click()

        self.browser.ele('css:svg.arrow').hover()
        for k, v in where.items():
            _ = self.browser.ele(f'css:span[data-index1="{k}"][data-index2="{v}"]')
            if _:
                _.click()

    def tiktok_start(self):
        time.sleep(.9)
        self.set_search_where('视频', self.filter)
        data = self.listen_wait()
        if data:
            return data
        else:
            return self.tiktok_start()


class Transformation(object):
    def __init__(self, data):
        self.data = data['data']
        ...

    def save_data(self):
        for i in self.data:
            i = i['aweme_info']
            video_id = i['aweme_id']
            if not Video.filter(Video.video_id == video_id).first():
                video = {"video_id": video_id,
                         "user_id": i["author"]["uid"],
                         "post_time": i["create_time"],
                         "docs": i["desc"],
                         "link": f"https://www.douyin.com/video/{video_id}",
                         "like_count": i["statistics"]["digg_count"],
                         "collect_count": i["statistics"]["collect_count"],
                         "share_count": i["statistics"]["share_count"],
                         "comment_count": i["statistics"]["comment_count"],
                         "download_count": i["statistics"]["download_count"]}
                Video(**video).save()
            user_id = i['author']['uid']
            if not User.filter(User.user_id == user_id).first():
                user = {'user_id': user_id,
                        "name": i['author']['nickname'],
                        'followers': i['author']['follower_count'],
                        'avatar': i['author']['avatar_thumb']['url_list'][0],
                        'self_url': f"https://www.douyin.com/user/{i['author']['sec_uid']}"
                        }
                User(**user).save()

            ...


if __name__ == '__main__':
    ...
