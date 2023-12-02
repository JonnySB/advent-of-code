import re

with open("calibration_file.txt", "r") as f:
    content = f.readlines()

dictionary = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

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

for row in content:
    numbers = []
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i:j] in dictionary:
                if len(row[i:j]) > 1:
                    numbers.append(dictionary_converter[row[i:j]])
                else:
                    numbers.append(row[i:j])
    final_num = ""
    if len(numbers) == 1:
        final_num = numbers[0] * 2
    else:
        final_num = numbers[0] + numbers[-1]
    total += int(final_num)
print(total)
