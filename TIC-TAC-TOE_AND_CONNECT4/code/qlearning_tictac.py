import copy
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
def PrintGame2(game):
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
                return "qlearning_wins"
            else: 
                return "random_player_wins"
    if 0 in game:
        return "no_winner_yet"
    return "draw"

def get_state(game):
    return "".join(str(value) for value in game )

def maxQ_value(state,game):
    global Q,N,reward,total_states , actions
    max_value = float('-inf')
    final_action = -1
    for action in actions:
        if(game[action] == 0):
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
        if(game[action] == 0):
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
        if(game[action] == 0):
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

def update_state(current_state,last_state,game,last_action,alpha,discount,epsilon_first_step):
    global total_states
    total_states = total_states+1
    try:
        abcd  = (1-alpha)*Q[(last_state,last_action)] + alpha * (N[(last_state,last_action)]/total_states)* (discount*maxQ_value(current_state,game) - Q[(last_state,last_action)])
        if(Q[(last_state,last_action)] >5):
            
            Q[(last_state,last_action)] = abcd
        else:
            Q[(last_state,last_action)] = abcd
    except:
        breakpoint()
def q_learning(game,alpha,discount,epsilon,current_state,last_state,last_action,first_step):
    global Q,N,reward,total_states
    if not (first_step ):
        update_state(current_state,last_state,game,last_action,alpha,discount,epsilon)

    action = maxQ(current_state,game)
    if (current_state,action) not in N:
        N[(current_state,action)] = 1
        
    else:
        N[((current_state,action))] = N[((current_state,action))]+1
    action = explore_exploit(epsilon,action,current_state,game)
    game[action] = "x"
    return action
    
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
    global count_q,count_mini,count_draw, alpha, discount, epsilon
    game = [0] * 9
    #play = int(input('type 1 for minimax to play first, type 2 for minimax to play second \n'))
    play = 1
    result = "no_winner_yet"
    current_state = get_state(game)
    action = 0
    first_step = True
    while check_result(game) == "no_winner_yet":
        if((play+1)%2 != 1):
            print("q-agent turn")
            PrintGame(game)

            last_state = current_state
            current_state = get_state(game)
            last_action = action
            result = check_result(game)
            last_game = copy.deepcopy(game)
            reward[get_state(game)] = 0
            action = q_learning(game,alpha,discount,epsilon,current_state,last_state,last_action,first_step)
            first_step = False
            #last_game = copy.deepcopy(game)
            
            last_state = current_state
        else:
            print("random play turn")
            PrintGame(game)
            pos = random_play(game)
            game[pos] = "o"
            #game = user_play(game)
        play = (play+1)%2
    result = check_result(game)
    
    last_action = action
    if (result == "qlearning_wins"):
        Q[(last_state,action)]  = 100
        count_q = count_q+1
        PrintGame(game)
        #reward[state] = 200
    elif (result == "random_player_wins"):
        Q[(last_state,action)]  = -100
        count_mini = count_mini+1
        PrintGame(game)
        #reward[state] = -200
    elif(result == "draw"):
        count_draw = count_draw+1
        PrintGame(game)
        Q[(last_state,action)]  = 0


Q = {}
N = {}
reward = {}
total_states = 0
count_mini = 0
count_q = 0
count_draw = 0
epsilon = 0.4
alpha = 0.9
discount = 0.9
actions = [0,1,2,3,4,5,6,7,8]
list_qwin = []
list_rwin = []
list_draw = []
list_count = []
for i in range(1,800001):
    start_game()

    if i%10000 == 0 and count_q+count_mini != 0:
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
    if(i >500000):
        epsilon = 0.2
    if(i>700000):
        epsilon = 0



import matplotlib.pyplot as plt
plt.ylabel('Game result in %')
plt.xlabel('Game count')

plt.plot(list_count, list_draw, 'r-', label='Draw')
plt.plot(list_count, list_rwin, 'g-', label='Random player wins')
plt.plot(list_count, list_qwin, 'b-', label='Qlearning Wins')
plt.legend()
plt.show()

