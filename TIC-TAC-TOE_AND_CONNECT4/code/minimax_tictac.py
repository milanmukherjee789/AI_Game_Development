import random

def PrintGame(game):
    for i in range(len(game)):
        if game[i] == 0:
            value = "_"
        else:
            value = game[i]
        print(value, end=" ")
        if((i+1)%3 == 0):
            print("\n")

def check_result(game):
    for sequence in winning_sequence():
        if(game[sequence[0]] != 0 and game[sequence[0]] == game[sequence[1]] and game[sequence[1]]==game[sequence[2]]):
            if game[sequence[0]] == "x":
                return "minimax_wins"
            else: 
                return "random_player_wins"
    if 0 in game:
        return "no_winner_yet"
    return "draw"

def minimax_algo(game, alpha, beta, maxmin): 
    global total_state,total_max
    total_state = total_state+1
    
    result = check_result(game)
    if(result == "draw"):
        return 0
    elif(result == "minimax_wins"):
        return 100
    elif(result == "random_player_wins"):
        return -100
    if maxmin == True:
        total_max= total_max+1
        maxValue = float('-inf')
        for square_index in range(len(game)):
            if(game[square_index] == 0):
                game[square_index] = "x"
                result = minimax_algo(game, alpha, beta,False)
                game[square_index] = 0
                maxValue = max(maxValue,result)
                alpha = max(alpha,maxValue)
                if beta<=alpha:
                    break
        
        return maxValue 
    else:
        minValue = float('inf')
        for square_index in range(len(game)):
            if(game[square_index] == 0):
                game[square_index] = "o"
                result = minimax_algo(game,alpha,beta,True)
                game[square_index] = 0
                minValue = min(minValue,result)
                beta = min(minValue,beta)
                if(beta <= alpha):
                    break
        return minValue

def minimax_play(game):
    max_result = float('-inf')
    index = -1
    for i in range(len(game)):
        if(game[i] == 0):
            game[i] = "x"
            result = minimax_algo(game,float('-inf'),float('inf'),False)
            game[i] = 0
            if(result>max_result):
                max_result = result
                index = i
    
    game[index] = "x"
    return game

def winning_sequence():
    return [[2,4,6],[0,4,8],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
def find_prob_loss(index1,index2,index3,sequence,game):
    return (game[sequence[index3]] == 0 and game[sequence[index1]] == "x" and game[sequence[index1]] == game[sequence[index2]])
def find_prob_win(index1,index2,index3,sequence,game):
    return (game[sequence[index3]] == 0 and game[sequence[index1]] == "o" and game[sequence[index1]] == game[sequence[index2]])
def random_play(game):
    for sequence in winning_sequence():
        if find_prob_win(0,1,2,sequence,game) :
            game[sequence[2]] = "o"
            return sequence[2]
        elif find_prob_win(1,2,0,sequence,game):
            game[sequence[0]] = "o"
            return sequence[0]
        elif find_prob_win(0,2,1,sequence,game):
            game[sequence[1]] = "o"
            return sequence[1]
         
    for sequence in winning_sequence():
        if find_prob_loss(0,1,2,sequence,game) :
            game[sequence[2]] = "o"
            return sequence[2]
        elif find_prob_loss(1,2,0,sequence,game):
            game[sequence[0]] = "o"
            return sequence[0]
        elif find_prob_loss(0,2,1,sequence,game):
            game[sequence[1]] = "o"
            return sequence[1]
    list1 = []
    for i in range(len(game)):
        if(game[i] == 0):
            list1.append(i)
    pos = random.randint(0,len(list1)-1)   
    return list1[pos]

def user_play(game):
    position = input('input the box number you chose. range(1-9) \n')
    if game[int(position)-1] != 0:
        print("Wrong Move")
        exit(1)
    game[int(position)-1] = 'o'
    return game

def start_game():
    global count_q,count_mini,count_draw
    game = [0] * 9
    play = 1
    
    result = "no_winner_yet"
    for square_index in range(len(game)):
        result = check_result(game)
        if(result != "no_winner_yet"):
            break;
        elif((square_index+play)%2 != 1):
            
            print("minimax turn")
            PrintGame(game)
            game = minimax_play(game)
        else:
            print("random play turn")
            PrintGame(game)
            #random_play(game)
            pos = random_play(game)
            game[pos] = "o"
    result = check_result(game)
    if(result == "minimax_wins"):
        count_q = count_q+1
        PrintGame(game)
        print("minimax_wins")
    elif(result == "random_player_wins"):
        count_mini = count_mini+1
        PrintGame(game)
        print("random_player_wins")
    elif(result == "draw"):
        count_draw = count_draw+1
        PrintGame(game)
        print("It's a draw")

count_mini = 0
count_q = 0
count_draw = 0
list_qwin = []
list_rwin = []
list_draw = []
list_count = []
total_state = 0
total_max = 0

for i in range(1000):
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

import matplotlib.pyplot as plt
plt.ylabel('Game result in %')
plt.xlabel('Game count')

plt.plot(list_count, list_draw, 'r-', label='Draw')
plt.plot(list_count, list_rwin, 'g-', label='Random player wins')
plt.plot(list_count, list_qwin, 'b-', label='Minimax Wins')
plt.legend()
plt.show()