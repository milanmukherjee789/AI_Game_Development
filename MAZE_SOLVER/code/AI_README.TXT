All the algorithms can be run from a single scriptcalled “main.py” 
Initially, inside the code folder , run : “python3 main.py”
The script will ask user for input to different variables.
All the parameters are customizable. For example: for BFS,DFS, and A* the customizable parameters are: 
1. maze size
2.  loopPercent of the maze
3.  target or goal cell


For MDP the customizable parameters are: 
1. maze size
2.  loopPercent of the maze 
3. target or goal cell 
4.  discount factor
5.  Noise (probability to move straight, right or left when policy is to move straight. ) 




Whenever a question is asked, give ‘y’ as answer for yes and ‘n’ as answer for no. User can either choose from existing size maze or can create of her own. 


Following are sample run:


DFS:
example 1)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> dfs
type 'y' if you want to use predefined maze?
>> y
give your maze name
 options:    name
 50*50 maze: 'maze5050.csv'
 30*30 maze: 'maze3030.csv'
 20*20 maze: 'maze2020.csv'
 10*10 maze: 'maze1010.csv'
 20*30 maze: 'maze2030.csv'
 80*80 maze: 'maze8080.csv'
>> maze8080.csv
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> y
maze solver is running. Grab a coffee or relax a bit :)




2)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> dfs
type 'y' if you want to use predefined maze?
>> n
Enter maze number of rows
>> 34
Enter maze number of cols
>> 32
type 'y' if you want to use defalt loopPercent of the maze? default = 10
>> n
input loopPercent raange 0-100
>> 34
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> n
give row number of goal state
>> 2
give column number of goal state
>> 3
maze solver is running. Grab a coffee or relax a bit :)




BFS:


1)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> bfs
type 'y' if you want to use predefined maze?
>> y
give your maze name
 options:    name
 50*50 maze: 'maze5050.csv'
 30*30 maze: 'maze3030.csv'
 20*20 maze: 'maze2020.csv'
 10*10 maze: 'maze1010.csv'
 20*30 maze: 'maze2030.csv'
 80*80 maze: 'maze8080.csv'
>> maze2020.csv
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> y
maze solver is running. Grab a coffee or relax a bit :)


2)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> bfs
type 'y' if you want to use predefined maze?
>> n
Enter maze number of rows
>> 23
Enter maze number of cols
>> 23
type 'y' if you want to use defalt loopPercent of the maze? default = 10
>> n
input loopPercent raange 0-100
>> 34
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> n
give row number of goal state
>> 23
give column number of goal state
>> 23
maze solver is running. Grab a coffee or relax a bit :)






A_Star:
1) 
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> astar
type 'y' if you want to use predefined maze?
>> y
give your maze name
 options:    name
 50*50 maze: 'maze5050.csv'
 30*30 maze: 'maze3030.csv'
 20*20 maze: 'maze2020.csv'
 10*10 maze: 'maze1010.csv'
 20*30 maze: 'maze2030.csv'
 80*80 maze: 'maze8080.csv'
>> maze2020.csv
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> y
maze solver is running. Grab a coffee or relax a bit :)




2)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> astar
type 'y' if you want to use predefined maze?
>> n
Enter maze number of rows
>> 34
Enter maze number of cols
>> 35
type 'y' if you want to use defalt loopPercent of the maze? default = 10
>> n
input loopPercent raange 0-100
>> 45
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> n
give row number of goal state
>> 2
give column number of goal state
>> 3
maze solver is running. Grab a coffee or relax a bit :)


Value Iteration:
Example 1)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> value
type 'y' if you want to use predefined maze?
>> y
give your maze name
 options:    name
 50*50 maze: 'maze5050.csv'
 30*30 maze: 'maze3030.csv'
 20*20 maze: 'maze2020.csv'
 10*10 maze: 'maze1010.csv'
 20*30 maze: 'maze2030.csv'
 80*80 maze: 'maze8080.csv'
>> maze3030.csv
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> y
type 'y' to use default discount factor? default 0.9
>> y
type 'y' to use default probability. Default is 0.8 for straght,0.1 for left and 0.1 for right
>> y
type 'y' to use default reward. Default is 0 for normal state and 1000 for goal state
>> y
maze solver is running. Grab a coffee or relax a bit :)


2)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> value
type 'y' if you want to use predefined maze?
>> n
Enter maze number of rows
>> 23
Enter maze number of cols
>> 23
type 'y' if you want to use defalt loopPercent of the maze? default = 10
>> n
input loopPercent raange 0-100
>> 23
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> n
give row number of goal state
>> 2
give column number of goal state
>> 3
type 'y' to use default discount factor? default 0.9
>> n
give your preferred discount factor
>> 0.8
type 'y' to use default probability. Default is 0.8 for straght,0.1 for left and 0.1 for right
>> n
give straight moving prob. sample: 0.8
>> 1
give right moving prob. sample: 0.1
>> 0
give left moving prob. sample 0.1
>> 0
type 'y' to use default reward. Default is 0 for normal state and 1000 for goal state
>> n
give reward for normal states apart from goal state
>> 0
give reward for goal states apart from goal state
>> 10000
maze solver is running. Grab a coffee or relax a bit :)
maze calculation running. Please give some time






Policy Iteration:
1)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> policy
type 'y' if you want to use predefined maze?
>> y
give your maze name
 options:    name
 50*50 maze: 'maze5050.csv'
 30*30 maze: 'maze3030.csv'
 20*20 maze: 'maze2020.csv'
 10*10 maze: 'maze1010.csv'
 20*30 maze: 'maze2030.csv'
 80*80 maze: 'maze8080.csv'
>> maze2020.csv
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> y
type 'y' to use default discount factor? default 0.9
>> y
type 'y' to use default probability. Default is 0.8 for straght,0.1 for left and 0.1 for right
>> y
type 'y' to use default reward. Default is 0 for normal state and 1000 for goal state
>> y
maze solver is running. Grab a coffee or relax a bit :)


2)
PS C:\Users\boyin\OneDrive\Documents\AI\assignment1\final> python3 .\main.py
Enter the algorithm you want to use:
 type 'policy' for policy iteration
 type 'value' for value_iteration
 type 'astar' for A_STAR
 type 'bfs' for Breadth First Search
 type 'dfs' for Depth First Search
>> policy
type 'y' if you want to use predefined maze?
>> n
Enter maze number of rows
>> 43
Enter maze number of cols
>> 43
type 'y' if you want to use defalt loopPercent of the maze? default = 10
>> n
input loopPercent raange 0-100
>> 23
type 'y' to use default goal state?default is (1,1) top left cell of the maze
>> n
give row number of goal state
>> 2
give column number of goal state
>> 3
type 'y' to use default discount factor? default 0.9
>> n
give your preferred discount factor
>> 0.8
type 'y' to use default probability. Default is 0.8 for straght,0.1 for left and 0.1 for right
>> n
give straight moving prob. sample: 0.8
>> 1
give right moving prob. sample: 0.1
>> 0
give left moving prob. sample 0.1
>> 0
type 'y' to use default reward. Default is 0 for normal state and 1000 for goal state
>> n
give reward for normal states apart from goal state
>> -12
give reward for goal states apart from goal state
>> 1000
maze solver is running. Grab a coffee or relax a bit :)