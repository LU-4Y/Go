#initialization
import string
#initialization

#simple class to call black or white pieces from.
class Pieces:
    def __init__(self):
        self.b = "●"
        self.w = "○"

#the board is defined as an object so it can be persistent and managed between turns
class Board:

    def __init__(self, size = 19): #generates a board at the start of the game
        if size > 25:
            raise Exception("Board size must be less than or equal to 25.")
        
        self.size = size
        self.layout = [["+" for x in range(size)] for x in range(size)]
        self.color = Pieces()
        self.key = {}

        #generate grid key for board
        rows_low = string.ascii_lowercase[:size]
        rows_upp = string.ascii_uppercase[:size]
        for n in range(size):  #I know this is t = O(n^2). I don't know if I want to fix it because the max grid size is 25.
            for m in range(size):
                self.key_low[rows_low[n] + str(m)] = [n,m]
                self.key_upp[rows_upp[n] + str(m)] = [n,m]
        #generate grid key for board

    def place_piece(self, place):  #place is a list.  The first item is the turn, the second item is the grid coordinate.
        #unpack place variable
        color = place[0]
        coord = place[1]
        #unpack place variable

        #convert coord to layout parameters

        #convert coord to layout parameters

        ##check if valid move
        
        #check if valid move