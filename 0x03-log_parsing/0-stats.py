#!/usr/bin/python3
""" asd fd"""


def parseLogs():
    """
    Readff
    Reports: fdf
    Raises: df"""
    stdin = __import__('sys').stdin
    ln = 0
    fs = 0
    st = {}
    co = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for e in stdin:
            ln += 1
            e = e.split()
            try:
                fs += int(e[-1])
                if e[-2] in co:
                    try:
                        st[e[-2]] += 1
                    except KeyError:
                        st[e[-2]] = 1
            except (IndexError, ValueError):
                pass
            if ln == 10:
                report(fs, st)
                ln = 0
        report(fs, st)
    except KeyboardInterrupt as e:
        report(fs, st)
        raise


def report(f, sc):
    """
    Prrc
    Args:
        f (int): t
        sc (dict): d
    """
    print("File size: {}".format(f))
    for k, v in sorted(sc.items()):
        print("{}: {}".format(k, v))


if __name__ == '__main__':
    parseLogs()
