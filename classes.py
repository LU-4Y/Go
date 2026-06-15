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
        if size < 2:
            raise Exception("Board size must be greater than or equal to 2.")
        
        self.size = size
        self.layout = [["+" for x in range(size)] for x in range(size)]
        self.color = Pieces()  #Do we need this line?  Or should I declare the color class in the main file?
        self.key = {}

        #generate grid key for board
        self.columns = string.ascii_uppercase[:size] #NOTE: you will need to convert coordinates to upper case using .upper() to fit the key.
        for n in range(size):  #I know this is t = O(n^2). I don't know if I want to fix it because the max grid size is 25.
            for m in range(size):
                self.key[self.columns[n] + str(m+1)] = [n,m] #Creates a dictionary entry that connects to every coordinate location in layout.  "A1" maps to [0,0], "C2" maps to [2,1], etc.
        #generate grid key for board

        self.rows = []
        for i in range(1, size + 1, 1):
            self.rows.append(str(i))
            

    def place_piece(self, place) -> int:  #place is a list.  The first item is the turn of the player, the second item is the grid coordinate.
        #unpack place variable
        player = place[0]
        coord = place[1].upper() #upper() ensures compatability with Board.key dict
        #unpack place variable

        k = int(0) #initialization within method. This variable will determine whether the turn moves forward or not.  k=0 is returned from this method if something is wrong, k=1 is returned from this method if a piece is successfully played on the board.

        coord = self.key[coord] #convert coord to layout parameters

        #check if valid move
        if (self.layout[coord[0]][coord[1]] != "+"): #A piece cannot be placed on top of another piece
            return k
        else: #expand placement conditions for valid move
            return k
            
        #check if valid move