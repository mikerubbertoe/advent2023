import re

def part1():
    seeds = []
    mapped = []
    readyToMap = False
    with open("day5_input.txt") as f:
        for line in f:
            if not seeds:
                seeds = re.findall('\d+', line)
            elif 'map' in line:
                readyToMap = True
                mapped = [False for x in seeds]
            elif not line or line == '\n':
                readyToMap = False
                continue
            elif readyToMap:
                dest, source, step = re.findall('\d+', line)
                dest, source, step = int(dest), int(source), int(step)

                for i in range(len(seeds)):
                    if not mapped[i] and source <= int(seeds[i]) and int(seeds[i]) <= source + step - 1:
                        seeds[i] = int(seeds[i]) + (dest - source)
                        mapped[i] = True
        print(sorted(seeds)[0])


def part2():
    seeds = dict()
    conversions = []
    readyToMap = False
    with open("day5_input.txt") as f:
        for line in f:
            if not seeds:
                seedRanges = re.findall('\d+', line)
                for i in range(0, len(seedRanges), 2):
                    seeds[int(seedRanges[i])] = int(seedRanges[i]) + int(seedRanges[i + 1]) - 1
            elif 'map' in line:
                readyToMap = False
                conversions = []
            elif line != '\n':
                dest, source, step = re.findall('\d+', line)
                conversions.append((int(dest), int(source), int(step)))
            elif line == '\n' and conversions:
                readyToMap = True

            if readyToMap:
                newSeeds = dict()
                for c in conversions:
                    dest, source, step = c
                    allSeeds = list(seeds.items())
                    while len(allSeeds) > 0:
                        start, end = allSeeds.pop()
                        if  source <= start and (source + step) - 1 >= end:
                            newStart = start + (dest - source)
                            newEnd = end + (dest - source)
                            newSeeds[newStart] = newEnd
                            newSeeds.pop(start, None)
                            seeds.pop(start)
                        elif source >= start and source <= end and (source + step) - 1 >= end:
                            #start .. source - 1 if start != source else start
                            newStart = dest
                            newEnd = end + (dest - source)
                            newSeeds[newStart] = newEnd
                            newSeeds.pop(start, None)
                            seeds[start] = source - 1 if start != source else start
                            allSeeds.append((start, source - 1))

                        elif source <= start and start <= (source + step) - 1 and end >= (source + step) - 1:
                            #source + step .. end
                            newStart = start + (dest - source)
                            newEnd = dest + step - 1
                            newSeeds[newStart] = newEnd
                            seeds.pop(start)
                            newSeeds.pop(start, None)
                            seeds[source + step] = end
                            allSeeds.append((source + step, end))

                        elif source >= start and (source + step) - 1 <= end:

                            #start..source - 1 if start != source else start
                            # source + step ..
                            newStart = dest
                            newEnd = dest + step - 1
                            newSeeds[newStart] = newEnd
                            seeds[start] = source - 1 if start != source else start
                            seeds[source + step] = end
                            newSeeds.pop(start, None)
                            allSeeds.append((start, source - 1))
                            allSeeds.append((source + step, end))

                        else:
                            newSeeds[start] = end

                seeds = newSeeds

    print(sorted(seeds.items())[0][0])
part1()
part2()