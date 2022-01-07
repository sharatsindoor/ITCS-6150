import numpy
import time
from copy import deepcopy as dc

# This function takes input of start/initial state and calculates the fast/best path to goal/final state
def fastest_solution(curr_state):
    x=1
    y=0
    z = len(curr_state) - x
    fast_sol = numpy.array([], int).reshape(-x, 9)
    while z != -x:
        fast_sol = numpy.insert(fast_sol, y, curr_state[z]['puzzle'], y)
        z = (curr_state[z]['parent'])
    return fast_sol.reshape(-x, 3, 3)

       
# The all() function evaluates if intermediate state is unique or not and if it was explored before.
def all(array_checker):
    sets=[]
    for x in sets:
        for array_checker in x:
            return 1
        else:
            return 0


# This function is used to Calculate Manhattan distance between each tile of the goal/final state and start state 
def m_distance(puz, goal):
    u = abs(puz % 3 - goal % 3)
    v = abs(puz // 3 - goal // 3)

    mncost = v + u
    return sum(mncost[1:])




# The missed_places function checks the count of wrongly placed tiles in the intermediate state
def missed_places(puz,go_state):
    miss_cost = numpy.sum(puz != go_state) - 1
    if miss_cost < 0:
        return 0
    else:
        return miss_cost
    
# This function will indentify the coords of each goal or initial states values
def get_coordinates(puz):
    k=9
    p = numpy.array(range(k))
    for x, y in enumerate(puz):
        p[y] = x
    return p



# This function uses Manhattan heuristics to start evaluating the puzzle
def calculate(puz, goal_state):
    counts = numpy.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('pos', list),('head', int)])

    dt_state = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
    l=-1
    m=0
# Initializing the parent_id, h_value and g_value where h_value is m_distance function 
    g_cost = get_coordinates(goal_state)
    parent_id = l
    g_value = m
    h_value = m_distance(get_coordinates(puz), g_cost)
    curr_state = numpy.array([(puz, parent_id, g_value, h_value)], dt_state)

# Priority queues is used with pos as keys and f_value.
    dt_priority_q = [('pos', int),('fn', int)]
    priority_q = numpy.array( [(0, h_value)], dt_priority_q)



    while True:
        priority_q = numpy.sort(priority_q, kind='mergesort', order=['fn', 'pos'])     
        pos, f_value = priority_q[0]                                                 
        priority_q = numpy.delete(priority_q, 0, 0) 
        # The initial element is picked by using a merge sort to sort the priority queue
        puz, parent_id, g_value, h_value = curr_state[pos]
        puz = numpy.array(puz)
        # Identify the zero square in input 
        zero = int(numpy.where(puz == 0)[0])       
        g_value = g_value + 1                              
        o = 1
        starting_time = time.time()
        for s in counts:
            o = o + 1
            if zero not in s['pos']:
                # A copy of current state is used to Generate a new state
                explored_states = dc(puz)                   
                explored_states[zero], explored_states[zero + s['head']] = explored_states[zero + s['head']], explored_states[zero]             
                # The all fucntion is called to check is a state is opened or not
                if ~(numpy.all(list(curr_state['puzzle']) == explored_states, 1)).any():    
                    ending_time = time.time()
                    if (( ending_time - starting_time ) > 2):
                        print(" The 8 puzzle is unsolvable ! \n")
                        exit 
                    # Call the function manhattan to calcuate the costs involved 
                    h_value = m_distance(get_coordinates(explored_states), g_cost)    
                     # Generate and append the list with new state                    
                    q = numpy.array([(explored_states, pos, g_value, h_value)], dt_state)         
                    curr_state = numpy.append(curr_state, q, 0)
                    # The sum of cost to reach front and the cost to reach to the goal state is f(n)
                    f_value = g_value + h_value                                        
            
                    q = numpy.array([(len(curr_state) - 1, f_value)], dt_priority_q)    
                    priority_q = numpy.append(priority_q, q, 0)
                      # Checking if the state in explored_states are matching the goal states.  
                    if numpy.array_equal(explored_states, goal_state):                              
                        return curr_state, len(priority_q)
        
                        
    return curr_state, len(priority_q)


