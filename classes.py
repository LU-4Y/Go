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
        self.color = Pieces()  #Do we need this line?  Or should I declare the color class in the main file?
        self.key = {}

        #generate grid key for board
        rows = string.ascii_uppercase[:size] #NOTE: you will need to convert coordinates to upper case using .upper() to fit the key.
        for n in range(size):  #I know this is t = O(n^2). I don't know if I want to fix it because the max grid size is 25.
            for m in range(size):
                self.key[rows[n] + str(m)] = [n,m] #Creates a dictionary entry that connects to every coordinate location in layout.  "A1" maps to [1,1], "A2" maps to [1,2], etc.
        #generate grid key for board

    def place_piece(self, place) -> int:  #place is a list.  The first item is the turn, the second item is the grid coordinate.
        #unpack place variable
        player = place[0]
        coord = place[1].upper() ##upper() ensures compatability with Board.key dict
        #unpack place variable

        k = 0 #initialization within mathod. This variable will determine whether the turn moves forward or not.  k=0 is returned from this method if something is wrong, k=1 is returned from this method if a piece is successfully played on the board.

        coord = self.key[coord] #convert coord to layout parameters

        #check if valid move
        if (self.layout[coord[0]][coord[1]] != "+"):
            return k
        #check if valid move