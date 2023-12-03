symbols = set()

def part1():
    total = 0
    schematic = createMap()
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x] in symbols:
                total += find_adjacent_numbers(schematic, x, y)
    print(total)

def part2():
    total = 0
    schematic = createMap()
    symbols = set().add('*')
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x] in symbols:
                total += find_adjacent_numbers(schematic, x, y)
    print(total)

def find_adjacent_numbers(schematic, x, y):
    total = set()

    if schematic[y + 1][x + 1].isdigit():
        total.add(getNumber(schematic, x + 1, y + 1))
    if schematic[y + 1][x].isdigit():
        total.add(getNumber(schematic, x, y + 1))
    if schematic[y + 1][x - 1].isdigit():
        total.add(getNumber(schematic, x - 1, y + 1))
    if schematic[y][x - 1].isdigit():
        total.add(getNumber(schematic, x - 1, y ))
    if schematic[y - 1][x - 1].isdigit():
        total.add(getNumber(schematic, x - 1, y - 1))
    if schematic[y - 1][x].isdigit():
        total.add(getNumber(schematic, x, y - 1))
    if schematic[y - 1][x + 1].isdigit():
        total.add(getNumber(schematic, x + 1, y - 1))
    if schematic[y][x + 1].isdigit():
        total.add(getNumber(schematic, x + 1, y))

    if len(total) == 2:
        return total.pop() * total.pop()
    return 0

def getNumber(schematic, x, y):
    tempX = x + 1
    number = schematic[y][x]
    while tempX < len(schematic[y]) and schematic[y][tempX] != '.' and schematic[y][tempX] not in symbols:
        number += schematic[y][tempX]
        tempX += 1
    tempX = x - 1
    while tempX >= 0 and schematic[y][tempX] != '.' and schematic[y][tempX] not in symbols:
        number = schematic[y][tempX] + number
        tempX -= 1
    return int(number)

def createMap():
    schematic = []
    with open('day3_input.txt', 'r') as f:
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                row.append(char)
                if char != '.' and not char.isdigit():
                    symbols.add(char)
            schematic.append(row)

    print(symbols)
    return schematic

part1()