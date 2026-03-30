# Go
Simple application to play Go between two human players.

Version 1.0 Project requirements:  
    >   Resizeable Go board (Can the board go in its own class?)  
    >   Capture logic (zero liberty condition) (insert board, check condition, make changes, return new board if changes are made)  
    >   Point logic (Japanese ruleset) (insert board, return current points)  
    >   Turns (white always goes first)  
    >   Display board on screen  
    >   Text commands (placement, quitting, passing)

Version 2.0 Project requirements:  
    >   Playable over local area network  
    >   Starting menu (terminal)  
    >   Game saving (prerequisite for LAN play)  
    >   P2P optional  
    >   GUI optional  

Version 3.0 Project requirements:  
    >   Implemented GUI  
    >   P2P over LAN  

==========================================  
==========================================  

29MAR2026
Notes on connecting pieces for capture and point logic.
When pieces are on a board, they intrinsically "connect" to adjacent pieces.  I will need to write an algorithm to determine the contiguous bodies on the board.  The way I am thinking of tackling that right now is using a "growing tree" model.  

When a piece is placed, it performs a check in all four direction of itself.  Where it finds another piece of the same color, it grows a "branch" to connect with that, joining to that contiguous body.  Where it finds empty space, a "+", it has a liberty (can also be considered a branch, but of a different type).  

As I type this out, I think I should have a "contiguous body" class which has specified coordinates on the board, and each time a piece is placed, it checks if it touches a contiguous body, and the contiguous body object is updated to include it.  This will help manage liberties; when all the liberties of a contiguous body are filled, the coordinates of the contiguous body is replaced with "+", and the object is then deleted.  If the piece is solitary, it should not need to instantiate a contiguous object class.  When two contiguous bodies connect, they form a new one.  

It seems like we can track how a contiguous body changes by tracking what piece is placed in a liberty coordinate.

To calculate points, it may be necessary to calculate inverse liberties of "+" spaces as well.