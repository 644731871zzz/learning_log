from pathlib import Path

path=Path('alice.txt')
try:
    contents=path.read_text(encoding='utf-8')
except:
    print(f"sorry,the file {path} doex not exist")
else:
    #计算文件大致包含多少个单词
    words=contents.split()
    num_words=len(words)
    print(f"the file {path} has about {num_words} words.")