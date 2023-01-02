#!/usr/bin/env python

import re
from collections import deque


def parse_crates(crates):
    def cleanup(data):
        return data.isalnum()

    crates = zip(*(i for i in crates))
    crates = (list(filter(cleanup, i)) for i in crates)
    crates = (i for i in crates if i)
    crates = {i[-1]: deque(i[:-1]) for i in crates}
    return crates


def parse_arrangements(arrangements):
    return [re.findall("\d+", i) for i in arrangements]


def first(crates, arrangements):
    for count, origin, destination in arrangements:
        for i in range(int(count)):
            crates[destination].appendleft(crates[origin].popleft())
    print("".join((i[0]) for i in crates.values()))


def second(crates, arrangements):
    for count, origin, destination in arrangements:
        temp = deque()
        for i in range(int(count)):
            try:
                temp.append(crates[origin].popleft())
            except IndexError:
                break


        temp.reverse()
        crates[destination].extendleft(temp)
    print("".join((i[0]) for i in crates.values()))


if __name__ == "__main__":
    with open("five.txt") as f:
        data = [i.strip("\n") for i in f]

    crates = []
    while data:
        c = data.pop(0)
        if c == "":
            break
        crates.append(c)

    arrangements = data

    crates_one = parse_crates(crates)
    crates_two = parse_crates(crates)
    arrangements = parse_arrangements(arrangements)

    first(crates_one, arrangements)
    second(crates_two, arrangements)
