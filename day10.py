# day 10 problem

import day10in

import time

def LJolt(strIn):
    lJolt = []
    for strLine in strIn.split('\n'):
        lJolt.append(int(strLine))

    return lJolt

def Part1():
    lJolt = LJolt(day10in.strIn)

    # figure out all the jolt differences:
    #  - sort the jolts from smallest to biggest
    #  - compute pair-wise deltas and sum those

    lJolt.sort()

    joltPrev = 0
    difference1 = 0
    difference2 = 0
    difference3 = 0
    for jolt in lJolt:
        diff = jolt - joltPrev
        if diff == 1:
            difference1 += 1
        elif diff == 2:
            difference2 += 1
        elif diff == 3:
            difference3 += 1
        joltPrev = jolt

    # device is always 3 jolts higher

    difference3 += 1

    print("Part 1:", difference1, '*', difference3, '=', difference1 * difference3)

def CComboCompute(joltStart, joltEnd, lJolt):

    cCombo = 0
    for iJolt in range(min(3, len(lJolt))):
        if lJolt[iJolt] - joltStart < 4:
            cCombo += CComboCompute(lJolt[iJolt], joltEnd, lJolt[iJolt+1:])

    if joltEnd - joltStart < 4:
        cCombo += 1

    return cCombo

class Combo:
    def __init__(self):
        self.m_dictStartCCombo = {}

    def Compute(self, joltStart, joltEnd, lJolt):
        if joltStart in self.m_dictStartCCombo:
            return self.m_dictStartCCombo[joltStart]

        cCombo = 0
        for iJolt in range(min(3, len(lJolt))):
            if lJolt[iJolt] - joltStart < 4:
                cCombo += self.Compute(lJolt[iJolt], joltEnd, lJolt[iJolt+1:])

        if joltEnd - joltStart < 4:
            cCombo += 1

        self.m_dictStartCCombo[joltStart] = cCombo

        return cCombo

def Part2():
    # count up the number of legal combos that link 0 and the device (= highest adapter + 3)

    lJolt = LJolt(day10in.strIn)
    lJolt.sort()

    joltStart = 0
    joltEnd = lJolt[-1] + 3

    # attempt divide and conquer with recursion

    # Part 2: 19208 in 0.0458223819732666 - original version

    # tStart = time.time()
    # cCombo = CComboCompute(joltStart, joltEnd, lJolt)
    # tEnd = time.time()

    # Part 2: 19208 in 5.1021575927734375e-05 - remembered combo version

    tStart = time.time()
    combo = Combo()
    cCombo = combo.Compute(joltStart, joltEnd, lJolt)
    tEnd = time.time()

    print("Part 2:", cCombo, "in", tEnd - tStart)

if __name__ == '__main__':
    Part1()
    Part2()
