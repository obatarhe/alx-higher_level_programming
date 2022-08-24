#!/usr/bin/python3
for one in range(97, 123):
    if not(chr(one) == 'q' or chr(one) == 'e'):
        print("{}".format(chr(one)), end="")
