#!/usr/bin/env python


def first(data):
    data = [i if i not in "\n" else "-" for i in data]
    data = [i.replace("\n", ",") for i in data]
    data = "".join(data).split("-")
    data = [i.rstrip(",") for i in data]
    data = [i.split(",") for i in data]
    result = max(sum(int(n) for n in i) for i in data)
    print(result)


def second(data):
    data = [i if i not in "\n" else "-" for i in data]
    data = [i.replace("\n", ",") for i in data]
    data = "".join(data).split("-")
    data = [i.rstrip(",") for i in data]
    data = [i.split(",") for i in data]
    result = sum(sorted(sum(int(n) for n in i) for i in data)[-3:])
    print(result)


def main(data):

    first(data)
    second(data)


if __name__ == "__main__":
    with open("one.txt") as f:
        data = [i for i in f]
    main(data)
