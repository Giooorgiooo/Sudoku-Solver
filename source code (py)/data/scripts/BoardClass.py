from tkinter import *
from tkinter import ttk
import tkinter, time

from data.scripts.SudokuClass import Sudoku

class Board:
    def __init__(self) -> None:
        self.reset_board = False
    
    # limiting the number of characters
    def limitSquareChars(self, event):
        # possible input
        numbers = [str(i) for i in range(1, 10)]
        for square in self.squares:
            # checking if there is more than one character in a square
            if len(square.get()) > 1:
                square.delete(1, END)
            
            # checking if there is any character which is not a number
            if not square.get() in numbers:
                square.delete(0, END)

    # adding every input square to an array and to the screen
    def addSquares(self, root: Tk):
        self.root = root
        self.squares = []
        for position_y in range(9):
            for position_x in range(9):
                # adding the square
                self.squares.append(ttk.Entry(root, font = "TkDefaultFont 44", justify = CENTER))
                # positioning the square
                self.squares[-1].place(width = 100, height = 100, x = position_x * 100, y = position_y * 100)
        
        # adding events to limit the characters of one square
        for square in self.squares:
            # key down
            square.bind("<KeyPress>", self.limitSquareChars)
            # key up
            square.bind("<KeyRelease>", self.limitSquareChars) 
        return self.squares
    
    # adding the button "solve"
    def addSolveButton(self, root: Tk):
        solve_button = tkinter.Button(root, text="solve sudoku", font = "TkDefaultFont 15", command=self.solveSudoku)
        solve_button.place(x = 935, y = 435)

    # adding the button "reset"
    def addResetButton(self, root: Tk):
        reset_button = tkinter.Button(root, text="reset sudoku", font = "TkDefaultFont 15", command=self.resetSudoku)
        reset_button.place(x = 935, y = 335)

    # executing on button press
    # solving the Sudoku
    def solveSudoku(self):
        if self.reset_board:
            self.reset_board = False
        # converting the input of the squares into integers
        # to use it for the solving process
        board = []
        for square in self.squares:
            if square.get() == "":
                board.append(0)
            else:
                board.append(int(square.get()))

        sudoku = Sudoku(board)

        # solving the sudoku
        sudoku.solve()
        
        # converting the solved array back to the screen
        for index, square in enumerate(self.squares):
            if square.get() == "":
                # delay for animation
                time.sleep(0.05)
                # every new square is blue
                square.config(foreground = "blue")
                # inserting new value
                square.delete(0, END)
                square.insert(0, str(sudoku.board[index]))
                # updating the window
                self.root.update()
            if self.reset_board:
                self.resetSudoku()
                break
    
    # resetting the screen (board)
    def resetSudoku(self):
        self.reset_board = True
        for square in (self.squares):
            # text color is set to black
            square.config(foreground = "black")
            # deleting the numbers in the squares
            square.delete(0, END)
            square.insert(0, "")
                
