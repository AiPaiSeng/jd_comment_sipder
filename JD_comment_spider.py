'''
作者：艾派森
csdn主页：https://blog.csdn.net/m0_64336780
时间：2023/7/28
'''

# 导包
import requests
import time
import random

# 获取评论
def get_content(page):
    # 目标网址
    url = 'https://club.jd.com/comment/productPageComments.action'
    # 参数
    params = {
        'productId': product_id,
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': 10,
        'isShadowSku': 0,
        'fold': 1
    }
    # 请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.35 Safari/537.36',
        'cookie':'__jdu=16589701614111380507873; shshshfpa=4daabca1-903d-22ab-baf8-97de678e14b1-1665804114; shshshfpb=opwrgFhIfEq3uLkjOVzijtQ; areaId=27; unpl=JF8EALRnNSttWB9SBBsHGEZCSg0HW1wIH0cDZjVQU19cT1FQSAMdRhl7XlVdXhRLFx9uYBRXXlNJVA4ZBysSEXtdVV9fD0oeBm5vNWRcNks6cmQDZnBMSlxRNiE4SBczblcFU1lRQ1IEGwUbFxBLXVZXXAxKEQppZTVVbVhDUDUrMh4SEUpcXFlcD0onAl9lBFVYXEpTBBgFK1l-ShBUWVkBQxECb2AFUV1YS1YMGgYaFBlNX2RfbQs; __jdv=76161171|www.baidu.com|t_1003608409_|tuiguang|1e70142ec0ab401ea18cd63554db07e8|1667745095451; __jda=122270672.16589701614111380507873.1658970161.1667719720.1667745095.7; __jdc=122270672; jsavif=1; shshshfp=1075b1ee284c481ea605141bda519a56; token=99f32c7dafc446558ee3457c800615ba,2,926525; __tk=jpIxjze0JsA1jsBilUq1lcfTkUaxjDtxkcfTjDIxJijwkctwjphoJn,2,926525; ip_cityCode=2376; ipLoc-djd=27-2376-50232-53749; 3AB9D23F7A4B3C9B=EQ27JR2QLTE5R4TJCP4OICTNOVNYQZRPPKFT66XF32BQ3MXX2DSVKPDCEHSB2RQDRMGCGNPGC42YI7WAEXO6XEQ3HI; JSESSIONID=229855194FEAF8A1A0898F4D875A5667.s1; jwotest_product=99; shshshsID=c9d69e6764a3fcbe122cc5d8922262aa_4_1667745624837; __jdb=122270672.4.16589701614111380507873|7.1667745095',
        'referer': 'https://item.jd.com/'
    }
    # 发生请求并获取json数据
    resp = requests.get(url,params=params,headers=headers).json()
    # 获取评论内容并保存
    for comment in resp['comments']:
        # 将评论内容里的换行符剔除
        content = comment['content'].replace('\n','')
        print(content)
        f.flush()
        f.write(content)
        f.write('\n')
    print(f'============================第{page+1}页爬取完毕===============================')

if __name__ == '__main__':
    product_id = input('请输入商品的ID：')
    page_number = int(input('请输入要爬取的页数：'))
    with open(f'JD_comment_{product_id}.txt','a',encoding='utf-8')as f:
        for page in range(page_number):
            try:
                get_content(page)
                time.sleep(5+random.random())
            except:
                break
    print(f'爬虫程序已结束！评论内容请在同目录下的 JD_comment_{product_id}.txt 查看！')
