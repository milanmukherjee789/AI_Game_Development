from pyamaze import maze, COLOR, agent, textLabel

def my_heuristic(squareA,squareB):
    x1,y1=squareA
    x2,y2=squareB
    return abs(x1-x2) + abs(y1-y2)
    
def handle_agent_movement(direction,square):
    next_move = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    return (square[0]+next_move[direction][0],square[1]+next_move[direction][1])
def backtrace(temp_goal,begin,journey):
    final = {}
    while begin != temp_goal:
        final[journey[temp_goal]] = temp_goal
        temp_goal = journey[temp_goal]
    return final
def a_star(agent,goal):
    begin = (agent.rows,agent.cols)
    previous_cost = {}

    total_cost = {}
    visited = [begin]
    goal = goal
    for i in range(1,agent.rows+1):
        for j in range(1,agent.cols+1):
            previous_cost[(i,j)] =  float('inf')
            total_cost[(i,j)] =  float('inf')
    previous_cost[begin] = 0
    total_cost[begin] = my_heuristic(begin,goal)


    queue = [(total_cost[begin],begin)]

    journey = {}
    count = 0

    while len(queue)>0:
        square_tuple = min(queue) 
        queue.remove(square_tuple)
        square = square_tuple[1]
        count = count+1
        if square == None or square == goal:
            break
        try:
            
            for direction in agent.maze_map[square]:
                
                if agent.maze_map[square][direction] == 1:
                    next_square = handle_agent_movement(direction,square)
                    next_square_cost = previous_cost[square]+1 + my_heuristic(next_square,goal)

                    if next_square in visited:
                        if next_square_cost < total_cost[next_square]:
                            previous_cost[next_square] = previous_cost[square]+1
                            total_cost[next_square] = next_square_cost
                            queue.append((total_cost[next_square],next_square))
                            journey[next_square] = square
                    else:
                        previous_cost[next_square] = previous_cost[square]+1
                        total_cost[next_square] = previous_cost[square]+1 + my_heuristic(next_square,goal)
                        queue.append((total_cost[next_square],next_square))
                        journey[next_square] = square
                        visited.append(next_square)
                
        except:
            print("error")    
    temp_goal = goal
    final = backtrace(temp_goal,begin,journey)
    print("count: " + str(count))
    return final,count




def find_path(my_maze,goal):
    path,count=a_star(my_maze,goal)
    return path,count