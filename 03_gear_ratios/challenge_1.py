with open("input_file.txt") as f:
    gears_input = f.readlines()

lines = [line.strip() for line in gears_input]
line_length = len(lines[0])
list_length = len(lines)


def get_chunk_indexes(line):
    chunk_indexes = []
    chunk_index_dict = {}
    for index in range(len(line)):
        num = line[index]
        if num.isnumeric():
            if chunk_index_dict.get("start") is None:
                chunk_index_dict["start"] = int(index)
                chunk_index_dict["end"] = int(index) + 1
            else:
                chunk_index_dict["end"] = int(index) + 1
        elif chunk_index_dict.get("start") is not None:
            chunk_indexes.append(chunk_index_dict)
            chunk_index_dict = {}
    if chunk_index_dict.get("start") is not None:
        chunk_indexes.append(chunk_index_dict)
    return chunk_indexes


def check_for_adj_on_current_line(chunk_index_dict, current_line):
    start = chunk_index_dict["start"] - 1
    end = chunk_index_dict["end"]

    chars_to_check = set()

    if start >= 0:
        chars_to_check.add(current_line[start])
    if end < len(current_line):
        chars_to_check.add(current_line[end])

    chars_to_check.discard(".")
    if len(chars_to_check) > 0:
        return True
    else:
        return False


def check_for_adj_on_another_line(chunk_index_dict, other_line):
    start = chunk_index_dict["start"] - 1
    end = chunk_index_dict["end"] + 1
    if start < 0:
        start = 0
    if end > len(other_line):
        end = len(other_line)

    for char in other_line[start:end]:
        if char.isnumeric() or char == ".":
            continue
        else:
            return True
    return False


total = 0
for current_line_index in range(len(lines)):
    # set up line indexes
    prev_line_index = current_line_index - 1
    next_line_index = current_line_index + 1

    # get all chunk indexes
    chunks = get_chunk_indexes(lines[current_line_index])

    list_to_add = []

    for chunk_dict in chunks:
        if prev_line_index >= 0 and prev_line_index < len(lines) - 1:
            if check_for_adj_on_another_line(chunk_dict, lines[prev_line_index]):
                number = lines[current_line_index][
                    chunk_dict["start"] : chunk_dict["end"]
                ]
                list_to_add.append(number)
                continue
        if check_for_adj_on_current_line(chunk_dict, lines[current_line_index]):
            number = lines[current_line_index][chunk_dict["start"] : chunk_dict["end"]]
            list_to_add.append(number)
            continue
        if next_line_index <= len(lines) - 1:
            if check_for_adj_on_another_line(chunk_dict, lines[next_line_index]):
                number = lines[current_line_index][
                    chunk_dict["start"] : chunk_dict["end"]
                ]
                list_to_add.append(number)
                continue
    for num in list_to_add:
        total += int(num)

print(total)
