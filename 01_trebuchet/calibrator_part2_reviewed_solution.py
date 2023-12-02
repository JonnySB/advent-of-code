import re

with open("calibration_file.txt", "r") as f:
    content = f.readlines()

dictionary_converter = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total = 0

for line in content:
    nums = []
    for n in dictionary_converter:
        line = line.replace(
            n, str(n[0]) + str(dictionary_converter.get(n)) + str(n[-1]), line.count(n)
        )
    for char in line:
        if char.isnumeric():
            nums.append(char)
    total += int(nums[0] + nums[-1])

print(total)
