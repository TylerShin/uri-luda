# coding: utf-8
import sys
from bs4 import BeautifulSoup
import requests
import hashlib

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

def save_image(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    article_content = soup.find('div', id='dgn_gallery_detail')
    imgs = article_content.find_all('img')
    filtered_imgs = list(map(lambda x: x.get('src'), filter(lambda x: x.get('onclick'), imgs)))[1:] # 첫번째꺼 이상한거라 제외

    for link in filtered_imgs:
        filename = hashlib.sha3_224(str(link).encode('utf-8')).hexdigest()[:6] + '.png'
        print('[!]  Downloading... - {0}'.format(link))
        fp = open(filename, 'wb')
        data = requests.get(link)
        fp.write(data.content)
        fp.close()
        print('[+] {0} Saved!'.format(filename))


# save_image('http://gall.dcinside.com/mgallery/board/view/?id=luda&no=19865&page=1&exception_mode=recommend')

if __name__=='__main__':
    if len(sys.argv) > 1:
        print('[!] Run with URL({0})\n'.format(sys.argv[1]))
        save_image(sys.argv[1])
    else:
        print('[-] Run with URL argument')
        print('  e.g.) python luda-crawl-practice.py "http://gall.dcinside.com/mgallery/board/view/?id=luda&no=19865&page=1&exception_mode=recommend"')
        
