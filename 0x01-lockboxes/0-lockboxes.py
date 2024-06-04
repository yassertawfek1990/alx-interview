#!/usr/bin/python3
""" Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes) """


def canUnlockAll(boxes):
    """ Check if boxes can be unlocked """
    for m in range(1, len(boxes) - 1):
        r = False
        for x in range(len(boxes)):
            r = (m in boxes[x] and m != x)
            if r:
                break
        if r is False:
            return r
    return True
