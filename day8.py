import re
import math

def part1():
    index = 0
    steps = 0
    instructions = []
    path = dict()
    with open("day8_input.txt", 'r') as f:
        for line in f:
            if not instructions:
                instructions = [x for x in line.strip()]
            elif line != '\n':
                current, left, right = re.findall('([A-Z0-9]{3})', line)
                path[current] = (left, right)
        size = len(instructions)
        current = 'AAA'
        while current != 'ZZZ':
            nextInstruction = instructions[index]
            index = (index + 1) % size
            current = path[current][0] if nextInstruction == 'L' else path[current][1]
            steps += 1
        print(steps)


def part2():
    instructions = []
    currents = []
    leastCommon = 1
    path = dict()
    with open("day8_input.txt", 'r') as f:
        for line in f:
            if not instructions:
                instructions = [x for x in line.strip()]
            elif line != '\n':
                current, left, right = re.findall('([A-Z0-9]{3})', line)
                path[current] = (left, right)
                if current.endswith('A'):
                    currents.append(current)

        size = len(instructions)
        for current in currents:
            steps = 0
            index = 0
            while not current.endswith('Z'):
                nextInstruction = instructions[index]
                index = (index + 1) % size
                current = path[current][0] if nextInstruction == 'L' else path[current][1]
                steps += 1
            leastCommon = abs(leastCommon * steps) // math.gcd(leastCommon, steps)
        print(leastCommon)


part1()
part2()