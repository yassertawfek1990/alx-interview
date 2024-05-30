#!/usr/bin/python3
"""0-pascal_triangle """


def pascal_triangle(n):
    """bgbb"""
    gg = []
    if n <= 0:
        return gg
    gg = [[1]]
    for b in range(1, n):
        gp = [1]
        for v in range(len(gg[b - 1]) - 1):
            d = gg[b - 1]
            gp.append(gg[b - 1][v] + gg[b - 1][v + 1])
        gp.append(1)
        gg.append(gp)
    return gg
