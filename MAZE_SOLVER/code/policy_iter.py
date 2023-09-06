from pyamaze import maze, COLOR, agent, textLabel
import numpy as np
import copy


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D



def handle_agent_movement(direction,square):
    next_move = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    return (square[0]+next_move[direction][0],square[1]+next_move[direction][1])

def handle_agent_movement_prob(agent,direction,square,prob):
    next_move = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    moves = ['W','N','E','S']
    if(agent.maze_map[square][direction] == 1):
        straight_square = (square[0]+next_move[direction][0],square[1]+next_move[direction][1])
    else:
        straight_square = square
    if(moves.index(direction) == 3):
        right_direction = moves[0]
    else:    
        right_direction = moves[moves.index(direction)+1]
    if(agent.maze_map[square][right_direction] == 1):
        right_square = (square[0]+next_move[right_direction][0],square[1]+next_move[right_direction][1])
    else:
        right_square = square

    left_direction = moves[moves.index(direction)-1]
    if(agent.maze_map[square][left_direction] == 1):
        left_square = (square[0]+next_move[left_direction][0],square[1]+next_move[left_direction][1])
    else:
        left_square = square

    P={"straight":{"prob": prob[0],"square":straight_square},"right":{"prob": prob[1],"square":right_square},"left":{"prob": prob[2],"square":left_square}}

    return P

def find_direction(square,next_square):
    move={(0,1):'E',(0,-1):'W',(-1,0):'N',(1,0):'S'}
    return move[(next_square[0]-square[0],next_square[1]-square[1])]

def pol_iter(agent,rows,cols,discount,reward,delta,policy,prob,goal):
    value = {}
    for i in range(1,agent.rows+1):
        for j in range(1,agent.cols+1):
            value[(i,j)] =  0
    value[goal] = reward[goal]

    error = float('inf')
    count = 0
    check_no_change = False
    temp_policy={}

    while True:
        count = count+1

        #policy evaluation

        while(delta<error):
            temp_error = float("-inf")

            for square in agent.maze_map:
                if (square == goal):
                    value[(square)] = reward[goal]
                    continue
                next_square = policy[square]
                temp_score = value[square]

                #asynchronous update of uitility

                if( agent.maze_map[square][find_direction(square,next_square)] == 1):
                    next_square = handle_agent_movement_prob(agent,find_direction(square,next_square),square,prob)
                    direction_score = reward[square]+(discount*value[next_square["straight"]["square"]]*next_square["straight"]["prob"])+(discount*value[next_square["right"]["square"]]*next_square["right"]["prob"])+(discount*value[next_square["left"]["square"]]*next_square["left"]["prob"])
                    value[square] = direction_score

                if (abs(temp_score-value[square]) > temp_error):
                    temp_error = abs(temp_score-value[square]) 
            error = temp_error

    

        #policy improvement code

        for square in agent.maze_map:
            temp_score = float("-inf")

            if(square == goal):
                continue
            for direction in agent.maze_map[square]:

                if agent.maze_map[square][direction] == 1:
                    next_square = handle_agent_movement_prob(agent,direction,square,prob)
                    direction_square = reward[square]+(discount*value[next_square["straight"]["square"]]*next_square["straight"]["prob"])+(discount*value[next_square["right"]["square"]]*next_square["right"]["prob"])+(discount*value[next_square["left"]["square"]]*next_square["left"]["prob"])

                    if direction_square > temp_score:
                        temp_score = direction_square
                        temp_policy[square] = next_square["straight"]["square"]
        if(temp_policy == policy):
            break
        else:
            policy = copy.deepcopy(temp_policy)
            error = float('inf')
    return policy,count



def find_path(my_maze,goal,discount_factor,prob,reward_normal_state,reward_goal_state):
    
    rows = my_maze.rows
    cols = my_maze.cols
    reward = {}
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            reward[(i,j)] =  reward_normal_state
    reward[goal] = reward_goal_state
    policy = {}


    for square in my_maze.maze_map:
        if(square == goal):
            continue
        for direction in my_maze.maze_map[square]:
            if my_maze.maze_map[square][direction] == 1:
                next_square = handle_agent_movement(direction,square)
                policy[square] = next_square
    prob = [1,0,0]
    path,count = pol_iter(my_maze,rows,cols,discount_factor,reward,0.001,policy,prob,goal)

    start = (rows,cols)
    final_path = {}

    while start != goal:
        final_path[start] = path[start]
        start = path[start]
    return final_path,count

