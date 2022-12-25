#!/usr/bin/env python


def first(data):
    """
    >>> first(["1-5,5-10"])
    0
    >>> first(["1-6,5-10"])
    0
    >>> first(["1-10,5-5"])
    1
    >>> first(["5-6,1-10"])
    1
    >>> first(["49-69,49-49"])
    1
    >>> first(["11-11,11-49"])
    1
    >>> first(["49-69,49-49"])
    1
    >>> first(["9-20,10-90"])
    0

    """
    data = [i.split(",") for i in data]
    data = [(i.split("-"), v.split("-")) for i, v in data]
    data = [([int(ii) for ii in i], [int(vv) for vv in v]) for i, v in data]
    data = [(range(i[0], i[1] + 1), range(v[0], v[1] + 1)) for i, v in data]

    data = [set(i) <= set(v) or set(v) <= set(i) for i, v in data]

    print(data.count(True))


def second(data):
    """
    >>> second(["2-4,6-8"])
    0
    >>> second(["2-3,4-5"])
    0
    >>> second(["5-7,7-9"])
    1
    >>> second(["2-8,3-7"])
    1
    >>> second(["6-6,4-6"])
    1
    >>> second(["2-6,4-8"])
    1
    """
    data = [i.split(",") for i in data]
    data = [(i.split("-"), v.split("-")) for i, v in data]
    data = [([int(ii) for ii in i], [int(vv) for vv in v]) for i, v in data]
    data = [(range(i[0], i[1] + 1), range(v[0], v[1] + 1)) for i, v in data]

    data = [bool(set(i) & set(v)) for i, v in data]

    print(data.count(True))


if __name__ == "__main__":
    with open("four.txt") as f:
        data = [i.strip() for i in f]

    first(data)
    second(data)
