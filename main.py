from classes import Pieces, Board
import string #still needed?
import re

def main():
    ##Initialization
    #ask for board size
    int_test = True
    while int_test == True:
        try: #Ensures entered number is an integer
            board_size = int(input("Enter a board size (Min = 2, Max = 25; leave blank for default size of 19): ") or "19")
            int_test = False #if int() does not throw an error, int_test is set to false so the while loop does not repeat
        except:
            print("Board size must be an integer.")
            continue #resets from while int_test == True:

        #enforce minimum and maximum board size
        if board_size < 2:
            board_size = int(2)
        elif board_size > 25:
            board_size = int(25)

    #construct necessary objects
    current_board = Board(board_size)
    p = Pieces()
    quit_state = False #if the primary game loop reaches its conclusion and this variable is True, the program terminates
    current_turn = p.w #white goes first
    k = 1

    ##Primary game loop
    while quit_state == False:
        #print current board

        for i in range(board_size):
            current_row = current_board.layout[i].append("  " + str(current_board.rows[i]))
            print_current_row = ""
            for j in range (board_size):
                print_current_row = print_current_row + current_row[j] # type: ignore
            print(print_current_row)
        
        print(current_board.columns)
        try:  #in the first loop through the program, the print_commands variable will not yet be defined.  This exception is handled by "try".
            if print_commands == True:
                print("? - List all possible commands.")
                print("C2 - Play the current piece at spot C2.")
                print("P - Pass the current turn.")
                print("Q - Quit the game. WARNING: GAME SAVING NOT YET IMPLEMENTED!")
        finally:
            print_commands = False
        
        try:
            if k == 0:
                print("That was an invalid move.  Please try again.")
        finally:
            k = 1

        #ask user for input
        print("Issue a '?' to list all possible commands.")
        user_action = input("Issue a command: ")
        user_action = re.sub('\s','',user_action) #eliminate white space in the submitted action.
        user_action = re.sub('\W','',user_action) #eliminate non-letter/number characters (does this include white space?  If yes, previous line is redundant.)

        #take action based on input
        if user_action == '?':
            print_commands = True
            continue
        elif user_action == 'P':
            if current_turn == p.b:
                current_turn = p.w
            elif current_turn == p.w:
                current_turn = p.b
            continue
        elif user_action == 'Q':
            break
        else:
            place = [current_turn, user_action]
            k = current_board.place_piece(place)

##Ensure the program only runs when executed directly from the terminal
import os

def clear_console():
    # os.name is 'nt' for Windows, 'posix' for macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
        try:
            clear_console()
        finally:
            main()
