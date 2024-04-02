import requests
import time
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

# 创建一个工作簿
workbook = Workbook()
# 获取当前活动的工作表
sheet = workbook.active
headers = ""
data_list = []
#爬取数据：
for i in range(1,3):
    time.sleep(1)
    url_path = f"https://nature.hxsjcbs.com/index.php?s=/nature/index/get_detail/sid/{i}"
    resp = requests.get(url_path)
    resp_data = resp.json()
    if resp_data['code'] == 200:
        print(f">>>>>>正在爬取第{i}条数据")
        data = resp_data['data']

        title = data['category_chain'][2]['title']
        # print(">>>动物门科：", title)

        territory = data['category_chain'][3]['title']
        # print(">>>所属纲：", territory)

        name = data['name']['cn']
        # print(">>>动物名称：", name)

        lt = data['name']['lt']
        # print(">>>动物英文名称：", lt)

        protection = data['protection']['npl']
        # print(">>>保护级别：", protection)

        habit = data['habit']
        # print(">>>习性与生境：", habit)

        distribution = data['distribution']
        # print(">>>分布：", distribution)

        distinguish = data['distinguish']
        # print(">>>形态特征：", distinguish)

        # 图片地址：
        img_addr_list = data['pictures']
        # 图面名称：
        img_name_list = [f"动物图片{j}" for j in range(1,len(img_addr_list)+1)]
        headers = ['动物门科', '动物所属', '动物名称', '英文名称', '保护级别', '习性与生境', '地理分布', '形态特征']
        headers += img_name_list

        # 数据
        data_list.append((title, territory, name, lt, protection, habit, distribution, distinguish))
        # 下载好的图片：
        row_num = 1
        for i_img, img_data in enumerate(img_addr_list):
            response = requests.get(img_data['img'])
            if response.status_code == 200:
                # 获取图片的字节流
                image_bytes = BytesIO(response.content)
                img = Image(image_bytes)
                img.width = 70
                img.height = 70
                col_num = i + 1
                sheet.add_image(img, f'{chr(65 + row_num)}{col_num}')
            else:
                print(f"爬取图片 {img_data['img']} 失败！")

    else:
        print(">>>>>>爬取数据失败！")

# 写入标题到工作表
sheet.append(headers)
# print(data_list)
# 写入数据到工作表
for row in data_list:
    sheet.append(row)
# 保存工作簿到文件
workbook.save(filename='students.xlsx')