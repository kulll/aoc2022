#!/usr/bin/env python

from collections import deque


def first(data):
    """
    >>> first(
    ...    [
    ...        "bvwbjplbgvbhsrlpgdmjqwftvncz",
    ...        "nppdvjthqldpwncqszvftbrmjlhg",
    ...        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    ...        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ...    ]
    ... )
    5
    6
    10
    11
    """

    for d in data:
        check = deque(maxlen=4)
        for i, v in enumerate(d):
            check.append(v)
            if len(set(check)) == 4:
                print(i + 1)
                break


def second(data):
    """
    >>> second(
    ...    [
    ...        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    ...        "bvwbjplbgvbhsrlpgdmjqwftvncz",
    ...        "nppdvjthqldpwncqszvftbrmjlhg",
    ...        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    ...        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ...    ]
    ... )
    19
    23
    23
    29
    26

    """
    for d in data:
        check = deque(maxlen=14)
        for i, v in enumerate(d):
            check.append(v)
            if len(set(check)) == 14:
                print(i + 1)
                break


if __name__ == "__main__":
    with open("six.txt") as f:
        data_one = [i.strip("\n") for i in f]
        data_two = data_one[:]

    first(data_one)
    second(data_two)
