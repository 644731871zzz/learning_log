from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少词汇"""
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        #计算文件大致包含多少单词
        words=contents.split()
        num_words=len(words)
        print(f"the file {path} has abou {num_words} words")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    path=Path(filename)
    count_words(path)