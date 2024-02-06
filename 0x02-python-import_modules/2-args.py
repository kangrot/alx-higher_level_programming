#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    arg.pop(0)
    lenght = len(arg)
    if lenght == 0:
        print("0 arguments.")
    elif lenght == 1:
        print(f"1 argument:\n1: {arg[0]}")
    else:
        print(f"{lenght} arguments:")
        for num, item in enumerate(arg):
            print(f"{num + 1}: {item}")
