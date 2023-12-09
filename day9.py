import re

def part1and2():
    with open("day9_input.txt", 'r') as f:
        startTotal, endTotal = 0, 0
        for line in f:
            firstValue, lastValue = [], []
            history = re.findall('([-]?\d+)', line)
            finished = False

            firstValue.append(int(history[0]))
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
                firstValue.append(history[0])

            startTotal += sum(lastValue)
            extrapolation = firstValue.pop()
            while len(firstValue) > 0:
                extrapolation = firstValue.pop() - extrapolation
            endTotal += extrapolation

    print(startTotal)
    print(endTotal)

part1and2()
