from pathlib import Path
import json

path=Path('favorite_number.txt')
if path.exists():
    contents=path.read_text()
    favorite_number=json.loads(contents)
    print(f"i know your favorite number! it's : {favorite_number}")
else:
    favorite_number=input("what number is your favorite number? ")
    try:
        favorite_number=int(favorite_number)
    except ValueError:
        print("Please enter a valid number.")
    else:
        contents=json.dumps(favorite_number)
        path.write_text(contents)
        print(f"we'll remember your favorite number {favorite_number}")