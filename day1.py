import day1in

def PairFindSum(lN, n):
    # find two entries in the list that sum to n, dumb simple version

    for n0 in lN:
        for n1 in lN:
            if n0 + n1 == n:
                return (n0, n1)

    return (0, 0)

def TripleFindSum(lN, n):

    for n0 in lN:
        for n1 in lN:
            for n2 in lN:
                if n0 + n1 + n2 == n:
                    return (n0, n1, n2)

    return (0, 0, 0)

if __name__ == '__main__':
    pair = PairFindSum(day1in.lN, 2020)
    print(pair[0], pair[1], pair[0] * pair[1])

    triple = TripleFindSum(day1in.lN, 2020)
    print(triple[0], triple[1], triple[2], triple[0] * triple[1] * triple[2])
