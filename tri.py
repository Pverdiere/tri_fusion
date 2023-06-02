import random
import math


def gogeta(list):
    if len(list) > 1:
        part1 = list[0:math.floor(len(list)/2)]
        part2 = list[math.floor(len(list)/2):len(list)]

        part1Tri = gogeta(part1)
        part2Tri = gogeta(part2)

        newList = []

        for i in range(len(list)):
            if len(part1Tri) == 0:
                newList.append(part2Tri[0])
                part2Tri.remove(part2Tri[0])
            elif len(part2Tri) == 0:
                newList.append(part1Tri[0])
                part1Tri.remove(part1Tri[0])
            elif part1Tri[0] < part2Tri[0]:
                newList.append(part1Tri[0])
                part1Tri.remove(part1Tri[0])
            else:
                newList.append(part2Tri[0])
                part2Tri.remove(part2Tri[0])
        list = newList
    return list


tab = []

for i in range(51):
    tab.append(random.randrange(800))

print(tab)

print(gogeta(tab))