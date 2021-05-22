import requests
from lxml import etree
import openpyxl

def get_data():
    # 设置cookies
    cookies = {
        'Cookie': 'bid=2OI7-SlmbK0; douban-fav-remind=1; __gads=ID=04399e232ec2b360-228b299cdec70045:T=1620352781:RT=1620352781:S=ALNI_MbrjqFfl-umLhDH_zfJ4vGJ0hYKEw; ll="118281"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1621604136%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; __utmz=30149280.1621604137.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=30149280; __utma=30149280.720624164.1620352783.1620352783.1621604137.2; __utmz=223695111.1621604137.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utma=223695111.1179981690.1621604137.1621604137.1621604137.1; __yadk_uid=EezUQnLRghR77Wyw8nEn5MTqokGG8tdS; _vwo_uuid_v2=DC73840BA3A6A557B4F4A7C96CEC3E876|5d339758288880329f5adf54997b7b82; dbcl2="238480159:SPia6nrVCuY"; ck=86RY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23848; _pk_id.100001.4cf6=a8cab06f3f4f852a.1621604136.1.1621606078.1621604136.',

    }
    # 设置请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }

    count = 0 # 记录页码
    for page in range(25):
        try:

            url = 'https://movie.douban.com/subject/32493124/comments'

            params = {
                'start': str(page * 20),
                'limit': '20',
                'sort': 'new_score',
                'status': 'P'
            }
            response = requests.get(url, headers=headers, cookies=cookies, params=params)
            html = etree.HTML(response.content.decode('utf-8'))
            comment_items = html.xpath('//div[@class="comment-item "]')
            for comment_item in comment_items:
                # 用户名
                username = comment_item.xpath('.//span[@class="comment-info"]/a/text()')[0]
                # 评论时间
                times = comment_item.xpath('.//span[@class="comment-time "]/@title')[0]
                # 推荐值
                rating = comment_item.xpath('.//span[2]/@title')[0]
                # 评论
                comments = comment_item.xpath('.//span[@class="short"]/text()')[0]
                sheeet.append([username, times, rating, comments])
                print(username + '===' + times + '===' + rating + '===' + comments)
                wb.save('悬崖之上短评.xlsx')
            count += 1
            print('正在保存第{}页数据'.format(count))

        except Exception as e:
            continue


def main():
    get_data()


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheeet = wb.active
    sheeet.title = '悬崖之上短评'
    sheeet['A1'] = '用户名称'
    sheeet['B1'] = '评论时间'
    sheeet['C1'] = '推荐值'
    sheeet['D1'] = '评论'


    main()
