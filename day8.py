# day 8 solution

import day8in

# game console emulator

class Emulator:
    def __init__(self, strIn):
        """Set up the emulator to run the given set of instructions"""

        self.m_lLine = []
        self.m_acc = 0
        self.m_iLine = 0
        self.m_fTerminated = False

        self.Load(strIn)

        # set up instruction execution tables

        self.m_mpOpFn = {
            'acc' : self.Acc,
            'jmp' : self.Jmp,
            'nop' : self.Nop,
        }

    def Load(self, strIn):
        """Load the given input string in as instructions for the emulator"""

        for strLine in strIn.split('\n'):
            op, arg = strLine.split(' ')
            self.m_lLine.append((op, int(arg)))

    def Acc(self):
        """Adds argument to the accumulator and goes to the next line"""

        self.m_acc += self.m_lLine[self.m_iLine][1]
        self.m_iLine += 1

    def Jmp(self):
        """Adds the argument to the line index"""

        self.m_iLine += self.m_lLine[self.m_iLine][1]

    def Nop(self):
        """Does nothing other than increment the line index"""

        self.m_iLine += 1

    def Step(self):

        if self.m_iLine == len(self.m_lLine):
            self.m_fTerminated = True
            return
        elif self.m_iLine < 0 or self.m_iLine > len(self.m_lLine):
            print("WAUGH: Ran off instruction space, line was:", self.m_iLine)
            return

        op = self.m_lLine[self.m_iLine][0]
        fn = self.m_mpOpFn.get(op, None)
        if fn is None:
            print("WAUGH: Unknown op", op, "encountered on line", self.m_iLine)
            return

        fn()

def Part1():
    em = Emulator(day8in.strIn)
    setLine = set()
    cStep = 0
    while True:
        if em.m_iLine in setLine:
            # found duplicate instruction
            break
        setLine.add(em.m_iLine)
        em.Step()
        cStep += 1

    print("Part 1:", em.m_acc, " (in", cStep, "steps)")

def Part2():
    # change one nop to jmp, or one jmp to nop, so that the program "terminates" by
    #  trying to execute one past the end of the instruction stream

    # method: brute force of part 1, ish -- try iteratively changing each nop to jmp or
    #  vice versa, and check if the program terminates or loops; if the former, report
    #  the accumulator and stop; if the latter, give up on that iteration

    emBase = Emulator(day8in.strIn)

    cStep = 0       # just my curiosity
    cAttempt = 0    #  ...

    for iLine in range(len(emBase.m_lLine)):
        op = emBase.m_lLine[iLine][0]
        if op != 'nop' and op != 'jmp':
            # no instruction to change, don't bother trying this iteration
            continue

        # generate new emulator, but change iLine's op to the other

        em = Emulator(day8in.strIn)
        em.m_lLine[iLine] = ('nop' if op == 'jmp' else 'jmp', em.m_lLine[iLine][1])
        cAttempt += 1

        # run the emulator until termination or duplicate iLine

        setLine = set()
        while True:
            if em.m_fTerminated:
                # program terminated
                break
            if em.m_iLine in setLine:
                # found duplicate instruction
                break
            setLine.add(em.m_iLine)
            em.Step()
            cStep += 1

        if em.m_fTerminated:
            break

    print("Part 2:", em.m_acc, "(after", cAttempt, "attempts for", cStep, "steps)")

if __name__ == '__main__':
    Part1()
    Part2()
