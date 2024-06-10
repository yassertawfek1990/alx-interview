#!/usr/bin/python3
"""Iner terext fierle."""


def minOperations(n: int) -> int:
    """ers thgre rg"""
    ss = 2
    oo = 0
    while n > 1:
        while n % ss == 0:
            oo += ss
            n /= ss
        ss += 1
    return oo
