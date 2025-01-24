favorite_languages={
    'jen':'python',
    'sarach':'c',
    'edward':'rust',
    'phil':'python',
    }
print(f"jen favorite language is {favorite_languages['jen'].title()}")
print(favorite_languages.get('aage','no aage ,you can see this'))

print("\n")

friends=['jen','edward']
for name in favorite_languages:
    print(f"hi {name}")
    if name in friends:
        print(f"{name} you like {favorite_languages[name].title()}")

for name in sorted(favorite_languages):
    print(name)

for language in favorite_languages.values():
    print(language)
language_1=set(favorite_languages.values())
print(language_1)

print("\n")

access_names=[]