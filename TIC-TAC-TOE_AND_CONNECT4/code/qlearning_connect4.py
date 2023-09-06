import numpy as np
import random
count = 0
import copy

def get_state(game):
    state = ""
    for i in range(len(game)):
        for j in range(len(game[0])):
            state = state + str(int(game[i][j]))

    return state

def maxQ_value(state,game):
    global Q,N,reward,total_states , actions
    max_value = float('-inf')
    final_action = -1
    for action in actions:
        if(is_valid_location(game, action)):
            if (state,action) not in Q:
                Q[(state,action)] = 0
            if(Q[(state,action)]> max_value):
                max_value = Q[(state,action)]
                final_action = action
    return Q[(state,final_action)]

def maxQ(state,game):
    global Q,N,reward,total_states , actions
    max_value = float('-inf')
    final_action = -1
    for action in actions:
        if(is_valid_location(game, action)):
            if (state,action) not in Q:
                Q[(state,action)] = 0
            if(Q[(state,action)]> max_value):
                max_value = Q[(state,action)]
                final_action = action
    return final_action

def least_used_Q(state,game):
    global Q,N,reward,total_states, actions
    min_n = float('inf')
    final_action = -1
    for action in actions:
        
        if(is_valid_location(game, action)):
            if (state,action) not in N:
                N[(state,action)] = 0
                final_action = action
                break
            else:
                if N[(state,action)] < min_n:
                    min_n = N[(state,action)]
                    final_action = action
    
    return final_action



def explore_exploit(epsilon,action,state,game):
    global Q,N,reward,total_states
    if  random.uniform(0,1) < epsilon :        
        action = least_used_Q(state,game)
        N[(state,action)] = N[(state,action)]+1
    return action

def update_state(current_state,last_state,game,last_action,alpha,discount):
    global total_states
    total_states = total_states+1
    try:
        Q[(last_state,last_action)]  = (1-alpha)*Q[(last_state,last_action)] + alpha * (discount*maxQ_value(current_state,game) - Q[(last_state,last_action)])
    except:
        breakpoint()
def q_learning(game,alpha,discount,epsilon,current_state,last_state,last_action,first_step,play):
    global Q,N,reward,total_states

    #if not (first_step ):

        #update_state(current_state,last_state,game,last_action,alpha,discount,epsilon)

    action = maxQ(current_state,game)
    if (current_state,action) not in N:
        N[(current_state,action)] = 1
        
    else:
        N[((current_state,action))] = N[((current_state,action))]+1
    col = explore_exploit(epsilon,action,current_state,game)
    row = get_next_open_row(game, col)
    drop_piece(game, row, col, play)
    return col


#connect4 board


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

def check_result(game,turn):
    if(turn == 1):
        opturn = 2
    else:
        opturn = 1
    if  winning_move(game, turn):
        return "1st_player"
    elif(winning_move(game, opturn)):
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
rows=4
cols=4

def random_play(game):
    list1 = []
    for col in actions:
        if(is_valid_location(game,col)):
            list1.append(col)
    pos = random.randint(0,len(list1)-1)
    col = list1[pos]
    return col
    
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
    

def start_game():
    global count_q,count_mini,count_draw, alpha, discount, epsilon
    game = create_game(rows,cols)
    game_over = False
    #turn = int(input('type 0 for minimax to play first, type 1 for minimax to play second \n'))
    play = 1
    turn = 1
    result = "no_winner_yet"
    current_state = get_state(game)
    action = 0
    first_step = True
    update_list = []
    while check_result(game,play) == "no_winner_yet":
        # Ask for player input
        if((turn)%2 == 1):
            last_state = current_state
            current_state = get_state(game)
            last_action = action
            result = check_result(game,play)
            last_game = copy.deepcopy(game)
            reward[get_state(game)] = 0
            if not(first_step):
                update_list.append((current_state,last_state,copy.deepcopy(game),last_action))
            action = q_learning(game,alpha,discount,epsilon,current_state,last_state,last_action,first_step,play)
            first_step = False
            last_state = current_state
            turn=2
        else:
            try:
                col = random_player(game,2,1)
            except:
                breakpoint()        
            while not (is_valid_location(game, col)):
                col = int(input("Player 2 make your selection (0-rows): "))
            if is_valid_location(game, col):
                row = get_next_open_row(game, col)
                drop_piece(game, row, col, 2)
                if winning_move(game, 2):
                    #print("Player 2 wins!!!")
                    game_over = True
            turn = 1
        print_game(game)
    result = check_result(game,play)

    last_action = action

    if (result == "1st_player"):
        Q[(last_state,action)]  = 100
        count_q = count_q+1
        #reward[state] = 200
    elif (result == "2nd_player"):
        count_mini = count_mini+1
        Q[(last_state,action)]  = -100
        #reward[state] = -200
    elif(result == "draw"):
        count_draw = count_draw+1
        Q[(last_state,action)]  = 0
    update_list.reverse()
    for entry in range(len(update_list)):
        update_state(update_list[entry][0],update_list[entry][1],update_list[entry][2],update_list[entry][3],alpha,discount)
    #print("Thanks for playing Connect4!")
Q = {}
N = {}
reward = {}
total_states = 0
count_mini = 0
count_q = 0
count_draw = 0
epsilon = 0.9
alpha = 0.4
discount = 0.9
actions = [*range(cols)]
list_qwin = []
list_rwin = []
list_draw = []
list_count = []

for i in range(100):
    start_game()
    if i%10 == 0 and count_q+count_mini != 0:
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
        print("q-learning = " +str(count_qi) )
        print("random = "+ str(count_minii))
        print("draw = "+ str(count_drawi))
    if(i >200000):
        epsilon = 0.2
    if(i>300000):
        epsilon = 0
        

import matplotlib.pyplot as plt
plt.ylabel('Game result in %')
plt.xlabel('Game count')

plt.plot(list_count, list_draw, 'r-', label='Draw')
plt.plot(list_count, list_rwin, 'g-', label='Random player wins')
plt.plot(list_count, list_qwin, 'b-', label='Qlearning Wins')
plt.legend()
plt.show()


