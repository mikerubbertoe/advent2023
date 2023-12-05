import re
import math

# numWinningNumbers = 5
numWinningNumbers = 10


def part1():
    total = 0
    for line in i.split('\n'):
        winners = set()
        exp = -1
        nums = re.findall('\d+', line)
        for x in range(1, len(nums)):
            if x <= numWinningNumbers:
                winners.add(int(nums[x]))
            else:
                if int(nums[x]) in winners:
                    exp += 1
        total += math.pow(2, exp) if exp >= 0 else 0
    print(total)


def part2():
    total = 0
    punchcards = {}
    for line in i.split('\n'):
        winners = set()
        numWinners = 0
        nums = re.findall('\d+', line)
        cardNum = 0
        for x in range(0, len(nums)):
            if x == 0:
                cardNum = int(nums[x])
                if cardNum not in punchcards:
                    punchcards[cardNum] = 1

            elif x <= numWinningNumbers:
                winners.add(int(nums[x]))
            else:
                if int(nums[x]) in winners:
                    numWinners += 1

        for y in range(cardNum + 1, cardNum + numWinners + 1):
            punchcardTotal = punchcards.setdefault(y, 1)
            punchcards[y] = punchcardTotal + punchcards[cardNum]

    print(sum(punchcards.values()))


part1()
part2()