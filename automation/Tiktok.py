import time

from DrissionPage import Chromium

from modules.models.video import Video
from modules.models.user import User
from modules.models.comment import Comment


class Harvester(object):

    def __init__(self, selector, _filter):
        """

        :param selector:
        :param _filter:
        """
        self.selector = selector
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
        """

        :return:
        """
        res = self.browser.listen.wait()
        if res:
            return res.response.body
        return None

    def set_search_where(self, _filter):
        """
         修改搜索条件
        :return:
        """
        time.sleep(.9)
        items = {i.text: i for i in self.browser.eles('css:span[data-key]')}
        if self.selector not in items.keys():
            print(f"选项必须在 {items.keys()} ")
            raise TypeError
        items[self.selector].click()

        self.browser.ele('css:svg.arrow').hover()
        for k, v in _filter.items():
            _ = self.browser.ele(f'css:span[data-index1="{k}"][data-index2="{v}"]')
            if _:
                _.click()

    def tiktok_video_data(self):
        data = self.listen_wait()
        if data:
            return data
        else:
            print("下钻+1")
            return self.tiktok_video_data()

    def recycle(self):
        videos = Video().filter(Video.comment_consumption == 0).all()
        print(videos)

        for video in videos:
            self.listen_start('/aweme/v1/web/comment/list/?device_platform=webapp')
            self.browser.get(video.link)
            login_iframe = self.browser.ele('css:rect[width="36"][height="36"][fill="url(#pattern0_3645_22461)"]')
            if login_iframe:
                login_iframe.click()

            for packet in self.browser.listen.steps():
                try:
                    for i in packet.response.body["comments"]:
                        exists = User.filter(User.user_id == i["user"]["uid"]).first()
                        if not exists:
                            user = i["user"]
                            user_info = {
                                "user_id": user["uid"],
                                "account": user["unique_id"],
                                "sec_uid": user["sec_uid"],
                                "self_url": f"https://www.douyin.com/user/{user["sec_uid"]}",
                                "followers": "",
                                "following": "",
                                "name": user["nickname"],
                                "avatar": user["avatar_thumb"]["url_list"][0],
                            }
                            User(**user_info).save()
                        exists = Comment.filter(Comment.cid == i['cid']).first()
                        if not exists:
                            item = {
                                "cid": i['cid'],
                                "video_id": i["aweme_id"],
                                "content": i["text"],
                                "user_id": i["user"]["uid"],
                                "liked": i["digg_count"],
                                "fid": None,
                                "timestamp": i["create_time"]
                            }
                            Comment(**item).save()
                    print(packet.response.body)
                    if packet.response.body["has_more"] == 0:
                        break
                    else:
                        self.browser.actions.move_to((300, 300), offset_x=0, offset_y=0)
                        self.browser.actions.scroll(delta_y=600)
                except Exception as e:
                    print(e)
                    print(packet.response.body)
                    break
                video.comment_consumption = 1
                print(video.link)
                video.save()

        ...


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
                        'sec_uid': i['author']['sec_uid'],
                        'self_url': f"https://www.douyin.com/user/{i['author']['sec_uid']}"
                        }
                User(**user).save()

            ...


if __name__ == '__main__':
    cls = Harvester("综合", {
        '0': '1',
        '1': '1',
        '2': '0',
        '3': '0',
    })
    cls.recycle()

    ...
