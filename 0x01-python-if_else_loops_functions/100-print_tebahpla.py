#!/usr/bin/python3
for letter in range(122, 98, -2):
    for letter2 in range(89, 64, -2):
        print("{}{}".format(chr(letter), chr(letter2)), end="")
