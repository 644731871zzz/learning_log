from pathlib import Path
import json

path=Path('favorite_number.txt')
if path.exists():
    contents=path.read_text()
    favorite_number=json.loads(contents)
    print(f"i know your favorite number! it's : {favorite_number}")
else:
    favorite_number=input("what number is your favorite number? ")
    path=Path('favorite_number.txt')
    contents=json.dumps(favorite_number)
    path.write_text(contents)