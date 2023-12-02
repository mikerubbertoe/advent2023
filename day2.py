import re

def part1():
    color_pattern = '(\d+) (green|blue|red)'
    game_pattern = 'Game (\d+)'
    answer = 0
    possible = True
    with open("day2_input.txt") as f:
        for line in f:
            gameNum = int(re.findall(game_pattern, line)[0])
            subgames = line.split(';')
            for game in subgames:
                possible = True
                totals = {'red': 0, 'green': 0, 'blue': 0}
                counts = re.findall(color_pattern, game)

                for couple in counts:
                    totals[couple[1]] += int(couple[0])
                if totals['red'] > 12 or totals['green'] > 13 or totals['blue'] > 14:
                    possible = False
                    break
            if possible:
                answer += gameNum
    print(answer)

def part2():
    color_pattern = '(\d+) (green|blue|red)'
    answer = 0

    with open("day2_input.txt") as f:
        for line in f:
            max_red, max_green, max_blue = 0, 0, 0
            subgames = line.split(';')
            for game in subgames:
                totals = {'red': 0, 'green': 0, 'blue': 0}
                counts = re.findall(color_pattern, game)

                for couple in counts:
                    totals[couple[1]] += int(couple[0])

                max_red = max(max_red, totals['red'])
                max_green = max(max_green, totals['green'])
                max_blue = max(max_blue, totals['blue'])
            mult = max_red * max_green * max_blue
            answer += mult

    print(answer)
    
part1()
part2()