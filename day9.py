import re

def part1():
    with open("day9_input.txt", 'r') as f:
        total = 0
        for line in f:
            lastValue = []
            history = re.findall('([-]?\d+)', line)
            finished = False
            lastValue.append(int(history[-1]))
            while not finished:
                nextHistory = []

                finished = True
                for i in range(len(history) - 1):
                    difference = int(history[i+1]) - int(history[i])
                    nextHistory.append(difference)
                    if difference != 0:
                        finished = False
                history = nextHistory
                lastValue.append(history[-1])
                #print(history)
            total += sum(lastValue)
    print(total)

def part2():
    with open("day9_input.txt", 'r') as f:
        total = 0
        for line in f:
            firstValue = []
            history = re.findall('([-]?\d+)', line)
            finished = False
            firstValue.append(int(history[0]))
            while not finished:
                nextHistory = []

                finished = True
                for i in range(len(history) - 1):
                    difference = int(history[i+1]) - int(history[i])
                    nextHistory.append(difference)
                    if difference != 0:
                        finished = False
                history = nextHistory
                firstValue.append(history[0])

            extrapolation = firstValue.pop()
            while len(firstValue) > 0:
                extrapolation = firstValue.pop() - extrapolation
            total += extrapolation

    print(total)

#part1()
part2()