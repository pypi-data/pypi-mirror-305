from sys import argv


def main(*args):
    args = argv[1:]
    print(f"\nmain({', '.join(args)})\n")
