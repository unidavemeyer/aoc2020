import day6in

# day 6 problems

class Declaration:
    def __init__(self, strIn):
        self.m_lSetYes = []         # sets of yesses per person
        self.m_setYes = set()       # whole group set of yesses (anyone said yes)
        self.m_setYesAll = set()    # questions that everyone answered yes to

        for strLine in strIn.split('\n'):
            self.m_lSetYes.append(set([x for x in strLine]))
            self.m_setYes |= self.m_lSetYes[-1]

        self.m_setYesAll = self.m_lSetYes[0]
        for setYes in self.m_lSetYes[1:]:
            self.m_setYesAll &= setYes

def Part1():
    # load sets of questions for each group

    lDecl = []
    for strGroup in day6in.strIn.split('\n\n'):
        lDecl.append(Declaration(strGroup))

    # report sum of questions yes for each group

    cQuestion = 0
    for decl in lDecl:
        cQuestion += len(decl.m_setYes)

    print("Part 1:", cQuestion, " questions yes")

def Part2():
    # load sets of questions for each group

    lDecl = []
    for strGroup in day6in.strIn.split('\n\n'):
        lDecl.append(Declaration(strGroup))

    # report sum of questions yes for each group

    cQuestion = 0
    for decl in lDecl:
        cQuestion += len(decl.m_setYesAll)

    print("Part 2:", cQuestion, "questions yes all")

if __name__ == '__main__':
    Part1()
    Part2()