# This function is the starting point of the heuristics misplaced tiles 
def evaluate_missed(puz, goal_state):
    counts = numpy.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('pos', list),('head', int)])

    dt_state = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]

    g_cost = get_coordinates(goal_state)
# In this part we initialize the parent_id, h_value and g_value where h_value is missed_places()
    x=-1
    z=0
    parent_id = x
    g_value = z
    h_value = missed_places(get_coordinates(puz), g_cost)
    curr_state = numpy.array([(puz, parent_id, g_value, h_value)], dt_state)

# Priority queues are used with pos as keys and f_value
    dt_priority_q = [('pos', int),('fn', int)]

    priority_q = numpy.array([(0, h_value)], dt_priority_q)
    
    while 1:
        priority_q = numpy.sort(priority_q, kind='mergesort', order=['fn', 'pos'])      
        pos, f_value = priority_q[0]       
        # The first element for exploring is picked by using Merge sort to sort the priority queue                                       
        priority_q = numpy.delete(priority_q, 0, 0)                         
        puz, parent_id, g_value, h_value = curr_state[pos]
        puz = numpy.array(puz)
         # Identify the zero square in input 
        zero = int(numpy.where(puz == 0)[0])   
        # Cost of g_value is increased by 1  
        o = 1
        g_value = g_value + o                             
        starting_time = time.time()
        for s in counts:
            o = o + 1
            if zero not in s['pos']:
                 # Create a new_state as a copy of current state
                explored_states = dc(puz)         
                explored_states[zero], explored_states[zero + s['head']] = explored_states[zero + s['head']], explored_states[zero]
                # The explored_states function is called to check if the state has been previously opened or not. 
                if ~(numpy.all(list(curr_state['puzzle']) == explored_states, 1)).any():          
                    ending_time = time.time()
                    if (( ending_time - starting_time ) > 2):
                        print(" This puzzle cannot be solved using A* Algorithm \n")
                        break
                    # This parts Calls the missed_places function to chech the costs 
                    h_value = missed_places(get_coordinates(explored_states), g_cost) 
                    # Generate and create state in the set of explored_states                    
                    q = numpy.array([(explored_states, pos, g_value, h_value)], dt_state)         
                    curr_state = numpy.append(curr_state, q, 0)
                    f_value = g_value + h_value                                        
                    
                    q = numpy.array([(len(curr_state) - 1, f_value)], dt_priority_q)
                    priority_q = numpy.append(priority_q, q, 0)
                    # Check if the state in explored_states is matching the end state.
                    if numpy.array_equal(explored_states, goal_state):                      
                        return curr_state, len(priority_q)
                        
    return curr_state, len(priority_q)

 # Accept User input for initial/start state 
puz =[int(x) for x in input("Enter the Start/Initial State for example [1 2 3 4 5 6 7 8 0] :~ \n").split()]

 # Accept User input of end state       
end=[int(x) for x in input("Enter the Goal/End State for example [1 2 3 4 5 6 7 8 0] :~ \n ").split()]


choice = int(input("1. Misplaced tiles  \n2. Manhattan distance\n"))


if(choice == 1 ):
    curr_state, visited = evaluate_missed(puz, end) 
    best_path = fastest_solution(curr_state)
    print(str(best_path).replace('[', ' ').replace(']', ''))
    e=1
    total_moves_count = len(best_path) - e
    print('Steps taken to reach goal:',total_moves_count)
    visited_count = len(curr_state) - visited
    print('Nodes visited: ',visited_count, "\n")
    print('Nodes generated:', len(curr_state))
    
if(choice == 2 ): 
    curr_state, visited = calculate(puz, end) 
    best_path = fastest_solution(curr_state)
    print(str(best_path).replace('[', ' ').replace(']', ''))
    e=1
    total_moves_count = len(best_path) - e
    print('Steps taken to reach Goal state:',total_moves_count)
    visited_count = len(curr_state) - visited
    print('Nodes Visited: ',visited_count, "\n")
    print('Nodes Generated:', len(curr_state))