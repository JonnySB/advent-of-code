with open("puzzle_input.txt") as f:
    content = f.readlines()

max_cubes = {"red": 12, "green": 13, "blue": 14}


def check_game(games_string):
    print(games_string)
    games = games_string.split(";")
    for game in games:
        game = game.strip()
        print(game)
        for cubes in game.split(", "):
            print(cubes)
            number, colour = cubes.split(" ")
            if int(number) > max_cubes[colour]:
                print("NOOOO", colour, number)
                return False
    return True


total = 0
for row in content:
    game_num, games_string = row.split(":")
    game_num = int(game_num[5:])
    if check_game(games_string):
        total += game_num
        print(total)

print(total)
