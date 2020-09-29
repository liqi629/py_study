#
#
# import urllib.request
# import re
# import os
#
# targetDir = r'E\img'
#
# def destFile(path):
#     if not os.path.isdir(targetDir):
#         os.mkdir(targetDir)
#
#     pos = path.rindex('/')
#
#     t = os.path.join(targetDir,path[pos+1:])
#
#
# if __name__ == '__main__':
#     weburl = ""
#
#     webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
#
#
#     req = urllib.request.Request(url=weburl, headers=webheader)
#
#     webpage = urllib.request.urlopen(req)
#     contentBytes = webpage.read()
#
#     for link in set(re.findall(r'((http|https):[^\s]*?(jpg|png|gif)', str(contentBytes))):
#         print(link)
#         try:
#             slink = link[0];
#             urllib.request.urlretrieve(slink, destFile(slink))
#
#         except:
#             print('失败')



"""请求网页"""
# import requests
# import re
# import time
# import os
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537'
# }
# response=requests.get('',headers=headers)
# #print(response.request.headers)
# #print(response.text)
# html=response.text
# """解析网页"""
# dir_name=re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]#文件
# if not os.path.exists(dir_name):#检查文件
#     os.mkdir(dir_name)
# urls=re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
# print(urls)
# """保存图片"""
# for url in urls:
#     time.sleep(1)
#     #图片的名字
#     file_name=url.split('/')[-1]
#     response = requests.get(url, headers=headers)
#     with open(dir_name+'/'+file_name,'wb') as f:
#         f.write(response.content)
import re
import requests


def download(html):
    # 通过正则匹配
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    for key in pic_url:
        print("开始下载图片：" + key + "\r\n")
        try:
            pic = requests.get(key, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        # 保存图片路径
        dir = '保存路径' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


def main():
    url = 'https://f.w24.rocks/viewthread.php?tid=357802'
    result = requests.get(url)
    download(result.text)


if __name__ == '__main__':
    main()