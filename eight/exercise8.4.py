def make_shirt(shirt_size='big',shirt_printword='i love python'):
    """show the shirt size and printword"""
    print(f"you can get a {shirt_size} size and {shirt_printword} word shirt")

make_shirt('8','AA')
make_shirt(shirt_printword='BB',shirt_size='9')

make_shirt()
make_shirt('middle')
make_shirt('big','i love mars')