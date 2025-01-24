from pathlib import Path

def print_animal_names(filename,animal_type):
    try:
        path=Path(filename)
        names=path.read_text().rstrip().splitlines()
        for name in names:
            print(f"this {animal_type} name is {name}")
    except FileNotFoundError:
        pass

print_animal_names('cat.txt','cat')
print_animal_names('dog.txt','dog')
