import requests

import os
class Mzitu():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }# 构造请求头，主网站的请求头较为简单只需构造浏览器头
        self.base_path = os.getcwd() # 获取当前路径

    def get_url(self,html):
    # '''获取每个套图的链接，并返回'''
        html_b=BeautifulSoup(html,'lxml')
        urls_b = html_b.find_all('ul',attrs={'id':'pins'})[0]
        urls = urls_b.find_all('a')
        for i in urls:
            yield i['href']

    def get_img_url_max(self,url):
    # '''获取图片的张数'''
        html_i = requests.get(url,headers=self.headers).text
        html_b = BeautifulSoup(html_i,'lxml')
        max_number=html_b.find_all('div',attrs={'class':'pagenavi'})[0]
        max_number = max_number.find_all('a')[-2].span.text
        return max_number

    def get_img_url(self,url):
    # '''获取每张图片的链接'''
        html_i = requests.get(url, headers=self.headers).text
        html_b = BeautifulSoup(html_i, 'lxml')
        img_url = html_b.find_all('div',attrs={'class':'main-image'})[0].p.a.img['src']
        return img_url

    def download_img(self,name,url):
    # '''获取每张图片的内容'''
        headers = {
            'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Host': 'i.meizitu.net',
            'Referer': 'http://www.mzitu.com/%s'%name,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        img = requests.get(url,headers=headers).content
        return img

    def get_img(self,name,max,img_url):
    # '''下载图片'''
        path = os.path.join(self.base_path,name)
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
        for i in range(1,int(max)):
            k = str(i)
            file_name = k+'.jpg'
            img_file_name = os.path.join(path,file_name)
            if len(k) <2:
                img_url = img_url[:-5]+k+img_url[-4:]
            else:
                img_url = img_url[:-6]+k+img_url[-4:]
            img = self.download_img(name,img_url)
            with open(img_file_name,'wb') as f:
                f.write(img)

    def get_html_url_link_max(self):
    # '''获取主网站中的总页数'''
        url = 'http://www.mzitu.com/'
        html = requests.get(url,headers = self.headers).text
        html_b = BeautifulSoup(html,'lxml')
        max_number = html_b.find_all('a',attrs={'class':'page-numbers'})[-2]['href']
        max_number = max_number.split('/')[4]
        return max_number

    def main(self):
        max_number = int(self.get_html_url_link_max())
        for i in range(1,max_number+1):
        # '''遍历构造网址'''
            url = 'http://www.mzitu.com/page/%d/'%i
            html = requests.get(url,headers=self.headers).text
            urls = self.get_url(html)
            for i in urls:
                name = i.split('/')[-1]
                max_number = self.get_img_url_max(i)
                img_url = self.get_img_url(i)
                self.get_img(name,max_number,img_url)

if __name__ == '__main__':
    mzitu = Mzitu()
    mzitu.main()