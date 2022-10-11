from data.scripts.RootClass import Root
from data.scripts.BoardClass import Board
from tkinter import *
import tkinter    

if __name__ == "__main__":

    # creating the window
    root = Root.init((1100, 900), "sudoku solver")

    board = Board()

    # adding squares to the screen
    squares = board.addSquares(root)
    # adding buttons to the screen
    board.addSolveButton(root)
    board.addResetButton(root)

    tkinter.mainloop()