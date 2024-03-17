
# 整理数据试图：
import re
import json
from utils import DataTiramisu


class DataView(DataTiramisu):


    # def __init__(self):
    #     self.min_keyword_count = 5
    #     self.max_keyword_count = 15


    # 提取pdf中的数据：
    def get_pdf_data(self):
        read_file_pdf = input("》》》》》》请输入读取文件路径：")
        new_pdf_file_path = input("》》》》》》请输入读新创建pdf路径，单个pdf才使用到：")
        save_img_path = input("》》》》》》请输入存放要提取数据图片：")
        save_txt_path = input("》》》》》》请输入存放提取后的文本存放地址：")
        start_num = input("》》》》》》请输入单个pdf使用，开始索引：")
        end_num = input("》》》》》》请输入单个pdf使用，结束索引：")
        if_all = input("》》》》》》请输入True读取文件夹中所有数据，False读取单个：")

        # "../data_files/pdf/"
        # "../static/"
        # "../txts/save_pdf_txt/"

        data_dict = {
            "read_file_pdf": read_file_pdf,          # 读取文件路径
            "new_pdf_file_path": new_pdf_file_path,  # 读取单个pdf才使用到
            "save_img_path": save_img_path,          # 存放要提取数据图片
            "save_txt_path": save_txt_path,          # 存放提取后的文本存放地址
            "start_num": start_num,                  # 单个pdf使用：开始
            "end_num": end_num,                      # 单个pdf使用：结束
            "if_all": if_all                         # True读取文件夹中所有数据，False读取单个
        }
        self.post_pdf_txt(data_dict)


    # 提取world中的数据：
    def get_world_data(self):

        read_file_word = input("》》》》》》请输入读取文件路径：")
        save_file_word = input("》》》》》》请输入存放word提取出来的数据：")
        start_num = input("》》》》》》请输入单个word使用,开始索引：")
        end_num = input("》》》》》》请输入单个word使用,结束索引：")
        if_all = input("》》》》》》请输入True读取文件夹中所有数据，False读取单个：")

        dat_dict = {
                "read_file_word": read_file_word,     #读取文件路径
                "save_file_word": save_file_word,     #存放word提取出来的数据
                "start_num": start_num,               #单个word使用：开始
                "end_num": end_num,                   #单个word使用：结束
                "if_all": if_all                      #True读取文件夹中所有数据，False读取单个
            }
        self.post_word_txt(dat_dict)


    def get_dat(self):
        input_txt_path = input("》》》》》》请输入读取文件路径：")
        input_data = input("》》》》》》请输入关键字：")
        #         进行读取文本中的数据;
        resp_txt = self.get_data_txt(input_txt_path).split("。")


        # 第二种解决办法
        # 思路：1.分割完后进行存入数据库
        # 2.将读出来的数据存入数据库，根据输入的关键字从数据库中模糊查询一下，查询相关语句
        # 3.转换为json数据格式的。





        joint_list = []


#                进行拼接数据：
#                 data_pal = {
#                     "instruction": input_data,
#                     "input": "",
#                     "output": i
#                 }
#                 joint_list.append(data_pal)


        # with open("../save_json/data_pal.json", "w",encoding="utf-8") as f:
        #     json.dump(joint_list, f, ensure_ascii=False, indent=4)


#



if __name__ == '__main__':
    dat = DataView()

    # 提取pdf中的数据：

    dat.get_pdf_data()


    # txt_path = "../txts/save_pdf_txt/pdf.txt"
    # dat.get_dat()



