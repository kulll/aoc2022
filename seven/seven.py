#!/usr/bin/env python


def parse_data(data):
    root = {"/": {}}
    for i in data:
        match i.split():
            case ("$", "cd", "/"):
                current = root.get("/")
            case ("$", "cd", _dir):
                if _dir == "..":
                    current = current.get("parent")
                    continue
                parent = current
                dirs = current.get("dirs")
                current = dirs.get(_dir)
                current.update(parent=parent)

            case ("dir", name):
                dirs = current.get("dirs", {})
                dir_name = dirs.get(name, {})
                dirs.update({name: dir_name})
                current.update(dirs=dirs)

            case (filesize, name) if filesize.isdigit():
                files = current.get("files", [])
                files.append((filesize, name))
                current.update({"files": files})
    return root


def sum_files_current_dir(files):
    try:
        result = sum(int(size) for size, name in files)
    except TypeError:
        return 0

    return result


def sum_files_in_dir(data, placeholder, max_size=float("inf")):

    total_size = 0

    if "dirs" in data:
        dirs = data.get("dirs")

        for i in dirs:
            size = sum_files_in_dir(dirs.get(i), placeholder, max_size)
            total_size += size

        size = sum_files_current_dir(data.get("files"))
        total_size += size

    else:
        files = data.get("files")
        total_size += sum_files_current_dir(files)

    if total_size < max_size:
        placeholder.append(data)

    return total_size


def first(data):

    data = parse_data(data)
    current = data.get("/")
    placeholder = []
    sum_files_in_dir(current, placeholder, 100000)
    print(sum(sum_files_in_dir(i, [], 100000) for i in placeholder))


def second(data):
    data = parse_data(data)
    current = data.get("/")
    placeholder = []
    total_usage = sum_files_in_dir(current, placeholder)
    total_diskspace = 70000000
    minimum_required = 30000000
    needed_space = minimum_required - (total_diskspace - total_usage)
    result = min(
        x for i in placeholder if (x := sum_files_in_dir(i, [])) > needed_space
    )
    print(result)


if __name__ == "__main__":
    with open("seven.txt") as f:
        data_one = [i.strip("\n") for i in f]
        data_two = data_one[:]

    first(data_one)
    second(data_two)
