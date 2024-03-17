# 连接数据库


import pymysql

# # 打开数据库连接
DB = pymysql.connect(host='192.168.88.54',
                     user='root',
                     password='123456',
                     database='mydatabase',
                     port=3307)





# try:
#     with db.cursor() as cursor:
#
#         # 读取pdf中的文本文件
#         import pdfplumber
#
#         resp_dat = ""
#         path_url = r'E:\pandas_project\Iko.pdf'
#         with pdfplumber.open(path_url) as pdf:
#             page = pdf.pages[0]
#             resp_dat = page.extract_text()
#
#         print(resp_dat)
#         # 编写SQL插入语句
#         sql = f"INSERT INTO sql_review (name,age,email,start_update) VALUES ('王五',30,'{resp_dat}','2024-03-13')"
#
#         # 使用游标执行SQL语句
#         cursor.execute(sql)
#
#     # 提交更改
#     db.commit()
#
# finally:
#     # 关闭游标和数据库连接
#     db.close()















