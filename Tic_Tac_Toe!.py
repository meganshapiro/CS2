'''
Name: Megan Shapiro
Date: December 1, 2022
Description: A program that allows 2 users to play tic tac toe against each other
Bugs: 
Features: Keeps score of game
Log: Submitted for a grade on December 2, 2022
Plan:
    1. Create the grid for the game
    2. Allow users to play game until someone wins or grid is full
        a. Updates grid after user selects the box they want
    3. Program decides if a player won or if it's a tie game
    4. Score is displayed
'''
from pickle import FALSE, TRUE

#defining variables
move_player1 = "X"
move_player2 = "O"
empty = "-"
grid_size = 3
space = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#assigning empty to '-' to show the available spaces   
grid = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]

#this function prints the grid
def print_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            next_box = grid[i][j]
            if next_box == empty:
                next_box = grid_size * i + j
            print(next_box, end = " ")
        print(" ")
        
#this function updates the grid once a player selects a box
def grid_update(move, player1):
    row = move // grid_size     # //grid_size gives the row number
    column = move % grid_size   # % grid_size gives the column number
    if player1:
        grid[row][column] = move_player1
    else:
        grid[row][column] = move_player2
    print_grid()

#this function will find if the grid is full and end the game if so
def full_grid():
    #looks for a dash. if it finds a dash/-/Empty
    
    dash_found = True
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == empty:                 #EMPTY means '-'
                dash_found = True                   #a dash was found -- not a tie!
                return dash_found
            else:
                dash_found = False                  #a dash Was NOT found!
                return dash_found

            
#this function shows all of the winning options and uses boolean conditions
def player_win(taken):
    
    winner = False
    
    if (grid[0][0] == taken and grid[0][1] == taken and grid [0][2] == taken) \
        or (grid[1][0] == taken and grid[1][1] == taken and grid[1][2] == taken) \
        or (grid[2][0] == taken and grid[2][1] == taken and grid[2][2] == taken) \
        or (grid[0][0] == taken and grid[1][0] == taken and grid[2][0] == taken) \
        or (grid[0][1] == taken and grid[1][1] == taken and grid[2][1] == taken) \
        or (grid[0][2] == taken and grid[1][2] == taken and grid[2][2] == taken) \
        or (grid[0][0] == taken and grid[1][1] == taken and grid[2][2] == taken) \
        or (grid[0][2] == taken and grid[1][1] == taken and grid[2][0] == taken):
        winner = True
    return winner
    

#this function will tell the user if their move was valid or not
def right_move(move):
    if move not in space:
        return FALSE
    move = int(move)
    row = move // grid_size
    column = move % grid_size
    return grid[row][column] == empty
    
#this function will print the score board after the round has ended 
def print_score(score_board):
    print("--------------------")
    print("score board")
    
    player = list(score_board.keys())
    print( " ", player[0], " ", score_board[player[0]])
    print( " ", player[1], " ", score_board[player[1]])
    
    print("--------------------")


    
def game_play():    
    #while the grid is not full, player 1 and 2 will be able to go back and forth putting in Xs and Os
    while full_grid() == True:
        move_player1 = input("Player 1, you are X. Please pick your box: ")
        while not right_move(move_player1):
            move_player1 = input ("Please enter in a valid input")
        grid_update(int(move_player1), True)
        if player_win(move_player1):
            print("Player 1 wins!")
            break
        elif full_grid():
            print("It's a tie game!")
            break
        
        move_player2 = input("Player 2, you are O. Please pick your box: ")
        while not right_move(move_player2):
            print("112")
            move_player2 = input("Please enter in a valid input")
            grid_update(int(move_player2), False)
            if player_win(move_player2):
                print("Player 2 wins!")
                break
        
def main():
    
    print("Let's play tic tac toe")
    
    print("Player 1")
    player1 = input("Enter your name:")
    
    print("Player 2")
    player2 = input("Enter your name:")
    
    #starts the score of at 0-0
    score_board = {player1: 0, player2: 0}
    print_score(score_board)
    
    
    print_grid()
    
    #will print the grid
    for row in range(0,3):
            col = 0
            for col in range(0,3):
                print(grid[row][col], end = " ")
            print("")   
            
    game_play()
    
    
    
#main()  
if __name__ == '__main__':    
    main()