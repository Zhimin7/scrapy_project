# -*- coding: utf-8 -*-
# jsonpath
"""
Created on Mon Jun  7 21:01:46 2021

@author: 13084
"""

from urllib.parse import urlencode
import requests
# from pyquery import PyQuery as pq
import csv

base_url = 'https://danjuanapp.com/net-history/000828?'
headers = {
    'Host': 'danjuanapp.com',
    'Referer': 'https://danjuanapp.com/net-history/000828',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'X-Requested-With': 'fetch',
}


def get_page(page):
    params = {
        'size': '30',
        'page': page
    }
    url = base_url + urlencode(params)
    print(url)

    # print(url)
    # try:
    #     response = requests.get(url, headers=headers)
    #     if response.status_code == 200:
    #         print(response.status_code)
    #         print(response.json())
    #         return response.json()
    # except requests.ConnectionError as e:
    #     print('Error', e.args)


# def parse_page(json):
#     print(json)
#     if json:
#         items = json.get('data').get('items')
#         # print(items)
#         for item in items:
#             danjuan = {}
#             danjuan['date'] = pq(item.get('date')).text
#             danjuan['percentage'] = item.get('percentage')
#             danjuan['value'] = item.get('value')
#             yield danjuan


# 保存数据
# def saving_csv():
#     with open('data.csv', 'a', encoding='utf-8', newline='')as csvfile:
#         fieldnames = ['日期', '日涨幅', '净值']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({'日期': '10001', 'name': 'Mike', 'age': 20})


if __name__ == '__main__':
    # for page in range(1,11):
    json = get_page(1)
    # print(json)
# results=parse_page(json)
# for result in results:
#  print(result)
