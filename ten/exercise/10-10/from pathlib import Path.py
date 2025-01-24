from pathlib import Path

path=Path('pg74662.txt')
book_invelve=path.read_text()

a=book_invelve.count('the')
b=book_invelve.lower().count('the')
c=book_invelve.count('the ')
d=book_invelve.lower().count('the ')

print(f"{a} {b} {c} {d}")