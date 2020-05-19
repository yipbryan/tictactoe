
class GameBoard:

    def __init__(self, board = [["-","-","-"],["-","-","-"],["-","-","-"]]):
        self.board = board

    def printBoard(self):
        for row in self.board:
            print(row)

    # playerNum variable will be set by while loop in main method
    def setValue(self, row, col, playerNum):
        if playerNum == 1:
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

        return True

    def checkValid(self, row, col):
        valid = True
        valid_inputs = ["0", "1", "2"]
        if row not in valid_inputs or col not in valid_inputs:
            valid = False
            print("Invalid input, please try again.")
            return valid
        elif self.board[int(row)][int(col)] != "-":
            valid = False
            print("Invalid input, please try again.")            
        
        return valid

    def checkVictory(self, playerNum, row, col):
        # there are only 8 ways to win - just check for these 8 conditions
        victory = False

        if playerNum == 1:
            icon = "X"
        else:
            icon = "O"

        # assign shorthand reference to board
        bd = self.board

        # implement victory condition algorithm (naive, check for all 8)
        # all rows
        for i in range(3):
            if bd[i] == [icon, icon, icon]:
                victory = True

        # all columns
        for j in range(3):
            if bd[0][j] == icon and bd[1][j] == icon and bd[2][j] == icon:
                victory = True

        # all diagonals
        if bd[0][0] == icon and bd[1][1] == icon and bd[2][2] == icon:
            victory = True
        
        if bd[2][0] == icon and bd[1][1] == icon and bd[0][2] == icon:
            victory = True

        return victory

