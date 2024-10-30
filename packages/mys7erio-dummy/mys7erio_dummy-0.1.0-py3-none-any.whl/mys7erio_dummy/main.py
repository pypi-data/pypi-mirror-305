import sys


def main():
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            print("Odd" if num % 2 else "Even")
        except ValueError:
            print("Invalid input")