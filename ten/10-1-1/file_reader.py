from pathlib import Path

path = Path('/Users/arch/Desktop/python_work/11/pi_digits.txt')
contents=path.read_text()
lines=contents.splitlines()
for line in lines:
    print(f"\n{line}")
