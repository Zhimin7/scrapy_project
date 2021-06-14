import requests
import os
import pprint


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'cookie': 'BIDUPSID=AED6C3CABA8CAB4E63221A8089620702; PSTM=1622806242; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_5a29a765cfc55b46909e578be8a2c08b1623056066924; BAIDUID=98B7147477CEB2687A42DDB93D590B11:FG=1; BAIDUID_BFESS=98B7147477CEB2687A42DDB93D590B11:FG=1; __yjs_st=2_ZDM3NThiOTg1MDcxYzgxOTExMjM4N2YyOTAyYzMyNDM4NDIwNWY0YjBlNzlmYzY2NGVkOGMzOWMwNzcwYjAwOTcwYzQ3MmRmNzE4MGFkY2RkYTA0MDExMTU3OWFmNzYxNDI2NzFhNGEzNjc1ZjQ4NmE3NjQyNGFlMzBjMjllMjBmMTk0MjE0YzUwMjcwZTg2YTk0ZWUwMzVjOTJhZmJiMGY4OTBmYThlMGI0MTcwMTMwYTVlMTQ0OThkNjM3MTRkZTVhYmE3ZDhhMjQxNzYxODE1Yzc2MmQxN2UzYmVlYjhmYjhkMzZmYjI3ZmVmMjllMDEzOTE4ODViMWRjNzMzNV83XzE3YTRhNjdj; jsdk-uuid=9558c7ab-673f-4c62-9eb0-c638717d7bd6; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1623116127; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1623116422; ab_sr=1.0.1_ZTIwZDVhMWI1Nzk3Y2M0NmQ5OTBjZjE0MmYyNzVhZjgyYzQ0NjdhZDliZjYwNTFjZDU3MDA0MWRiZGVjYjkwOTRlYjY3YmViZDUzMTg1OThkY2YzNWQ2YjkwZGVmNDQwY2IyMzdiYmIxMWI5ZTdjOGQ2ZThhNzgzYjhlMzA2ZDEyNjBmNTMwYTI0ZTU0ZTcyNTQ5MjFlZTBkNTg3NWEzMQ==; reptileData=%7B%22data%22%3A%22b93407142ef6dc78243e5058f9bfa4b095534ec10752b67ad9cba41ca5215ea69d802971d506114316438ff6ba86b3b5c2a3cdc61439a9b72cc6b8d2e9984947b3b9c93f87aaaf3b854735ff69584f65dff136d6eaa0573f0c32b38b959f73099e9d264aef6479009b449efc50df023f0db5a562265a1f2d2f2892ad75c472fc%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%223f90e0fa%22%7D',
    'referer': 'https://haokan.baidu.com/tab/yule_new'
}


def get_json(url):
    response = requests.get(url, headers=headers)
    data_json = response.json()
    return data_json


def get_data(json_data):
    videos = json_data['data']['response']['videos']
    return videos


def save_data(videos):
    for video in videos:
        video_url = video.get('play_url')
        video_name = video.get('title')
        data = requests.get(video_url).content
        with open(f'./videos/{video_name}.mp4', 'wb') as f:
            f.write(data)
        print(video)
        print(video.get('play_url'))


def main():
    url = 'https://haokan.baidu.com/web/video/feed?tab=yule_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1623116421264'
    json_data = get_json(url)
    videos = get_data(json_data)
    save_data(videos)
    print('下载完毕')


if __name__ == '__main__':
    main()