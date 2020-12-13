import day7in

# day 7 solutions

def MpBagHeldByBag(strIn):
    """This function parses strIn and returns a dictionary whose keys are bag types and
    whose values are sets of bag types that can hold the key bag directly"""

    mpBagHeld = {}

    for strRule in strIn.split('\n'):
        strLeft, strRight = strRule.split(' contain ')

        strHolder = strLeft
        if strHolder.endswith('s'):
            strHolder = strHolder[:-1]

        lStrHeld = strRight.split(', ')
        for strHeld in lStrHeld:
            strHeld = strHeld.replace('.', '')
            if strHeld.endswith('s'):
                strHeld = strHeld[:-1]

            lStr = strHeld.split(' ')
            if len(lStr) == 3:
                strHeld = ' '.join(lStr)
            elif len(lStr) == 4:
                strHeld = ' '.join(lStr[1:])
            else:
                print("WAUGH! Got a held bag of '{x}'".format(x=strHeld))

            if strHeld not in mpBagHeld:
                mpBagHeld[strHeld] = set()

            mpBagHeld[strHeld].add(strHolder)

    return mpBagHeld

def MpBagHolds(strIn):
    """This function parses strIn and returns a dictionary whose keys are bag types and
    whose values are lists of counts of other bag types that they contain"""

    mpBagHolds = {}

    for strRule in strIn.split('\n'):
        strLeft, strRight = strRule.split(' contain ')

        strHolder = strLeft
        if strHolder.endswith('s'):
            strHolder = strHolder[:-1]

        mpBagHolds[strHolder] = []

        lStrHeld = strRight.split(', ')
        for strHeld in lStrHeld:
            strHeld = strHeld.replace('.', '')
            if strHeld.endswith('s'):
                strHeld = strHeld[:-1]

            lStr = strHeld.split(' ')
            if len(lStr) == 3:
                continue
            elif len(lStr) == 4:
                cBag = int(lStr[0])
                strHeld = ' '.join(lStr[1:])
                mpBagHolds[strHolder].append((cBag, strHeld))
            else:
                print("WAUGH! Got a held bag of '{x}'".format(x=strHeld))

    return mpBagHolds

def Part1():
    mpBagHeld = MpBagHeldByBag(day7in.strIn)

    # figure out how many bags can hold, in some way, a shiny gold bag

    setAncestor = set()
    setCheck = mpBagHeld.get('shiny gold bag', set())

    while setCheck:
        bag = setCheck.pop()
        setAncestor.add(bag)

        setCheck |= mpBagHeld.get(bag, set())
        setCheck.difference_update(setAncestor)

    print("Part 1:", len(setAncestor))

def CBagsInBag(bag, mpBagHolds):

    lHold = mpBagHolds[bag]
    cBagTotal = 0
    for cBag, bag in lHold:
        cBagSub = CBagsInBag(bag, mpBagHolds)
        cBagTotal += cBagSub * cBag + cBag

    return cBagTotal

def Part2():
    mpBagHolds = MpBagHolds(day7in.strIn)

    # figure out how many bags are held inside a shiny gold bag, total, including
    #  bags (by their count) and any bags held inside them, etc.

    cBagTotal = CBagsInBag('shiny gold bag', mpBagHolds)

    print("Part 2:", cBagTotal)

if __name__ == '__main__':
    Part1()
    Part2()
