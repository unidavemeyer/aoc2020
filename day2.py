import day2in

class Entry:
    def __init__(self, strIn):
        self.m_strPass = None
        self.m_ch = None
        self.m_cChMin = 0
        self.m_cChMax = 0

        self.ParseLine(strIn)

    def ParseLine(self, strIn):
        # line looks like this: min-max letter: password

        lStr = strIn.split(':')
        self.m_strPass = lStr[1].strip()
        strRule = lStr[0].strip()

        lStr = strRule.split(' ')
        self.m_ch = lStr[1]
        strRange = lStr[0]

        lStr = strRange.split('-')
        self.m_cChMin = int(lStr[0])
        self.m_cChMax = int(lStr[1])

    def FIsValid(self):

        # calculate the count of letters we care about

        cCh = 0
        for ch in self.m_strPass:
            if ch == self.m_ch:
                cCh += 1

        # check if the count of letters is invalid

        if cCh < self.m_cChMin:
            return False

        if cCh > self.m_cChMax:
            return False

        return True

    def FIsValid2(self):

        cChMatch = 0

        # check characters

        for iCh in [self.m_cChMin, self.m_cChMax]:
            if iCh <= len(self.m_strPass):
                if self.m_strPass[iCh - 1] == self.m_ch:
                    cChMatch += 1

        return cChMatch == 1

def Day2Part1():

    # split apart the lines into rules and password

    lEntry = []
    for strLine in day2in.lStr:
        lEntry.append(Entry(strLine))

    # check if the password matches the rules

    cEntryValid = 0
    for entry in lEntry:
        if entry.FIsValid2():
            cEntryValid += 1

    print(cEntryValid)

if __name__ == '__main__':
    Day2Part1()
