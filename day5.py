import day5in

# day 5 problems

class BoardingPass:
    def __init__(self, strIn):
        self.m_str = strIn
        self.m_row = None
        self.m_col = None
        self.m_id = None

        # first seven chars are f/b for row - f = 0, b = 1, binary encoding

        strRow = strIn[:7]
        strRow = strRow.replace('F', '0')
        strRow = strRow.replace('B', '1')
        strRow = '0b' + strRow
        self.m_row = int(strRow, 2)

        # last three chars are l/r for column

        strCol = strIn[-3:]
        strCol = strCol.replace('L', '0')
        strCol = strCol.replace('R', '1')
        strCol = '0b' + strCol
        self.m_col = int(strCol, 2)

        # seat id

        self.m_id = self.m_row * 8 + self.m_col

    def SortKey(self):
        return self.m_id

def Part1():
    lBoardingpass = [BoardingPass(strIn) for strIn in day5in.strIn.split()]

    idMost = 0
    for bp in lBoardingpass:
        # print("bp:", bp.m_str, bp.m_row, bp.m_col, bp.m_id)
        idMost = max(idMost, bp.m_id)

    print("Part 1: largest seat id:", idMost)

def Part2():
    lBoardingpass = [BoardingPass(strIn) for strIn in day5in.strIn.split()]

    # sort the boarding passes by seat id

    lBoardingpass.sort(key=BoardingPass.SortKey)

    # find where we are missing the "next" seat id (plane is full) and report it

    idMissing = 0
    for iBp, bp in enumerate(lBoardingpass):
        if lBoardingpass[iBp + 1].m_id != bp.m_id + 1:
            idMissing = bp.m_id + 1
            break

    print("Part 2: missing seat id:", idMissing)

if __name__ == '__main__':
    Part1()
    Part2()
