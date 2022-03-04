from PIL import Image
import os
import requests as rqs
from bs4 import BeautifulSoup as bsp

def get_input():
    ipt = input('Please input the keyword: ')
    ret = ''
    for i in ipt.strip().split():
        ret += i + '+'
def main():
  keyword=get_input()
  response=rqs.get(f'https://imgur.com/search?q={keyword}')
  html = bsp(response.text, 'html.parser')
  element = html.find_all(name='div', attrs={'class', 'cards'})[0]
  pictures = element.find_all(name='img')
  picture_urls = []
  for i in pictures:
      picture_urls.append(i.get('src')[14:])
  for i in picture_urls:
      res_pic = rqs.get(f'https://i.imgur.com/{i}', stream=True, timeout=5)
      image = Image.open(res_pic.raw)
      image.show()
      os.system('pause')


if __name__ == '__main__':
    main()