import day4in

# passport checking, day 4

def FIsRangedYearValid(strValue, nMin, nMost):
    if len(strValue) != 4:
        return False

    return FIsValidRanged(strValue, nMin, nMost)

def FIsRangedPidValid(strValue):
    if len(strValue) != 9:
        return False

    return FIsValidRanged(strValue, 0, 999999999)

def FIsValidRanged(strValue, nMin, nMost):
    try:
        n = int(strValue)
        if n < nMin or n > nMost:
            return False
    except: # bad form - should have specific exception caught
        return False

    return True

class Passport:
    def __init__(self, strIn):
        self.dictFieldValue = {}

        lPart = strIn.split()
        for part in lPart:
            key, value = part.split(':')
            self.dictFieldValue[key] = value

    def FIsValid(self):

        lFieldReq = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
            ]

        for field in lFieldReq:
            if field not in self.dictFieldValue:
                return False

        return True

    def FIsValid2(self):
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        
        if not FIsRangedYearValid(self.dictFieldValue.get('byr', ''), 1920, 2002):
            return False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.

        if not FIsRangedYearValid(self.dictFieldValue.get('iyr', ''), 2010, 2020):
            return False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

        if not FIsRangedYearValid(self.dictFieldValue.get('eyr', ''), 2020, 2030):
            return False

        # hgt (Height) - a number followed by either cm or in:
        #   If cm, the number must be at least 150 and at most 193.
        #   If in, the number must be at least 59 and at most 76.

        hgt = self.dictFieldValue.get('hgt', '')

        if 'cm' not in hgt and 'in' not in hgt:
            return False

        if 'cm' in hgt and not FIsValidRanged(hgt[:-2], 150, 193):
            return False
        elif 'in' in hgt and not FIsValidRanged(hgt[:-2], 59, 76):
            return False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

        hcl = self.dictFieldValue.get('hcl', '')

        if len(hcl) != 7:
            return False

        if hcl[0] != '#':
            return False

        for ch in hcl[1:]:
            if ch not in '0123456789abcdef':
                return False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

        ecl = self.dictFieldValue.get('ecl', '')
        setEcl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        if ecl not in setEcl:
            return False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.

        pid = self.dictFieldValue.get('pid', '')

        if not FIsRangedPidValid(pid):
            return False

        return True

def LPassportLoad(strIn):

    lStr = strIn.split('\n\n')
    
    lPassport = [Passport(strX) for strX in lStr]

    return lPassport

def Part1():
    # load passports
    lPassport = LPassportLoad(day4in.strIn)

    # check validity

    cValid = 0

    for passport in lPassport:
        if passport.FIsValid():
            cValid += 1

    print("Part 1:", cValid, "passports valid")

def Part2():
    # load passports
    lPassport = LPassportLoad(day4in.strIn)

    # check validity

    cValid = 0

    for passport in lPassport:
        if passport.FIsValid2():
            cValid += 1

    print("Part 2:", cValid, "passports valid")

if __name__ == '__main__':
    Part1()
    Part2()
