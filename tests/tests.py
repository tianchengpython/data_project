
from transformers import BertTokenizer, BertForNextSentencePrediction
import torch

if __name__ == '__main__':


    # 加载BERT模型和分词器
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')

    # 定义关键词
    keyword = "apple"

    # 示例文本
    text = "I like bananas. Apples are delicious fruits. Orange is another fruit."

    # 分词并编码
    inputs = tokenizer(keyword, text, return_tensors='pt', padding=True, truncation=True)

    # 进行文本相似度预测
    outputs = model(**inputs)

    # 获取相似度分数
    score = torch.softmax(outputs.logits, dim=1)[0][0].item()

    # 打印文本与关键词的相似度分数
    print(f"与关键词 '{keyword}' 相似度分数：{score}")














