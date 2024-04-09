import requests
# from lxml import etree
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
# html = requests.get("https://www.dushu.com/showbook/135618/1934064.html",headers=headers)
#
# print(html.text)
#
# selector = etree.HTML(html.text)

# data = selector.xpath("//head/title/text()")
# print(data)



# 使用爬虫收集网上与书本相关数据：

url = "https://wenku.baidu.com/ndPureView/view/ccb5742d89d63186bceb19e8b8f67c1cfbd6ee08?apiVersion=v2021&isPure=1&noWaterMark=1&source=1&scrollLoadPagesNum=20&apiUrl=https://easylearn.baidu.com/edu-web-go/content/docreader?clientType%3D1%26pageType%3D1&retypeGetRequestUrl=https://easylearn.baidu.com/edu-web-go/content/longdocreader?pageType%3D1"

resp = requests.get(url)

print(resp.text)




