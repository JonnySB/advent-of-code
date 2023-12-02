with open("puzzle_input.txt") as f:
    content = f.readlines()


def check_minimum_number_of_cubes(games_string):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    games = games_string.split(";")
    for game in games:
        game = game.strip()
        for num_of_cubes in game.split(", "):
            number, colour = num_of_cubes.strip().split(" ")
            number = int(number)
            if number > min_cubes[colour]:
                min_cubes[colour] = number
    (a, b, c) = min_cubes.values()
    return a * b * c


total = 0
for row in content:
    _, games_string = row.split(":")
    total += check_minimum_number_of_cubes(games_string)

print(total)
