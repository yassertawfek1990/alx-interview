#!/usr/bin/python3
""" Rs dsck"""
import sys


def print_msg(cs, f):
    print("File size: <{}>".format(f))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("<{}>: <{}>".format(k, v))


f = 0
c = 0
cl = 0
cs = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for las in sys.stdin:
        pl = las.split()
        pl = pl[::-1]

        if len(pl) > 2:
            cl += 1

            if cl <= 10:
                f += int(pl[0])
                c = pl[1]

                if (c in cs.keys()):
                    cs[c] += 1

            if (cl == 10):
                print_msg(cs, f)
                cl = 0

finally:
    print_msg(cs, f)
