
# 整理数据试图：
import os
import json
from utils import DataTiramisu
# from models.db_model import insert_data,select_data

class DataView(DataTiramisu):
    # 提取pdf中的数据：
    def get_pdf_data(self):
        read_file_pdf = input("》》》》》》请输入读取文件路径：").strip()
        new_pdf_file_path = input("》》》》》》请输入读新创建pdf路径，单个pdf才使用到：")
        save_img_path = input("》》》》》》请输入存放要提取数据图片：")
        save_txt_path = input("》》》》》》请输入存放提取后的文本存放地址：")
        start_num = input("》》》》》》请输入单个pdf使用，开始索引：")
        end_num = input("》》》》》》请输入单个pdf使用，结束索引：")
        if_all = input("》》》》》》请输入True读取文件夹中所有数据,False读取单个：")

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
        if_all = input("》》》》》》请输入True读取文件夹中所有数据，False读取单个：")

        dat_dict = {
                "read_file_word": read_file_word,     #读取文件路径
                "save_file_word": save_file_word,     #存放word提取出来的数据
                "if_all": if_all                      #True读取文件夹中所有数据，False读取单个
            }
        self.post_word_txt(dat_dict)

    # 将文本中的每一行数据添加到列表中用于进行整理JSON数据使用：
    def transition(self):
        # 去重问题，使用集合：
        set_data = set()
        transition_list = []
        #     读取txt文件：
        read_path = "../txts/save_json/问题1.txt"
        save_path = "../txts/save_json/问题1.json"
        with open(read_path, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                set_data.add(i.strip())
        #     使用集合推导式
        {transition_list.append(i) for i in set_data}
        pal = {
            "text": transition_list
        }
        #     转换为JSON提问格式数据：
        if not os.path.exists(save_path):
            #             存入Json文件中
            with open(save_path, 'w', encoding='utf-8') as file:
                json.dump(pal, file, ensure_ascii=False, indent=4)
        else:
            with open(save_path, 'a', encoding='utf-8') as file:
                json.dump(pal, file, ensure_ascii=False, indent=4)


#     进行去重拼接数据：
    def de_weight_json(self):
#         输入保存过的数据集：
        save_data_input= input("请输入已保存数据集的路径：")
        # "../data_json正式数据/数据集/园林工程施工组织与管理.json"
        run_data_input= input("请输入新跑出来的数据集路径：")
        # ../data_json正式数据/joint.json
        self.de_weight(run_data_input,save_data_input)


if __name__ == '__main__':
    dat = DataView()

    # 提取pdf中的数据：
    procedure = input(">>>>>>请输入程序选项：\n1提取pdf中书本数据:\n2提取word中书本数据：\n3读取要提问的问题：\n4数据集去重：")

    if procedure == "1":
        dat.get_pdf_data()
    elif procedure == "2":
        dat.get_world_data()
    elif procedure == "3":
        dat.transition()
    elif procedure == "4":
        dat.de_weight_json()