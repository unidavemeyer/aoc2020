import day3in

# day 3 - traversing maps of trees

class Map:
    def __init__(self, strIn):

        self.dictPosTree = {}
        self.xMost = 0
        self.yMost = 0

        # pull information out of the input string for the map

        for y, strLine in enumerate(strIn.split('\n')):
            self.yMost = max(self.yMost, y)
            for x, ch in enumerate(strLine):
                self.xMost = max(self.xMost, x)
                if ch == '#':
                    self.dictPosTree[(x,y)] = True

    def IsTree(self, pos):
        # wrap around the position in X

        posCheck = (pos[0] % (self.xMost + 1), pos[1])
        return self.dictPosTree.get(posCheck, False)

def Part1():
    mapTrees = Map(day3in.strIn)
    x = 0
    y = 0

    cTree = 0

    while y <= mapTrees.yMost:
        if mapTrees.IsTree((x,y)):
            cTree += 1

        x += 3
        y += 1

    print(cTree)

def Part2():
    mapTrees = Map(day3in.strIn)

    # repeat a bunch of times
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

    lcTree = []
    for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        x = 0
        y = 0

        cTree = 0

        while y <= mapTrees.yMost:
            if mapTrees.IsTree((x,y)):
                cTree += 1

            x += right
            y += down

        print(cTree)
        lcTree.append(cTree)
    
    product = 1
    for cTree in lcTree:
        product *= cTree

    print(product)

if __name__ == '__main__':
    Part1()
    Part2()

