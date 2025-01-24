from pathlib import Path

contents="i loge programming \n"
contents+="i love creating new games \n"
contents+='i also love working with date .\n'

path=Path('programming.txt')
path.write_text(contents)
