'''
Name: Megan Shapiro
Date: December 1, 2022
Description: A program that allows 2 users to play tic tac toe against each other
Bugs: None
Features: Keeps score of game
Log: Submitted for a grade on December 2, 2022
Plan:
    1. Create the grid for the game
    2. Allow users to play game until someone wins or grid is full
        a. Updates grid after user selects the box they want
    3. Program decides if a player won or if it's a tie game
    4. Score is displayed
'''

#defining variables
move_player1 = "X"
move_player2 = "O"
empty = "-"
grid_size = 3
space = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#assigning empty to '-' to show the available spaces   
grid = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]

#this function prints the grid
def print_grid():
    for i in range(grid_size):          #iterate value within grid_size
        for j in range(grid_size):
            next_box = grid[i][j]
            if next_box == empty:       #if next_box is empty, add integers
                next_box = grid_size * i + j
            print(next_box, end = " ")
        print(" ")
        
#this function updates the grid once a player selects a box
def grid_update(move, player1):
    row = move // grid_size     # //grid_size gives the row number
    column = move % grid_size   # % grid_size gives the column number
    if player1:
        grid[row][column] = move_player1    #places player1 in specific location
    else:
        grid[row][column] = move_player2    #places player1 in specific location
    print_grid() #prints out grid

#this function will find if the grid is full and end the game if so
def full_grid():
    #looks for a dash. if it finds a dash/-/Empty
    #If this function finds a dash -- the game is still on.
    #If it DOESN'T FIND a dash "-" all slots are full
    
    dash_found = False
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == empty:                 #EMPTY means '-'
                dash_found = True                   #a dash was found -- not a tie!
                return dash_found
            #else:
                #dash_found = True                 #a dash Was NOT found!
                
                
        
    return dash_found    
                    
#this function shows all of the winning options and uses boolean conditions
def player_win(taken):
    
    winner = False
    
    #boolean operators that determine a win
    if (grid[0][0] == taken and grid[0][1] == taken and grid [0][2] == taken) \
        or (grid[1][0] == taken and grid[1][1] == taken and grid[1][2] == taken) \
        or (grid[2][0] == taken and grid[2][1] == taken and grid[2][2] == taken) \
        or (grid[0][0] == taken and grid[1][0] == taken and grid[2][0] == taken) \
        or (grid[0][1] == taken and grid[1][1] == taken and grid[2][1] == taken) \
        or (grid[0][2] == taken and grid[1][2] == taken and grid[2][2] == taken) \
        or (grid[0][0] == taken and grid[1][1] == taken and grid[2][2] == taken) \
        or (grid[0][2] == taken and grid[1][1] == taken and grid[2][0] == taken):
    
        winner = True   #if winner starts 
        
        
    return winner
    

#this function will tell the user if their move was valid or not
def right_move(move):
    if move not in space:
        return False        #if the move is not in an open space then return a false
    move = int(move)
    row = move // grid_size
    column = move % grid_size
    return grid[row][column] == empty
    
#this function will print the score board after the round has ended 
def print_score(player1_score, player2_score):
    print("--------------------")
    print("score board")
    
    
    print( " ", player1_score, " ")
    print( " ", player2_score, " ")
    
    print("--------------------")


    
def game_play(player1_score, player2_score): 

    #while the grid is not full, player 1 and 2 will be able to go back and forth putting in Xs and Os
    while full_grid() == True:
        move_player1 = input("Player 1, you are X. Please pick your box: ")
        while not right_move(move_player1):
            move_player1 = input ("Please enter in a valid input")  #if input is not valid try again
        grid_update(int(move_player1), True)
        if player_win("X"):
            print("Player 1 wins!")
            player1_score += 1  #adds 1 to the score when player1 wins
            break
        elif full_grid() == False:
            print("It's a tie game!")
            break
        
        move_player2 = input("Player 2, you are O. Please pick your box: ")
        while not right_move(move_player2):
            move_player2 = input("Please enter in a valid input")   #if input is not valid try again
        grid_update(int(move_player2), False)
        if player_win("O"):
            print("Player 2 wins!")
            player2_score +=1   #adds 1 to the score when player1 wins
            break
        elif full_grid() == False:  
            print("It's a tie game!")
            break
        
    return player1_score, player2_score
        
def main():
    
    #starts scoers at 0
    player1_score = 0
    player2_score = 0

    
    print("Let's play tic tac toe")
    
    print("Player 1")
    player1 = input("Enter your name:")
    
    print("Player 2")
    player2 = input("Enter your name:")
    
   
    print_grid()
    
    #will print the grid
    for row in range(0,3):
            col = 0
            for col in range(0,3):
                print(grid[row][col], end = " ")
            print("")   
            
    player1_score, player2_score = game_play(player1_score, player2_score)
    
         
    #starts the score of at 0-0
    print_score(player1_score, player2_score)       #prints final score
    

    
    
#main()  
if __name__ == '__main__':    
    main()