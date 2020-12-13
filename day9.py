# day 9 solutions

import day9in

class Xmas:
    def __init__(self, strIn):
        self.m_lNum = []
        for strLine in strIn.split('\n'):
            self.m_lNum.append(int(strLine))

    def IsValidEntry(self, iNum, cPrev):

        # extract the window of numbers to check

        lNumPrev = self.m_lNum[iNum - cPrev:iNum]
        assert(len(lNumPrev) == cPrev)

        # convert to counts by number for (a) fast lookup and (b) multiple instance tracking

        mpNumPrevC = {}
        for numPrev in lNumPrev:
            cPrev = mpNumPrevC.get(numPrev, 0) + 1
            mpNumPrevC[numPrev] = cPrev

        # check if any paring exists in the previous numbers to get the current one

        num = self.m_lNum[iNum]
        for numPrev, cPrev in mpNumPrevC.items():
            numOther = num - numPrev
            if numOther not in mpNumPrevC:
                continue
            if numPrev != numOther:
                # found a pair that works
                return True
            elif numPrev == numOther and cPrev > 1:
                # found a pair of identical values that works
                return True

        return False

    def LNumFindSum(self, numFind):

        for iNumFirst in range(len(self.m_lNum)):
            # scan the contiguous range starting at iNumFirst
            numSum = self.m_lNum[iNumFirst]
            iNumLast = iNumFirst

            while iNumLast < len(self.m_lNum):
                iNumLast += 1
                numSum += self.m_lNum[iNumLast]
                if numSum == numFind:
                    return self.m_lNum[iNumFirst:iNumLast+1]
                elif numSum > numFind:
                    break

        # sad panda

        return []

def Part1():
    # check for errors in XMAS encoding - valid if number is sum of two distinct elements of previous 25 numbers
    #  (but sample data is done with window of 5 instead of 25)

    xmas = Xmas(day9in.strIn)

    cNumWindow = 25
    iNum = cNumWindow
    cNum = len(xmas.m_lNum)

    while iNum < cNum:
        if not xmas.IsValidEntry(iNum, cNumWindow):
            break
        iNum += 1

    print("Part 1: Invalid:", xmas.m_lNum[iNum], "(entry at", iNum, ")")

def Part2():
    # find contiguous range of numbers that sum to a given value, and then report the sum of the smallest and largest
    #  values in that range

    numFind = 257342611

    xmas = Xmas(day9in.strIn)
    lNum = xmas.LNumFindSum(numFind)

    numMin = lNum[0]
    numMax = lNum[0]
    for num in lNum[1:]:
        numMin = min(num, numMin)
        numMax = max(num, numMax)

    print("Part 2: Sum:", numMin + numMax, "from", numMin, numMax)

if __name__ == '__main__':
    Part1()
    Part2()
