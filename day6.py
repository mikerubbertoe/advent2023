import re
import math

inp = """Time:        54     81     70     88
Distance:   446   1292   1035   1007"""


def part1():
    lines = inp.split('\n')
    time = re.findall('\d+', lines[0])
    dist = re.findall('\d+', lines[1])
    total = 1

    for i in range(len(time)):
        t = int(time[i])
        goal = int(dist[i])
        speed = 0
        scenarios = 0
        for speed in range(t + 1):
            dist_traveled = speed * (t - speed)
            # print(dist_traveled)
            if dist_traveled > goal:
                scenarios += 1
        total = total * scenarios if scenarios > 0 else total
    print(total)


def part2():
    lines = inp.split('\n')
    time = ''
    dist = ''

    for t in re.findall('\d+', lines[0]):
        time += t
    for d in re.findall('\d+', lines[1]):
        dist += d

    time = int(time)
    dist = int(dist)
    speed = int(math.floor(dist / time))
    scenarios = 0

    for s in range(speed, time + 1, 1):
        dist_traveled = s * (time - s)
        if dist_traveled > dist:
            scenarios += 1

    print(scenarios)


part1()
part2()