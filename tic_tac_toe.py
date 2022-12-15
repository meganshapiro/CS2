'''
Created on Nov 15, 2022

@author: MShapiro24
'''
from test.inspect_fodder2 import gone
from pickle import TRUE

def make_grid():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
    for row in range(0,3):
        col = 0
        for col in range(0,3):
            print(grid[row][col], end = " ")
        print("")
   
        
def print_score(score_board):
    print("--------------------")
    print("score board")
    
    player = list(score_board.keys())
    print( " ", player[0], " ", score_board[player[0]])
    print( " ", player[1], " ", score_board[player[1]])
    
    print("--------------------")
    
def confirm_win(pos_player, random_player):
    combo = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for x in combo:
        if all(y in pos_player[random_player] for y in x):
            return True
    return False

def confirm_tie(pos_player):
    if len(pos_player['X']) + len(pos_player['0']) == 9:
        return True
    return False
    
def game_play(random_player):
    value = {'' for x in range(9)}
    pos_player = {'X': [], 'O': []}
    
    while True:
        make_grid()
    
        try:
            print("It's player", random_player, "turn. Please select a box.", end="")
            selection = int(input())
        except ValueError:
            print("Please input another value 1-9")
            continue

        if selection < 1 or selection > 9:
            print("Please input another value 1-9")
            continue
        
        if make_grid([])[selection-1] != '':
            print("This box is taken. Please input another value 1-9")
            continue

        make_grid[selection-1] = random_player

        pos_player[random_player].append(selection)

        if confirm_win(pos_player, random_player):
            make_grid()
            print("Player", random_player, "won!")
            return random_player
        
        if confirm_tie(pos_player):
            make_grid()
            print("It's a tie game!")
            return 'T' 


        if random_player == 'X':
            random_player == 'O'
        else:
            random_player = 'X'
    

if __name__ == '__main__':
    
    print("Let's play tic tac toe")
    
    
    print("Player 1")
    player1 = input("Enter your name:")
    
    print("Player 2")
    player2 = input("Enter your name:")
    
    
    random_player = player1
    player_choice = {'X': "", 'O' : ""}
    options = ['X', 'O']
    score_board = {player1: 0, player2: 0}
    print_score(score_board)

    
    while True:
        print("Choose a symbol for", random_player)
        print("Input 1 for X")
        print("Input 2 for O")
        
        try:
            choice = int(input())
            
        except ValueError:
            print("Please enter in a valid input")
            continue
        
        if choice == 1:
            player_choice['X'] = random_player
            if random_player == player1:
                player_choice['O'] = player2
            else:
                player_choice["O"] = player1
                
        elif choice == 2:
            player_choice['O'] = random_player
            if random_player == player1:
                player_choice['X'] = player2
            else:
                player_choice["X"] = player1
                
        else:
            print("Please enter in 1 or 2 to select X or O")
        
    
        player_won = game_play(options[choice-1])

        if player_won != 'T':
            winner = player_choice[player_won]
            score_board[winner] = score_board[winner] + 1
 
 
    
        
    
    main()