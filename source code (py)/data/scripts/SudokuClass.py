class Sudoku:
    def __init__(self, board: list[int]) -> None:
        self.rows = 9
        self.columns = 9
        self.board = board
        return None

    # printing the board in a readable way
    def printBoard(self):
        for y in range(self.rows):
            print("| ", end="")
            for x in range(self.columns):
                print(self.getValue(x, y), "| ", end="")
            print("\n", end="")
            if (y + 1) % 3 == 0:
                for i in range(9):
                     print("----", end="")
                print("\n", end="")
        return None
    
    # getting value of a square
    def getValue(self, position_x: int, position_y: int):
        return self.board[position_x + position_y * self.columns]

    # chacking if an input is valid at a specific square
    def valueIsPossible(self, position_x: int, position_y: int, value: int):
        for index in range(self.columns):
            # checking for x row
            if value == self.getValue(index, position_y) and not index == position_x:
                return False   
            # checking for y column
            if value == self.getValue(position_x, index) and not index == position_y:
                return False   

        # checking for every of the nine larger squares 
        squares = [[] for i in range(9)]
        square_position_x = 0
        square_position_y = 0

        # adding every position into a subarray
        for a in range(3):
            for i in range(3):
                for x in range(3):
                    for y in range(3):
                        squares[a + i * 3].append([x + square_position_x, y + square_position_y])
                square_position_x += 3
            square_position_x = 0
            square_position_y += 3

        # checking if the given value is valid value 
        for square in squares:
            if [position_x, position_y] in square:
                for position in square:
                    if self.getValue(position[0], position[1]) == value:
                        return False
        return True

    def boardIsValid(self) -> bool:
        for x in range(self.columns):
            for y in range(self.rows):
                if not self.getValue(x, y) == 0:
                    if not self.valueIsPossible(x, y, self.getValue(x, y)):
                        return False
        return True

    # solving the board
    def solve(self):
        for y in range(self.rows):
            for x in range(self.columns):
                # checking if square is empty
                if self.getValue(x, y) == 0:
                    # testing every possible number
                    for value in range (1, 10):
                        if self.valueIsPossible(x, y, value):
                            # doing checking move
                            self.board[x + y * self.columns] = value
                            # recursivly calling
                            if self.solve():
                                return True
                            # undoing the move
                            self.board[x + y * self.columns] = 0   
                    # returning None if one square cant be set to one of the 9 numbers
                    return None
                
        # returning True when there is a solution
        return True
