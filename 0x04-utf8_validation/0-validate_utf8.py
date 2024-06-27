#!/usr/bin/python3
""" sbnl lsddsl ds dssdd"""


def validUTF8(data):
    """ shbkj sdhjkb kjsd kd"""
    byte_count = 0

    for qwsa in data:
        if byte_count == 0:
            if qwsa >> 5 == 0b110 or qwsa >> 5 == 0b1110:
                byte_count = 1
            elif qwsa >> 4 == 0b1110:
                byte_count = 2
            elif qwsa >> 3 == 0b11110:
                byte_count = 3
            elif qwsa >> 7 == 0b1:
                return False
        else:
            if qwsa >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
