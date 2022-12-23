#!/usr/bin/env python

from collections import deque
from enum import Enum
from string import ascii_letters


def second(data):

    group = deque(maxlen=3)
    final = []

    for i in data:
        group.append(i)
        if len(group) == group.maxlen:
            grouped = (set(i) for i in group)
            one, two, three = grouped
            result = one & two & three
            final.append(result)
            group.clear()

    final = sum(priorities[str(*i)].value for i in final)
    print(final)


def first(data):
    data = [(i[: len(i) // 2], i[len(i) // 2 :]) for i in data]
    data = [(set(one), set(two)) for one, two in data]
    data = [one.intersection(two) for one, two in data]
    final = sum(priorities[str(*i)].value for i in data)

    print(final)


if __name__ == "__main__":
    with open("three.txt") as f:
        data = [i.strip() for i in f]

    priorities = Enum("priorities", list(ascii_letters))

    first(data)
    second(data)
