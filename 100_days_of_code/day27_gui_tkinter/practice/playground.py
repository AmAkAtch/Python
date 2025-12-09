def add(*args):
    """Add as many arguments as you want to add them all together"""
    total = 0
    for n in args:
        total += n
    print(total)

add(1,4,5)