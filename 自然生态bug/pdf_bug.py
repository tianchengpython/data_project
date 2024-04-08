import requests
from urllib.parse import unquote

url_path ="https://momot.rs/d3/y/1712133998/149/v/duxiu_files/20240312/annas_archive_data__aacid__duxiu_files__20240312T060940Z--20240312T060941Z/aacid__duxiu_files__20240312T060940Z__LfjrAZ9NGUqQ6BAcvhMVVE~/GFYNfSdYV_5O3tSNUIv5GA/%E5%9B%AD%E6%9E%97%E5%B7%A5%E7%A8%8B%E4%BB%8E%E6%96%B0%E6%89%8B%E5%88%B0%E9%AB%98%E6%89%8B%E7%B3%BB%E5%88%97%20%20%E5%9B%AD%E6%9E%97%E5%9F%BA%E7%A1%80%E5%B7%A5%E7%A8%8B%20--%20%E9%99%88%E8%89%B3%E4%B8%BD%E4%B8%BB%E7%BC%96%20--%202015%20--%20%E5%8C%97%E4%BA%AC%EF%BC%9A%E6%9C%BA%E6%A2%B0%E5%B7%A5%E4%B8%9A%E5%87%BA%E7%89%88%E7%A4%BE%20--%209787111505365%20--%20973415a8bd979cf5e31b6585be7b0cef%20--%20Anna%E2%80%99s%20Archive.pdf"

# 解码URL
decoded_url = unquote(url_path)

print("解码后的URL:", decoded_url)


# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Connection": "keep-alive",
#     "Referer": "https://annas-archive.org/",
#     "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"Windows\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
# }
#
# resp = requests.get(decoded_url,headers)
# print(resp)


