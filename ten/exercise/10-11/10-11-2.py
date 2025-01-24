from pathlib import Path
import json

path=Path('favorite_number.txt')
contents=path.read_text()
favorite_number=json.loads(contents)
print(f"i know your favorite number! it's : {favorite_number}")