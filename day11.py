import day11in

def DictPosSeat(strIn):
    dictPosSeat = {}

    for y, strLine in enumerate(strIn.split('\n')):
        for x, seat in enumerate(strLine):
            dictPosSeat[(x,y)] = seat

    return dictPosSeat

def LSeatAdjacent(pos, dictPosSeat):
    lSeat = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            posOther = (pos[0] + dx, pos[1] + dy)
            lSeat.append(dictPosSeat.get(posOther, '.'))    # treat off the edge as floor

    return lSeat

def DictPosSeatReseat(dictPosSeatSrc):
    dictPosSeatDst = {}

    for pos, seat in dictPosSeatSrc.items():
        # figure out what to put in the dst dictionary at this position

        seatNext = seat
        if seat == '.':
            seatNext = seat
        elif seat == 'L':
            lSeat = LSeatAdjacent(pos, dictPosSeatSrc)
            if '#' not in lSeat:
                seatNext = '#'
            else:
                seatNext = 'L'
        elif seat == '#':
            lSeat = LSeatAdjacent(pos, dictPosSeatSrc)
            if len([x for x in lSeat if x == '#']) >= 4:
                seatNext = 'L'
            else:
                seatNext = '#'

        dictPosSeatDst[pos] = seatNext

    return dictPosSeatDst

def AreSeatsIdentical(dictPosSeat0, dictPosSeat1):

    for pos, seat in dictPosSeat0.items():
        if dictPosSeat1[pos] != seat:
            return False

    return True

def LSeatAdjacent2(pos, dictPosSeat):
    lSeat = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            posOther = pos
            while True:
                posOther = (posOther[0] + dx, posOther[1] + dy)
                seat = dictPosSeat.get(posOther, '')
                if seat == '':
                    lSeat.append('.')
                    break
                elif seat != '.':
                    lSeat.append(seat)
                    break

    return lSeat

def DictPosSeatReseat2(dictPosSeatSrc):
    dictPosSeatDst = {}

    for pos, seat in dictPosSeatSrc.items():
        # figure out what to put in the dst dictionary at this position

        seatNext = seat
        if seat == '.':
            seatNext = seat
        elif seat == 'L':
            lSeat = LSeatAdjacent2(pos, dictPosSeatSrc)
            if '#' not in lSeat:
                seatNext = '#'
            else:
                seatNext = 'L'
        elif seat == '#':
            lSeat = LSeatAdjacent2(pos, dictPosSeatSrc)
            if len([x for x in lSeat if x == '#']) >= 5:
                seatNext = 'L'
            else:
                seatNext = '#'

        dictPosSeatDst[pos] = seatNext

    return dictPosSeatDst

def Part1():
    # load initial seating arrangement

    dictPosSeatCur = DictPosSeat(day11in.strIn)

    cIter = 0
    while True:
        # make next arrangement by apply rules to current one

        dictPosSeatNext = DictPosSeatReseat(dictPosSeatCur)
        cIter += 1

        # terminate when next arrangement is current arrangement

        if AreSeatsIdentical(dictPosSeatCur, dictPosSeatNext):
            break

        dictPosSeatCur = dictPosSeatNext

    cSeat = len([x for x in dictPosSeatCur.values() if x == '#'])

    print("Part 1:", cSeat, cIter)

def Part2():
    # load initial seating arrangement

    dictPosSeatCur = DictPosSeat(day11in.strIn)

    cIter = 0
    while True:
        # make next arrangement by apply rules to current one

        dictPosSeatNext = DictPosSeatReseat2(dictPosSeatCur)
        cIter += 1

        # terminate when next arrangement is current arrangement

        if AreSeatsIdentical(dictPosSeatCur, dictPosSeatNext):
            break

        dictPosSeatCur = dictPosSeatNext

    cSeat = len([x for x in dictPosSeatCur.values() if x == '#'])

    print("Part 2:", cSeat, cIter)

if __name__ == '__main__':
    Part1()
    Part2()
