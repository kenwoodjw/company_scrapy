#coding:utf-8
import requests
def get_url():
    city_url = []
    with open('../测试.txt','r',encoding='GBK')as f_in:
        for line in f_in:
            short=line.split()
            city_name=short[2].lower()
            url='http://qy.58.com/%s_245/?PGTID=0d211266-0000-00b1-40b7-f2a14c69a2d3&ClickID=1'%(city_name)
            # if requests.get(url).status_code==200:
            city_url.append(url)
    return city_url
if __name__ == '__main__':
    print (get_url())