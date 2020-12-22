# day 13 problem solutions

import day13in

def MpFactorC(n):
    mpFactorC = {}
    factor = 2
    while n >= factor:
        if n % factor == 0:
            # divide out this factor and count it
            n //= factor
            c = mpFactorC.get(factor, 0) + 1
            mpFactorC[factor] = c
        else:
            # move on to the next factor
            factor += 1

    return mpFactorC

def LCM(a, b):
    mpFactorCA = MpFactorC(a)
    mpFactorCB = MpFactorC(b)

    lcm = 1
    setFactor = set(mpFactorCA.keys())
    setFactor |= set(mpFactorCB.keys())
    for factor in setFactor:
        c = max(mpFactorCA.get(factor, 1), mpFactorCB.get(factor, 1))
        lcm *= factor ** c

    return lcm

class Schedule:
    def __init__(self, strIn):
        strTime, strBus = strIn.split('\n')
        self.m_time = int(strTime)
        self.m_lBus = strBus.split(',') # NOTE: strings, includes x's, yuck...?

    def StrFindNextBus(self):
        # use modular arithmetic to figure out how long until each bus arrives
        dMinBest = None
        busBest = None
        for bus in self.m_lBus:
            if bus == 'x':
                continue

            bus = int(bus)
            dMin = (bus - (self.m_time % bus)) % bus    # delta = bus - time % bus, but delta bus = 0

            if dMinBest is None or dMin < dMinBest:
                dMinBest = dMin
                busBest = bus

        return "{a} (from {b} in {m} min)".format(a=busBest*dMinBest, b=busBest, m=dMinBest)

    def StrFindPatternBus(self):
        # find the lowest time t where self.m_lBus[i] leaves at t+i, and x doesn't matter, and other
        #  busses also leaving doesn't matter

        # e.g., t+n % lBus[n] == 0

        # idea: if I calculate a t that works for lBus[n], all t values that are bigger by multiples
        #  of lBus[n] will work for lBus[n].
        # method: once I've found a starting value, then add multiples of that bus until I can find one
        #  that works for the next bus. Then, add the product of those two busses (well, their LCM) until
        #  I find one that works for the next bus, and so forth, until all busses are satisfied.

        tSearch = 0
        dT = 1
        cIter = 0
        for i, n in enumerate(self.m_lBus):
            if n == 'x':
                continue
            n = int(n)
            while (tSearch + i) % n != 0:
                cIter += 1
                tSearch += dT

            dT = LCM(dT, n)

        # debug sanity check

        for i, n in enumerate(self.m_lBus):
            if n == 'x':
                continue
            print("  DEBUG: t = {t} + {i} % {b} = {r}".format(t=tSearch, i=i, b=n, r=(tSearch + i) % int(n)))

        return "{t} satisfies, found in {n} iterations".format(t=tSearch, n=cIter)

def Part1():
    sched = Schedule(day13in.strIn)
    print("Part 1:", sched.StrFindNextBus())

def Part2():
    sched = Schedule(day13in.strIn)
    print("Part 2:", sched.StrFindPatternBus())

if __name__ == '__main__':
    Part1()
    Part2()
