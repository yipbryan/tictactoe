import board
import cover

def main():

    # Start screen
    cover.printHeader()
    
    # initialise the game board
    gb = board.GameBoard()

    # initalise beginning variables
    player = 1
    victory = False # if game ends without a winner, this variable will remain False
    turn = 1

    # while loop to run gameplay
    while turn < 10:
        # print a few messages
        gb.printBoard()
        print("-----------------------------------------------")
        print("Turn: " + str(turn))
        print("Player " + str(player) + ", please make your move.")

        # retrieve player input and process it (cast to integer)
        while True:           
            row, col = raw_input("Please input row. "), raw_input("Please input column. ")
            valid = gb.checkValid(row, col)
            if valid:
                row, col = int(row), int(col)
                break
            else:
                continue

        gb.setValue(row, col, player)

        # modify board, print resulting board and check for victory condition
        victory = gb.checkVictory(player, row, col)
        # if victorious, announce winner and break out of while loop
        if victory:
            print("Player " + str(player) + " wins!")
            break

        # increment turn at the end (max 9 turns in 3x3 matrix)
        turn += 1
        # shift control to second player
        if player == 1:
            player = 2
        else:
            player = 1

    if not victory:
        print("Ended in a tie!")

    

main()


# issues to fix 
# 1 - error checking. prevent invalid selections and ask for another input (done)
# 2- victory checking doesn't work, fix that (done)
# 3 - design a nice start screen (done)
# 4 - refactor into multiple functions? possibly unneccesary
# 5 - write unit tests?
# 6- perform own testing - try to break the game
# 6 - AI with 3 difficulty settings (long run goal)