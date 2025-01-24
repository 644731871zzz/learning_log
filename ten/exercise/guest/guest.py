from pathlib import Path

contents=input("give your name : ")

path=Path('name.txt')
path.write_text(contents)