# 工具库
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import time
import docx
import random
import re
import json
# 支持word,txt,pdf,提取文字的封装:
class DataTiramisu():

    def __init__(self):
        # 配置Tesseract OCR修改路径：
        self.Tesseract = r"D:\Tesseract-OCR\tesseract.exe"

    def get_data_txt(self,txt_path):

        content = ""
        with open(txt_path,'r',encoding='utf-8') as file:
            for line in file:
                content += line.strip()
        content = content.replace(" ", "")
        return content

    def post_word_txt(self,dat_dict):
        try:
            print(">>>>>>开始提取word中的数据")
            start_time = time.time()
    #         是否将文件
            read_file_word = dat_dict['read_file_word']
            save_file_word = dat_dict['save_file_word']
            if_all = dat_dict['if_all']

            # 等于True的情况下获取文件夹中的所有word文档，进行提取数据：
            if if_all == "True":
                # 定义正则表达式模式，用于匹配需要去除的字符
                pattern = r'[\“\”\.）’\.)\s<>(\-\—\,\，\!\?\"\'\、\=\．]+'
                # 定义正则表达式模式，用于匹配每行开头的大小写数字
                digit_pattern = r'^[A-Za-z0-9]+\s*'
                dat_list = os.listdir(read_file_word)
                for i in dat_list:
                    doc = docx.Document(f"{read_file_word}{i}")
                    for j in doc.paragraphs:
                        with open(save_file_word, 'a+', encoding='utf-8') as file:
                            # 使用正则表达式去除特定字符
                            clean_line = re.sub(pattern, '', j.text.strip())
                            # 使用正则表达式去除每行开头的大小写数字
                            clean_line = re.sub(digit_pattern, '', clean_line)
                            # 去除句子两端的空白字符
                            clean_line = clean_line.strip()
                            # 如果处理后的行非空，则写入文件
                            if clean_line:
                                # 在句子末尾添加句号和换行符
                                for i in clean_line.split("。"):
                                    # 将 .213. 这种数据过滤掉 和 4)这样的数据
                                    clean_string = re.sub(r'·\d+·|\d+\)|\(\d+|\(\d+\)|\d+\. |\d+.', '', i)
                                    if i != "":
                                        file.write(clean_string + '。 \n')
            # 记录程序结束时间
            end_time = time.time()
            # 计算程序运行时间
            running_time = end_time - start_time
            print(">>>>>>提取数据操作结束,程序运行时间：", running_time, "秒")
            print("\n\n\n")
        except Exception as e:
            print(">>>>>>读取文件时出现异常！",e)


    def post_pdf_txt(self,data_dict):

        dat = data_dict
        read_file_pdf = dat['read_file_pdf']
        new_pdf_file_path =dat['new_pdf_file_path']
        save_img_path =dat['save_img_path']
        save_txt_path =dat['save_txt_path']
        start_num =dat['start_num']
        end_num =dat['end_num']
        if_all = dat['if_all']

        print(">>>>>>开始提取pdf中的数据")
        # 记录程序开始时间
        start_time = time.time()

        # 读取文件夹下所有的pdf文件进行提取数据：

        # 使用Tesseract OCR提取图片中的文字
        pytesseract.pytesseract.tesseract_cmd = self.Tesseract

        # 获取支持的语言列表
        supported_languages = pytesseract.get_languages()
        # print("Supported languages:", supported_languages)

        try:
            if if_all == "True":
                #获取文件夹中所有数据
            #     读取文件夹中所有pdf文件
                pdf_list = os.listdir(read_file_pdf)
                for i in pdf_list:
                    # 将pdf文件中的数据转换为图片
                    pages = convert_from_path(f"{read_file_pdf}{i}", 500)
                    for page in pages:
                        # print(">>>>>>",page)
                        filename = f"{save_img_path}page_" + str(random.randint(100000,999999)) + ".jpg"
                        # print(filename)
                        page.save(filename, 'JPEG')

            else:
                # print(">>>>>6666我是false选项")
            #     进行获取单个数据：
            # 读取pdf文件：
                pdfFile = open(read_file_pdf, 'rb')
                pdf_input = PyPDF2.PdfReader(pdfFile)
                # 创建一个新的pdf文件
                pdf_output = PyPDF2.PdfWriter()
                for i in range(int(start_num), int(end_num)):
                    pdf_output.add_page(pdf_input.pages[i])
                pdf_output.write(open(new_pdf_file_path, 'wb'))

                # 将pdf转换为图片的形式进行操作：
                pages = convert_from_path(new_pdf_file_path, 500)

                image_counter = 1
                for page in pages:
                    filename = f"{save_img_path}page_" + str(image_counter) + ".jpg"
                    page.save(filename, 'JPEG')
                    image_counter += 1

        except Exception as e:
            print(">>>>>>操作单个或多个pdf文件异常",e)

        try:
            # 打开图片
            file_list = os.listdir(save_img_path)
            for filename in file_list:
                # 读取图片数据:
                image = Image.open(f"{save_img_path}{filename}")
                # # 使用Tesseract OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang=supported_languages[0])
                # print(text)
                with open(f"{save_txt_path}", 'a+', encoding='utf-8') as file:
                    # 使用正则表达式匹配文本中的中文字符、逗号和句号
                    chinese_text_with_punctuation = re.findall(r'[\u4e00-\u9fff,。]+', text)
                    # 将提取到的中文文字、逗号和句号连接成一个字符串
                    extracted_text = ''.join(chinese_text_with_punctuation)

                    # print(">>>>>>获取出的文字查看是否有逗号",extracted_text)

                    for i in extracted_text.split("。"):
                        # 去除每行中指定的数据
                        # 替换每行中的 |
                        clean_string = i.replace("|", "").replace(",","，").replace("丨", "").replace("一", "").replace(' ','').replace("\t",'')
                        file.write(clean_string +"。\n")

            print(">>>>>>提取pdf数据完成\n\n")

        #       读取完后将新创建的文件进行删除：
        #    删除新创建pdf文件：
            if if_all == "False":
                os.remove(new_pdf_file_path)
        #     删除静态图片数据：
            for r_i in file_list:
                os.remove(f"{save_img_path}{r_i}")

            # 记录程序结束时间
            end_time = time.time()
            # 计算程序运行时间
            running_time = end_time - start_time
            print(">>>>>>提取数据操作结束,程序运行时间：", running_time, "秒")
            print("\n\n\n")

        except Exception as e:
            print(">>>>>>读取图片文件失败！",e)


