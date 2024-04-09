
# from transformers import BertTokenizer, BertForNextSentencePrediction
# import torch

# if __name__ == '__main__':


    # # 加载BERT模型和分词器
    # tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    # model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
    #
    # # 定义关键词
    # keyword = "apple"
    #
    # # 示例文本
    # text = "I like bananas. Apples are delicious fruits. Orange is another fruit."
    #
    # # 分词并编码
    # inputs = tokenizer(keyword, text, return_tensors='pt', padding=True, truncation=True)
    #
    # # 进行文本相似度预测
    # outputs = model(**inputs)
    #
    # # 获取相似度分数
    # score = torch.softmax(outputs.logits, dim=1)[0][0].item()
    #
    # # 打印文本与关键词的相似度分数
    # print(f"与关键词 '{keyword}' 相似度分数：{score}")




# import re

# ----   ——   ,  ，  !" ?  去掉
# if __name__ == '__main__':
#     # 读取原始文件
#     with open('../txts/save_word_txt/ce.txt', 'r', encoding='utf-8') as file:
#         original_text = file.readlines()
#         print(">>>>>",original_text)
#
#     # 定义正则表达式模式，用于匹配需要去除的字符\----\——\,\，\!"\?
#     pattern = r'[\“\”\.）’\.)\s<>(\-\—\,\，\!\?\"\'\、\=]+'
#
#     # 定义正则表达式模式，用于匹配每行开头的大小写数字
#     digit_pattern = r'^[A-Za-z0-9]+\s*'
#
#     # 打开新文件以写入处理后的内容
#     with open('../txts/save_word_txt/processed_text.txt', 'w', encoding='utf-8') as file:
#         # 遍历原始文件的每一行
#         for line in original_text:
#             # 使用正则表达式去除特定字符
#             clean_line = re.sub(pattern, '', line)
#             # 使用正则表达式去除每行开头的大小写数字
#             clean_line = re.sub(digit_pattern, '', clean_line)
#             # 去除句子两端的空白字符
#             clean_line = clean_line.strip()
#             # 如果处理后的行非空，则写入文件
#             if clean_line:
#                 # 在句子末尾添加句号和换行符
#                 for i in clean_line.split("。"):
#                     if i != "":
#                         # 使用正则表达式过滤掉 `·166·`
#                         clean_string = re.sub(r'·\d+·', '', i)
#                         file.write(clean_string + '。 \n')





import re



# def extract_chinese_text_with_punctuation(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read()
#     # 使用正则表达式匹配文本中的中文字符、逗号和句号
#     chinese_text_with_punctuation = re.findall(r'[\u4e00-\u9fff。]+', text)
#     # 将提取到的中文文字、逗号和句号连接成一个字符串
#     extracted_text = ''.join(chinese_text_with_punctuation)
#     # print(">>>>>>",extracted_text.split("。"))
#     for i in extracted_text.split("。"):
#         # print(i)
#         # clean_string = re.sub(r'·\d+·|\d+\)|\(\d+|\(\d+\)|\d+\. |\d+.\|+', '', i)
#         clean_string=i.replace("丨", "")
#         print(clean_string +"。")
#     return extracted_text


if __name__ == '__main__':
    # filename = "../txts/save_word_txt/ce.txt"
    # extract_chinese_text_with_punctuation(filename)


    # txt_data = "1. 我国\t是严重|的缺①水国家，尤 其北方地区，如 能在风 景园林绿地排  水的处 理方面采取一些行之有效的办法，对保护水一一一一资源具有一一非常重要一一的意义。"
    # chinese_text_with_punctuation = re.findall(r'[\u4e00-\u9fff，。]+', txt_data)
    # extracted_text = ''.join(chinese_text_with_punctuation)
    # print(extracted_text)
    # # clean_string = re.sub(r"\d+\.", '', extracted_text)
    # if ' ' in txt_data:
    #     a=extracted_text.replace("|", "").replace("一", "").replace(' ','').replace("\t",'')
    #
    #     print(a)
    # with open("../txts/save_pdf_txt/园林塑石假山设计.txt",'r',encoding='utf-8') as f:
    #     text = f.read()
    #
    # save_txt_path = "../txts/save_pdf_txt/园林塑石假山设计2.txt"
    # with open(f"{save_txt_path}", 'a+', encoding='utf-8') as file:
    #     # 使用正则表达式匹配文本中的中文字符、逗号和句号
    #     chinese_text_with_punctuation = re.findall(r'[\u4e00-\u9fff，。]+', text)
    #     # 将提取到的中文文字、逗号和句号连接成一个字符串
    #     extracted_text = ''.join(chinese_text_with_punctuation)
    #     for i in extracted_text.split("。"):
    #         # 去除每行中指定的数据
    #         # 替换每行中的 |
    #         clean_string = i.replace("|", "").replace("丨", "").replace("一", "").replace(' ', '').replace("\t", '')
    #         file.write(clean_string + "。\n")

    txt_data = "园林工程竣工验收项目较多，需要时间长，要根据工程的规模合理选择验收程序和方法"
    if txt_data[-1] != "。":
        txt_data = txt_data +"。"
    print(txt_data)
