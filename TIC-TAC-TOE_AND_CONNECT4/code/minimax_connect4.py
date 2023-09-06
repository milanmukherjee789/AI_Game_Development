import numpy as np
import random
import copy
count = 0

def minimax_algo(game,turn, alpha, beta, maxmin): 
    global total_state,total_maxmove
    total_state = total_state+1
    global count
    op_turn = change_turn(turn)    
    result = check_result(game)
    if(result != "no_winner_yet"):
        #count = count+1
        pass
    if(result == "draw"):
        return 0
    elif(result == "1st_player"):
        return 100
    elif(result == "2nd_player"):
        return -100
    if maxmin == True:
        total_maxmove = total_maxmove+1
        maxValue = float('-inf')
        for col in range(len(game)):
            if(game[rows-1][col] == 0):
                row = get_next_open_row(game, col)
                drop_piece(game, row, col, turn)
                
                result = minimax_algo(game,op_turn, alpha, beta,False)
                reverse_drop(game, row, col, turn)
                maxValue = max(maxValue,result)
                alpha = max(alpha,maxValue)
                if beta<=alpha:
                    break
        return maxValue 
    else:
        minValue = float('inf')
        for col in range(len(game)):
            if(game[rows-1][col] == 0):
                row = get_next_open_row(game, col)
                drop_piece(game, row, col, turn)
                result = minimax_algo(game,op_turn,alpha,beta,True)
                reverse_drop(game, row, col, turn)
                minValue = min(minValue,result)
                beta = min(minValue,beta)
                if(beta <= alpha):
                    break
        return minValue


def minimax_play(game,turn):
    max_result = float('-inf')
    final_row = -1
    final_col = -1
    for i in range(len(game[0])):
        if(game[rows-1][i] == 0):
            row = get_next_open_row(game, i)
            drop_piece(game, row, i, turn)
            op_turn = change_turn(turn)
            result = minimax_algo(game,op_turn,float('-inf'),float('inf'),False)
            reverse_drop(game, row, i, turn)
            if(result>max_result):
                max_result = result
                final_row = row
                final_col = i
            
    return final_col

import numpy as np


def create_game(rows,cols):
    game = np.zeros((rows, cols))
    return game

def drop_piece(game, row, col, piece):
    game[row][col] = piece
def reverse_drop(game, row, col, piece):
    game[row][col] = 0
def is_valid_location(game, col):
    try:
        return game[rows-1][col] == 0
    except:
        breakpoint()
def get_next_open_row(game, col):
    r = -1
    for r in range(rows):
        if game[r][col] == 0:
            return r
    

def print_game(game):
    print(np.flip(game, 0))

def winning_move(game, piece):
    # check horizontal locations
    for c in range(cols-3):
        for r in range(rows):
            if game[r][c] == piece and game[r][c+1] == piece and game[r][c+2] == piece and game[r][c+3] == piece:
                return True

    # check vertical locations
    for c in range(cols):
        for r in range(rows-3):
            if game[r][c] == piece and game[r+1][c] == piece and game[r+2][c] == piece and game[r+3][c] == piece:
                return True

    # check diagonal positive slope locations
    for c in range(cols-3):
        for r in range(rows-3):
            if game[r][c] == piece and game[r+1][c+1] == piece and game[r+2][c+2] == piece and game[r+3][c+3] == piece:
                return True

    # check diagonal negative slope locations
    for c in range(cols-3):
        for r in range(rows-3, rows):
            if game[r][c] == piece and game[r-1][c+1] == piece and game[r-2][c+2] == piece and game[r-3][c+3] == piece:
                return True

def check_result(game):

    if  winning_move(game, 1):
        return "1st_player"
    elif(winning_move(game, 2)):
        return "2nd_player"
    elif( np.all(game != 0)):
        return "draw"
    return "no_winner_yet"
def change_turn(turn):
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return turn

def random_player(game, piece,op_piece):
    possible_moves = []
    for col in actions:
        if is_valid_location(game, col):
            row = get_next_open_row(game, col)
            test_game = copy.deepcopy(game)
            drop_piece(test_game, row, col, op_piece)
            if winning_move(test_game, op_piece):
                return col
            test_game = copy.deepcopy(game)
            drop_piece(test_game, row, col, piece)
            if winning_move(test_game, piece):
                return col
            possible_moves.append(col)
    if possible_moves:
        return random.choice(possible_moves)
    

rows=4
cols=4
total_maxmove = 0
total_state = 0
def start_game():
    global count_q,count_mini,count_draw
    game = create_game(rows,cols)
    game_over = False
    turn = 0
    while check_result(game) == "no_winner_yet":
        # Ask for player input
        if turn == 0:
            print("minimax play")
            col = minimax_play(game,1)
            if is_valid_location(game, col):
                row = get_next_open_row(game, col)
                last_game = copy.deepcopy(game)
                drop_piece(game, row, col, 1)
                if winning_move(game, 1):
                    print("Player 1 wins!!!")
                    game_over = True
        else:
            print("random player play")
            col = random_player(game,2,1)
            while not (is_valid_location(game, col)):
                col = int(input("Player 2 make your selection (0-rows): "))
            if is_valid_location(game, col):
                row = get_next_open_row(game, col)
                drop_piece(game, row, col, 2)

        print_game(game)
        turn += 1
        turn = turn % 2
    result = check_result(game)
    if (result == "1st_player"):
        count_mini = count_mini+1
        print("minimax wins")
        #reward[state] = 200
    elif (result == "2nd_player"):#
        print("random player wins")
        count_q = count_q+1
        #reward[state] = -200
    elif(result == "draw"):
        count_draw = count_draw+1


    print("Thanks for playing Connectcols-3!")
actions = [*range(cols)]
count_mini = 0
count_q = 0
count_draw = 0
list_qwin = []
list_rwin = []
list_draw = []
list_count = []
for i in range(100):
    start_game()
    if i%10 == 0:
        print("i ="+str(i))
        sum = count_q+count_mini+count_draw
        count_qi = count_q/sum
        count_minii = count_mini/sum
        count_drawi = count_draw/sum
        count_q=0
        count_mini=0
        count_draw=0
        list_qwin.append(count_qi)
        list_rwin.append(count_minii)
        list_draw.append(count_drawi)
        list_count.append(i)
        print("minimax = " +str(count_qi) )
        print("random = "+ str(count_minii))
        print("draw = "+ str(count_drawi))

        

import matplotlib.pyplot as plt
plt.ylabel('Game result in %')
plt.xlabel('Game count')

plt.plot(list_count, list_draw, 'r-', label='Draw')
plt.plot(list_count, list_rwin, 'g-', label='Minimax wins')
plt.plot(list_count, list_qwin, 'b-', label='Random Player Wins')
plt.legend()
plt.show()



