
# 整理数据试图：
import os
import json
from utils import DataTiramisu
from models.db_model import insert_data,select_data


class DataView(DataTiramisu):

    # def __init__(self):
    #     super.__init__()


    # 提取pdf中的数据：
    def get_pdf_data(self):
        read_file_pdf = input("》》》》》》请输入读取文件路径：").strip()
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

        # print(">>>>>>>",data_dict)

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

    # 添加到数据库中
    def get_dat(self):
        print(">>>>>开始整理数据集:")
        input_txt_path = input("》》》》》》请输入读取文件路径：")
        input_book_name = input("》》》》》》请输入书本名称：")
        #         进行读取文本中的数据;
        resp_txt = self.get_data_txt(input_txt_path).split("。")

        # 思路：1.分割完后进行存入数据库
        for i in resp_txt:
            if i != "":
                insert_sql = f"INSERT INTO data_text (data_txt,book_name) VALUES ('{i}','{input_book_name}')"
                insert_data(insert_sql)

    # 读取转换为json数据集：
    def get_save_json(self):

        input_data = input("》》》》》》请输入关键字：").split(" ")
        # 2.将读出来的数据存入数据库，根据输入的关键字从数据库中模糊查询一下，查询相关语句

        # print(">>>>>",input_data)

        joint_list = []
        try:
            for i in input_data:
                select_sql = f"SELECT id,data_txt FROM data_text WHERE data_txt LIKE '%{i}%'"
                resp_data = select_data(select_sql)
                # print(">>>>>",resp_data)
                if len(resp_data) > 1:
                #     添加到json数据中
                    data_pal = {
                        "instruction": i,
                        "input": "",
                        # 获取从数据库读出来的[('id','data_txt')]这种格式的数据
                        "output": resp_data[0][1]
                    }
                    joint_list.append(data_pal)
                else:
                    data_pal = {
                        "instruction": i,
                        "input": "",
                        "output": resp_data[0][1]
                    }
                    joint_list.append(data_pal)

            # print(joint_list)

            # 如果没有文件就创建文件：如果有文件就进行合并数据：
            if os.path.exists("../save_json/data_pal.json"):
                # 1.先将原本的json数据读出来
                with open("../save_json/data_pal.json", "r",encoding="utf-8") as f:
                    file_data = f.read()
                    file_data = eval(file_data)
                    # 将读取出来的数据跟当前获取出来相关的数据合并
                    for j in joint_list:
                        file_data.append(j)
                    with open("../save_json/data_pal.json", "w",encoding="utf-8") as file:
                        json.dump(file_data, file, ensure_ascii=False, indent=4)
            else:
                with open("../save_json/data_pal.json", "w", encoding="utf-8") as file:
                    json.dump(joint_list, file, ensure_ascii=False, indent=4)


            print(">>>>>>转换数据集完成")

        except Exception as e:
            print(">>>>>>模糊查询异常！",e)



if __name__ == '__main__':
    dat = DataView()

    # 提取pdf中的数据：
    procedure = input(">>>>>>请输入程序选项：\n1提取pdf中书本数据:\n2提取word中书本数据：\n3将提取的数据添加至数据库：\n4将数据转换为JSON格式：")

    if procedure == "1":
        dat.get_pdf_data()
    elif procedure == "2":
        dat.get_world_data()
    elif procedure == "3":
        dat.get_dat()
    elif procedure == "4":
        dat.get_save_json()


# 1.下午2点跟胡耘硕对接一下数据集上线整体流程
# 4.进行更准确的完成查询




# if __name__ == '__main__':
#     dat = DataTiramisu()
#     # 提取pdf文件中的数据：
#     data_dict = {
#         "read_file_pdf":'../data_files/pdf/1.pdf',   #读取文件路径
#         "new_pdf_file_path":'../data_files/pdf/new_1.pdf',  #读取单个pdf才使用到
#         "save_img_path":'../static/', #存放要提取数据图片
#         "save_txt_path":'../txts/save_pdf_txt/pdf.txt', #存放提取后的文本存放地址
#         "start_num":0, #单个pdf使用：开始
#         "end_num":3, #单个pdf使用：结束
#         "if_all":False #True读取文件夹中所有数据，False读取单个
#     }
#     dat.post_pdf_txt(data_dict)


