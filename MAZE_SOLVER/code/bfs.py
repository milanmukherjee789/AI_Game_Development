from pyamaze import maze, COLOR, agent, textLabel
import sys


def handle_agent_movement(direction,square):
    next_move = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    return (square[0]+next_move[direction][0],square[1]+next_move[direction][1])
def backtrace(temp_goal,begin,journey):
    final = {}
    while begin != temp_goal:
        final[journey[temp_goal]] = temp_goal
        temp_goal = journey[temp_goal]
    return final
def Breadth_First(agent,goal):
    begin = (agent.rows,agent.cols)
    queue = [begin]
    visited = [begin]
    journey = {}
    count = 0
    while len(queue)>0:
        square = queue.pop(0) # first in first out
        count = count+1
        if square == None:
            break
        try:
            for direction in agent.maze_map[square]:
                if agent.maze_map[square][direction] == 1:
                    next_square = handle_agent_movement(direction,square)
                    if next_square in visited:
                        continue
                    journey[next_square] = square
                    visited.append(next_square)
                    queue.append(next_square)
                    if(next_square == goal):
                        break
        except:
            print("error")  
        if(next_square == goal):
            break
    temp_goal = goal
    final = backtrace(temp_goal,begin,journey)
    print("count: " + str(count))
    return final,count

arg={}
for i in range(1,len(sys.argv)):
    k,v = sys.argv[i].strip().split("=")
    arg[k] = v


def find_path(my_maze,goal):
    path,count=Breadth_First(my_maze,goal)
    return path,count