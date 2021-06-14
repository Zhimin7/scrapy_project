import requests
import threading
import time
import json
import csv

'''
 https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_1623134492176&jsonp=jsonp&next=2&type=1&oid=54827518&mode=3&plat=1&_=1623135073490
 https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_1623134492179&jsonp=jsonp&next=3&type=1&oid=54827518&mode=3&plat=1&_=1623135337942
 https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_1623134492180&jsonp=jsonp&next=4&type=1&oid=54827518&mode=3&plat=1&_=1623135431187
 https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_1623134492181&jsonp=jsonp&next=5&type=1&oid=54827518&mode=3&plat=1&_=1623135479902
 https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_1623134492186&jsonp=jsonp&next=6&type=1&oid=54827518&mode=3&plat=1&_=1623136041672
'''


class MyThread(threading.Thread):
    def __init__(self, thread_name, target=None, args=None):
        super(MyThread, self).__init__(name=thread_name, target=target, args=args)
        self.thread_name = thread_name

    def run(self):
        super(MyThread, self).run()


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    "cookie": "fingerprint=53214c9ab90babaf15202ac04dac9b60; buvid_fp=C94A10D6-50A9-43CE-90DA-797A8E77A83713444infoc; buvid_fp_plain=8DE0DD30-8ED3-41AA-AFF1-7508AB939215184993infoc; _uuid=48242A1F-A4E3-1A50-F946-4D83139E56E120096infoc; buvid3=C94A10D6-50A9-43CE-90DA-797A8E77A83713444infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|k)~)RYRR0J'uYkJukulR|; PVID=1; fingerprint=72fdc61295457a587682e1a285256311; buvid_fp_plain=0CB5E2C5-4120-4C3E-A721-A8C2E79D76C4138381infoc; DedeUserID=401204029; DedeUserID__ckMd5=276536be2f632326; SESSDATA=43e69167%2C1638674059%2Ca94e4*61; bili_jct=aec8d393272d15fd931a3c82f5d0c7b7; bsource=search_bing; sid=jq6avai8; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
    'referer': 'https://www.bilibili.com/video/BV114411K7kt?p=2'
}
proxies = {
    'http': 'http://120.86.38.210:4245',
    'https': 'http://120.86.38.210:4245'
}

f = open('data.csv', 'a', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(f)
# csv_writer.writerow(['uname', 'sex', 'sign', 'message', 'time', 'like'])


def get_json(url):
    response = requests.get(url, headers=headers, proxies=proxies)
    text = response.text[42:-1]
    json_data = json.loads(text)
    # print(type(json_data))
    # print(json_data)
    return json_data


def get_data(datas):
    replies = datas['data']['replies']
    return replies


def save_data(replies):

    for reply in replies:
        message = reply.get('content').get('message')
        ctime = reply.get('ctime')
        content_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(ctime))
        like = reply.get('like')
        uname = reply.get('member').get('uname')
        sex = reply.get('member').get('sex')
        sign = reply.get('member').get('sign', '什么都没有写')
        csv_writer.writerow([uname, sex, sign, message, content_time, like])
        print(uname, sex, sign, message, content_time, like)


def main():
    for i in range(197, 1001):
        try:
            time_chick = int(time.time()*1000)
            url = f'https://api.bilibili.com/x/v2/reply/main?callback=jQuery172022958084184545902_{1623134492175+i}&jsonp=jsonp&next={i}&type=1&oid=54827518&mode=3&plat=1&_={time_chick}'
            json_data = get_json(url)
            replies = get_data(json_data)
            save_data(replies)
        except:
            continue
    print('保存完毕')


if __name__ == '__main__':
    main()