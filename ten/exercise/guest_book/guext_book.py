from pathlib import Path

guext_books=''
guext_active=True
while guext_active:
    guext_book=input("give name: || you can write 'q' to quit  ")
    if guext_book== 'q':
        guext_active=False
    else:
        guext_books+=guext_book
        guext_books+='\n'
        path=Path('guest_book.txt')
        path.write_text(guext_books)


