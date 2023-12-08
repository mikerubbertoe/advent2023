from collections import defaultdict

cardValues = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2
}
wildJokers = False

def jokerCardValue(cards):
    numJokers = cards.count('J')
    if numJokers > 0:
        newValue = '2'
        jokerlessCards = cards.replace('J', '')
        maxOccurence = 0
        maxValues = ['A']
        for x in set(jokerlessCards):
            if jokerlessCards.count(x) >= maxOccurence:
                if jokerlessCards.count(x) == maxOccurence:
                    maxValues.append(x)
                else:
                    maxValues = [x]
                maxOccurence = jokerlessCards.count(x)

        if len(maxValues) == 1:
            newValue = maxValues[0]
        else:
            for x in maxValues:
                newValue = newValue if cardValues[newValue] > cardValues[x] else x
        cards = cards.replace('J', newValue)
    return cards

def compare(a, b):
    tempA = a
    tempB = b
    if wildJokers:
        a = jokerCardValue(a)
        b = jokerCardValue(b)
        cardValues['J'] = 0

    aMap, bMap = defaultdict(int), defaultdict(int)

    for i in range(len(a)):
        aMap[a[i]] += 1
        bMap[b[i]] += 1

    aValues = sorted(aMap.values(), reverse=True)
    bValues = sorted(bMap.values(), reverse=True)

    #if A or B has a pair of 5
    if aValues[0] == 5 or bValues[0] == 5:
        if aValues[0] == 5 and bValues[0] == 5:
            return sameHandCompare(tempA, tempB)
        return tempA if aValues[0] == 5 else tempB

    #if A or B has a pair of 4
    elif aValues[0] == 4 or bValues[0] == 4:
        if aValues[0] == 4 and bValues[0] == 4:
            return sameHandCompare(tempA, tempB)
        return tempA if aValues[0] == 4 else tempB

    #if A or B has a full house
    elif (aValues[0] == 3 and aValues[1] == 2) or (bValues[0] == 3 and bValues[1] == 2):
        if (aValues[0] == 3 and aValues[1] == 2) and (bValues[0] == 3 and bValues[1] == 2):
            return sameHandCompare(tempA, tempB)
        return tempA if aValues[0] == 3 and aValues[1] == 2 else tempB

    elif aValues[0] > bValues[0] or bValues[0] > aValues[0]:
        return tempA if aValues[0] > bValues[0] else tempB

    #if A or B has 2 pair
    elif (aValues[0] == 2 and aValues[1] == 2) or (bValues[0] == 2 and bValues[1] == 2):
        if (aValues[0] == 2 and aValues[1] == 2) and (bValues[0] == 2 and bValues[1] == 2):
            return sameHandCompare(tempA, tempB)
        return tempA if aValues[0] == 2 and aValues[1] == 2 else tempB

    #if same hand strength
    elif sorted(aMap.values(), reverse=True)[0] == sorted(bMap.values(), reverse=True)[0]:
        return sameHandCompare(tempA, tempB)

    else:
        return tempA

def sameHandCompare(a, b):
    for i in range(len(a)):
        if cardValues[a[i]] == cardValues[b[i]]:
            continue
        else:
            return a if cardValues[a[i]] > cardValues[b[i]] else b
    return

def part1():
    hands = []
    with open("day7_input.txt") as f:
        for line in f:
            s = line.split(' ')
            cards = s[0]
            bet = int(s[1].strip())
            hands.append((cards, bet))

    for step in range(1, len(hands)):
        key = hands[step]
        j = step - 1

        while j >= 0 and key[0] != compare(key[0], hands[j][0]):
            hands[j + 1] = hands[j]
            j = j - 1

        hands[j + 1] = key

    sum = 0
    for i in range(len(hands)):
        sum += ((i  + 1) * hands[i][1])
    print(sum)


def part2():

    hands = []
    with open("day7_input.txt") as f:
        for line in f:
            s = line.split(' ')
            cards = s[0]
            bet = int(s[1].strip())
            hands.append((cards, bet))

    for step in range(1, len(hands)):
        key = hands[step]
        j = step - 1

        while j >= 0 and key[0] != compare(key[0], hands[j][0]):
            hands[j + 1] = hands[j]
            j = j - 1

        hands[j + 1] = key
    print(hands)
    sum = 0
    for i in range(len(hands)):
        sum += ((i + 1) * hands[i][1])
    print(sum)

#part1()
wildJokers = True
part2()
#print(compare("QQQQ2", "QJJQ2"))
