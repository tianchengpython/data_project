import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
html = requests.get("https://www.dushu.com/showbook/135618/1934064.html",headers=headers)

print(html.text)

selector = etree.HTML(html.text)

# data = selector.xpath("//head/title/text()")
# print(data)


