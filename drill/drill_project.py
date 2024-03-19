from transformers import pipeline


if __name__ == '__main__':

    # 加载问答模型
    question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")


    # 读取文本数据
    text = """
    这是书本的内容，一些内容在这里...
    这是第一章的内容。第一章讨论了...什么什么
    这是第二章的内容。第二章解释了...
    """

    # 提问并获取回答
    question = "什么是第一章讨论的内容？"
    answer = question_answerer(question=question, context=text)
    print(answer)









from transformers import GPT2Tokenizer, GPT2ForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset


# 定义问答数据集类
# class QADataset(Dataset):
#     def __init__(self, data, tokenizer, max_length=512):
#         self.data = data
#         self.tokenizer = tokenizer
#         self.max_length = max_length
#
#     def __len__(self):
#         return len(self.data)
#
#     def __getitem__(self, idx):
#         item = self.data[idx]
#         encoding = self.tokenizer(item['question'], item['context'], truncation=True, padding='max_length',
#                                   max_length=self.max_length, return_tensors='pt')
#         return {key: torch.squeeze(value, dim=0) for key, value in encoding.items()}
#
# if __name__ == '__main__':
#
#     # 读取问答数据
#     qa_data = [
#         {"question": "你是一个虚拟助手吗？", "context": ""},
#         {"question": "你是谁？", "context": ""},
#         # 其他问答对
#     ]
#
#     # 加载GPT-2 tokenizer和模型
#     tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#     model = GPT2ForSequenceClassification.from_pretrained('gpt2')
#
#     # 准备数据集
#     train_dataset = QADataset(qa_data, tokenizer)
#
#     # 定义训练参数
#     training_args = TrainingArguments(
#         output_dir='./results',
#         num_train_epochs=3,
#         per_device_train_batch_size=8,
#         save_steps=500,
#         save_total_limit=2,
#         logging_dir='./logs',
#         logging_steps=100
#     )
#
#     # 定义Trainer对象
#     trainer = Trainer(
#         model=model,
#         args=training_args,
#         train_dataset=train_dataset
#     )
#
#     # 开始微调训练
#     trainer.train()




# from transformers import BertTokenizer, BertForQuestionAnswering
# from torch.utils.data import DataLoader
# from transformers import AdamW
# import torch
#
#
# if __name__ == '__main__':
#
#     # 读取书本的文本数据
#     book_text = """
#     这是书本的内容，一些内容在这里...
#     这是第一章的内容。第一章讨论了...
#     这是第二章的内容。第二章解释了...
#     """
#
#     # 假设我们有一些问题和答案
#     qa_pairs = [
#         {"question": "什么是第一章讨论的内容？", "answer": "第一章讨论了..."},
#         {"question": "第二章解释了什么？", "answer": "第二章解释了..."}
#         # 可以添加更多的问题和答案对
#     ]
#
#     # 准备问答数据集
#     qa_dataset = []
#     for pair in qa_pairs:
#         for sentence in book_text.split('.'):
#             if pair["answer"] in sentence:
#                 qa_dataset.append({"question": pair["question"], "context": sentence})
#
#     # 初始化BERT分词器和模型
#     tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
#     model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
#
#     # 数据预处理函数
#     def prepare_dataset(dataset):
#         inputs = tokenizer(dataset['question'], dataset['context'], return_tensors='pt', padding=True, truncation=True)
#         return inputs
#
#     # 将数据集转换为模型可接受的格式
#     qa_dataset = list(map(prepare_dataset, qa_dataset))
#
#     # 定义DataLoader
#     train_dataloader = DataLoader(qa_dataset, batch_size=1)
#
#     # 定义优化器
#     optimizer = AdamW(model.parameters(), lr=5e-5)
#
#     # 训练模型
#     num_epochs = 3
#     for epoch in range(num_epochs):
#         model.train()
#         total_loss = 0
#         for batch in train_dataloader:
#             optimizer.zero_grad()
#             outputs = model(**batch, labels=batch['input_ids'])
#             loss = outputs.loss
#             loss.backward()
#             optimizer.step()
#             total_loss += loss.item()
#         print(f"Epoch {epoch+1}/{num_epochs}, Loss: {total_loss}")
#
#     # 模型应用示例
#     def get_answer(question):
#         inputs = tokenizer(question, book_text, return_tensors='pt')
#         outputs = model(**inputs)
#         start_scores = outputs.start_logits
#         end_scores = outputs.end_logits
#         all_tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
#         answer = ' '.join(all_tokens[torch.argmax(start_scores): torch.argmax(end_scores)+1])
#         answer = tokenizer.convert_tokens_to_string(answer)
#         return answer
#
#
#
#     # 测试模型
#     question = "什么是第一章讨论的内容？"
#     print(f"Question: {question}")
#     print(f"Answer: {get_answer(question)}")





