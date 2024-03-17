
import re

def extract_sentences_with_keywords(text, keywords):
    # 将文本拆分成句子
    sentences = re.split(r'。|！|？', text)

    # 使用正则表达式匹配含有任意一个关键字的句子
    keyword_sentences = [sentence for sentence in sentences if any(re.search(keyword, sentence) for keyword in keywords)]

    return keyword_sentences

if __name__ == '__main__':

    # 示例文本
    text = """
    Python 是一种广泛使用的高级编程语言，用于通用编程，由 Guido van Rossum 创建，并于 1991 年首次发布。Python 的设计理念强调代码的可读性，其明显的缩进使用值得注意。其语言构造和面向对象的方法旨在帮助程序员编写适用于小型和大型项目的清晰、逻辑的代码。
    
    Python 有一个庞大的标准库，通常被认为是其最大的优势之一，提供适用于许多任务的工具。
    它还被广泛用于 Web 开发、科学计算、数据分析、人工智能等领域。
    
    Python 是一种解释型、高级和通用的编程语言。
    Python 的设计理念强调代码的可读性，其明显的缩进使用值得注意。
    
    与 Python 交互的几种技术：
    
    - 您可以使用文本编辑器编写 Python 程序，并从命令行运行它们。
    - 您可以使用集成开发环境（IDE）如 PyCharm、Visual Studio Code 或 Jupyter Notebook。
    - 您可以在终端中使用 Python 解释器交互地执行 Python 代码，也可以在诸如 IPython 或 Jupyter Notebook 的工具中执行 Python 代码。
    """

    keywords = input("请输入关键字，用空格分隔：")

    # 提取含有任意一个关键字的句子
    keyword_sentences = extract_sentences_with_keywords(text, keywords)

    print("含有关键字的句子：")
    for sentence in keyword_sentences:
        print("-", sentence)














