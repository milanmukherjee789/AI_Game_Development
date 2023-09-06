import sys
from pyamaze import maze, COLOR, agent, textLabel
from time import process_time
import time

algo = input("Enter the algorithm you want to use: \n type 'policy' for policy iteration \n type 'value' for value_iteration \n type 'astar' for A_STAR \n type 'bfs' for Breadth First Search \n type 'dfs' for Depth First Search \n>> ")

predefined_maze = input("type 'y' if you want to use predefined maze?\n>> ")
if(predefined_maze == "y"):
    maze_name = input("give your maze name\n options:    name\n 50*50 maze: 'maze5050.csv' \n 30*30 maze: 'maze3030.csv' \n 20*20 maze: 'maze2020.csv'\n 10*10 maze: 'maze1010.csv'\n 20*30 maze: 'maze2030.csv'\n 80*80 maze: 'maze8080.csv' \n>> ")
    my_maze=maze()
else:
    rows = int(input("Enter maze number of rows\n>> "))
    cols = int(input("Enter maze number of cols\n>> "))
    my_maze=maze(rows,cols)
    looppercent = input("type 'y' if you want to use defalt loopPercent of the maze? default = 10 \n>> ")
    if(looppercent != "y"):
        looppercent = int(input("input loopPercent raange 0-100\n>> "))
    else:
        looppercent = 10
goal_state = input("type 'y' to use default goal state?default is (1,1) top left cell of the maze\n>> ")
if(goal_state == "y"):
    goal = (1,1)
else:
    goal_row = int(input("give row number of goal state\n>> "))
    goal_col = int(input("give column number of goal state\n>> "))
    goal = (int(goal_row),int(goal_col))


if(algo == "policy" or algo == "value"):
    path_string = 'length of path'
    iteration_node = 'total iteration '
    discount_factor = input("type 'y' to use default discount factor? default 0.9\n>> ")
    if (discount_factor != "y"):
        discount_factor = float(input("give your preferred discount factor\n>> "))
    else:
        discount_factor = 0.9
    
    use_default_prob = input("type 'y' to use default probability. Default is 0.8 for straght,0.1 for left and 0.1 for right\n>> ")
    if(use_default_prob == "y"):
        prob = [0.8,0.1,0.1]

    else:
        straight_prob = float(input("give straight moving prob. sample: 0.8\n>> "))
        right_prob = float(input("give right moving prob. sample: 0.1\n>> "))
        left_prob = float(input("give left moving prob. sample 0.1\n>> "))
        prob = [straight_prob,right_prob,left_prob]

    use_default_reward = input("type 'y' to use default reward. Default is 0 for normal state and 1000 for goal state\n>> ")
    if(use_default_reward == "y"):
        reward_normal_state = 0
        reward_goal_state = 1000
    else:
        reward_normal_state = int(input("give reward for normal states apart from goal state\n>> "))
        reward_goal_state = int(input("give reward for goal states apart from goal state\n>> "))
else:
    path_string = 'length of path'
    iteration_node = 'total nodes traversed '

if(predefined_maze == "y"):
    my_maze.CreateMaze(goal[0],goal[1],loopPercent=10,loadMaze=maze_name)
else:
    my_maze.CreateMaze(goal[0],goal[1],loopPercent=10,saveMaze = True)

print("maze solver is running. Grab a coffee or relax a bit :) ")

t1_start = process_time() 
t1_wall_start = time.time()
if(algo == "policy"):
    import policy_iter
    final_path,count = policy_iter.find_path(my_maze,goal,discount_factor,prob,reward_normal_state,reward_goal_state)
elif(algo == "value"):
    import value_iter
    final_path,count = value_iter.find_path(my_maze,goal,discount_factor,prob,reward_normal_state,reward_goal_state)
elif(algo == "astar"):
    import a_star
    final_path,count = a_star.find_path(my_maze,goal)
elif(algo == "bfs"):
    import bfs
    final_path,count = bfs.find_path(my_maze,goal)
elif(algo == "dfs"):
    import dfs
    final_path,count = dfs.find_path(my_maze,goal)

t1_wall_stop = time.time()
t1_stop = process_time() 


try:
    my_agent=agent(my_maze,footprints=True)
    
    my_maze.tracePath({my_agent:final_path})
    
    my_path=textLabel(my_maze,path_string,len(final_path)+1)
    my_iteration=textLabel(my_maze,iteration_node,count)
    my_algo = textLabel(my_maze,"algorithm name",algo)
    
    wall_time_taken = textLabel(my_maze,"Wall time",t1_wall_stop-t1_wall_start)
    cpu_execution_time = textLabel(my_maze,"CPU execution time",t1_stop-t1_start)
    my_maze.run()
except:
    print("error at line 73 to 77 in main.py")
