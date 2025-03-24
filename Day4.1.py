test = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

lines = test.split("\n")

ysize = len(lines)
xsize = len(lines[0])

class Space():
    def __init__(self, letter):
        self.letter = letter
    def isX(self):
        if self.letter == "X":
            return True
    def isM(self):
        if self.letter == "M":
            return True
    def isA(self):
        if self.letter == "A":
            return True
    def isS(self):
        if self.letter == "S":
            return True

class Board():
    def __init__(self, xsize, ysize, lines):
        


