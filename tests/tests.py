
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




import re

# ----   ——   ,  ，  !" ?  去掉
if __name__ == '__main__':
    # 读取原始文件
    with open('../txts/save_word_txt/ce.txt', 'r', encoding='utf-8') as file:
        original_text = file.readlines()
        print(">>>>>",original_text)

    # 定义正则表达式模式，用于匹配需要去除的字符\----\——\,\，\!"\?
    pattern = r'[\“\”\.）’\.)\s<>(\-\—\,\，\!\?\"\'\、\=]+'

    # 定义正则表达式模式，用于匹配每行开头的大小写数字
    digit_pattern = r'^[A-Za-z0-9]+\s*'

    # 打开新文件以写入处理后的内容
    with open('../txts/save_word_txt/processed_text.txt', 'w', encoding='utf-8') as file:
        # 遍历原始文件的每一行
        for line in original_text:
            # 使用正则表达式去除特定字符
            clean_line = re.sub(pattern, '', line)
            # 使用正则表达式去除每行开头的大小写数字
            clean_line = re.sub(digit_pattern, '', clean_line)
            # 去除句子两端的空白字符
            clean_line = clean_line.strip()
            # 如果处理后的行非空，则写入文件
            if clean_line:
                # 在句子末尾添加句号和换行符
                for i in clean_line.split("。"):
                    if i != "":
                        # 使用正则表达式过滤掉 `·166·`
                        clean_string = re.sub(r'·\d+·', '', i)
                        file.write(clean_string + '。 \n')





