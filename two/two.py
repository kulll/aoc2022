#!/usr/bin/env python
from enum import Enum


def check_winner(first, second):
    if first - second == 2:
        return False
    if first - second == -2:
        return True
    if first > second:
        return True


def get_draw(p, i):
    return p.value + i.value


def get_lose(p, i):
    if (result := p.value - 1) == 0:
        return 3 + i.value
    return result + i.value


def get_win(p, i):
    if (result := p.value + 1) == 4:
        return 1 + i.value
    else:
        return result + i.value


def second(data):
    player = Enum("player", ["A", "B", "C"])
    instruction = Enum("instruction", [("X", 0), ("Y", 3), ("Z", 6)])
    data = [i.split() for i in data]

    lose = (
        get_lose(player[p], instruction[i])
        for p, i in data
        if instruction[i].name == "X"
    )

    draw = (
        get_draw(player[p], instruction[i])
        for p, i in data
        if instruction[i].name == "Y"
    )

    win = (
        get_win(player[p], instruction[i])
        for p, i in data
        if instruction[i].name == "Z"
    )

    print(sum([*win, *lose, *draw]))


def first(data):

    player_one = Enum("player_one", ["A", "B", "C"])
    player_two = Enum("player_one", ["X", "Y", "Z"])

    data = [i.split() for i in data]
    win = (
        player_two[two].value + 6
        for one, two in data
        if check_winner(player_two[two].value, player_one[one].value)
    )
    lose = (
        player_two[two].value + 0
        for one, two in data
        if check_winner(player_one[one].value, player_two[two].value)
    )

    draw = (
        player_two[two].value + 3
        for one, two in data
        if player_one[one].value == player_two[two].value
    )

    print(sum([*win, *lose, *draw]))


if __name__ == "__main__":
    with open("two.txt") as f:
        data = [i.strip() for i in f]
    first(data)
    second(data)