#    获取出来的数据与当前数据对比，为了解决重复率过高：
    def de_weight(self,run_data_path:str,save_data_path:str):
        try:
            save_data_list = []
            with open(f"{save_data_path}",'r',encoding='utf-8') as f:
                save_content = f.read()
            for i in eval(save_content):
                save_data_list.append(i['output'])

            run_data_list = []
            with open(f"{run_data_path}",'r',encoding='utf-8') as fz:
                run_content = fz.read()
            for j in eval(run_content):
                run_data_list.append(j['output'])

            num = 0
            pal_list = []
#             循环已保存的数据，将跑出来的数据比保存过的数据进行对比，要求跑出来的数据题目不能相同，问题也不能和已有的数据相同，若重复就不追加
            for run_i in run_data_list:
                if run_i not in save_data_list:
                    num += 1
                    key_name = ""
                    for run_j in eval(run_content):
                        if run_i == run_j['output']:
                            key_name = run_j['instruction']
            #         进行拼接数据:
                    pal_list.append({"instruction": key_name,"input": "","output": run_i})

            save_data = eval(save_content)
            save_data.extend(pal_list)
            data_str = json.dumps(save_data,indent=5).encode('utf-8').decode('unicode_escape')
#             将数据保存到指定文件中：
            with open(save_data_path,'w',encoding='utf-8')as save_f:
                save_f.write(data_str)

            print(f">>>>>>去重拼接数据成功,已新增{num}条数据")
        except Exception as e:
            print(">>>>>>去重拼接数据异常！",e)


if __name__ == '__main__':
    dat = DataTiramisu()
    save_data_path = "./data_json正式数据/数据集/园林工程施工与管理.json"
    run_data_path = "./data_json正式数据/joint.json"
    dat.de_weight(run_data_path,save_data_path)


    # dat.pdf_characters_txt()
    # 提取pdf文件中的数据：
    # data_dict = {
    #     "read_file_pdf":"./data_files/pdf/1.pdf",   #读取文件路径
    #     "new_pdf_file_path":"./data_files/pdf/new_1.pdf",  #读取单个pdf才使用到
    #     "save_img_path":"./static/", #存放要提取数据图片
    #     "save_txt_path":"./txts/save_pdf_txt/1pdf.txt", #存放提取后的文本存放地址
    #     "start_num":0, #单个pdf使用：开始
    #     "end_num":3, #单个pdf使用：结束
    #     "if_all":False #True读取文件夹中所有数据，False读取单个
    # }
    # dat.post_pdf_txt(data_dict)
