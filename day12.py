# day 12 problem solutions

import day12in

class Boat:
    def __init__(self, strIn):
        self.m_lMove = []
        self.m_pos = (0,0)
        self.m_dPosWaypoint = (10,1)
        self.m_heading = 'E'

        self.Parse(strIn)

    def Parse(self, strIn):
        # pull instructions apart

        for strLine in strIn.split('\n'):
            op = strLine[0]
            count = int(strLine.strip()[1:])
            self.m_lMove.append((op, count))

    def Move(self):
        for op, count in self.m_lMove:

            # BB (davidm) could do fn table instead of branching here

            # handle turns/forward first

            lHeading = ['N', 'E', 'S', 'W'] # headings ordered clockwise ("right") turns

            if op == 'L' or op == 'R':
                # find current heading index (could just store index instead)
                iHeading = lHeading.index(self.m_heading)

                # calculate index offset
                diHeading = int(count / 90)
                if op == 'L':
                    diHeading = -diHeading

                iHeadingNext = (iHeading + diHeading) % len(lHeading)
                self.m_heading = lHeading[iHeadingNext]
                continue

            elif op == 'F':
                # use our heading as the travel direction
                op = self.m_heading

            # handle motion component second

            if op == 'N':
                self.m_pos = (self.m_pos[0], self.m_pos[1] + count)
            elif op == 'S':
                self.m_pos = (self.m_pos[0], self.m_pos[1] - count)
            elif op == 'E':
                self.m_pos = (self.m_pos[0] + count, self.m_pos[1])
            elif op == 'W':
                self.m_pos = (self.m_pos[0] - count, self.m_pos[1])

    def MoveWaypoint(self):
        for op, count in self.m_lMove:

            # BB (davidm) could do fn table instead of branching here

            if op == 'L' or op == 'R':
                # rotate waypoint around the boat (easy since we store as dpos)

                # there is probably a closed form, but this model isn't too crazy

                cRot = (count // 90) % 4
                fnRot = lambda x,y: (y,-x)
                if op == 'L':
                    fnRot = lambda x,y: (-y,x)

                for iRot in range(cRot):
                    self.m_dPosWaypoint = fnRot(self.m_dPosWaypoint[0], self.m_dPosWaypoint[1])

            elif op == 'F':
                # add waypoint offset to boat

                self.m_pos = (self.m_pos[0] + count * self.m_dPosWaypoint[0], self.m_pos[1] + count * self.m_dPosWaypoint[1])

            elif op == 'N':
                self.m_dPosWaypoint = (self.m_dPosWaypoint[0], self.m_dPosWaypoint[1] + count)
            elif op == 'S':
                self.m_dPosWaypoint = (self.m_dPosWaypoint[0], self.m_dPosWaypoint[1] - count)
            elif op == 'E':
                self.m_dPosWaypoint = (self.m_dPosWaypoint[0] + count, self.m_dPosWaypoint[1])
            elif op == 'W':
                self.m_dPosWaypoint = (self.m_dPosWaypoint[0] - count, self.m_dPosWaypoint[1])

    def StrOffset(self):
        return "{o} (at {x},{y})".format(o=abs(self.m_pos[0]) + abs(self.m_pos[1]), x=self.m_pos[0], y=self.m_pos[1])

def Part1():
    boat = Boat(day12in.strIn)
    boat.Move()

    print("Part 1:", boat.StrOffset())

def Part2():
    boat = Boat(day12in.strIn)
    boat.MoveWaypoint()

    print("Part 2:", boat.StrOffset())

if __name__ == '__main__':
    Part1()
    Part2()
