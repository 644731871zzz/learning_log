from pathlib import Path
import json

favorite_number=input("what number is your favorite number? ")
path=Path('favorite_number.txt')
contents=json.dumps(favorite_number)
path.write_text(contents)