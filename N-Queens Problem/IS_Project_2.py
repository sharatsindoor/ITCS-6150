import copy
from random import randrange as rr
from random import randint as ri

class state_board():
    def __init__(self, n):
        self.n = n
        self.state_board= [[0 for uu in range (0,self.n)] for vv in range (0,self.n)]
        for uu in range(0, n):
            while 1:
                ran_row = ri(0,n-1)
                ran_col = uu
                #insert queens in different columns
                if self.state_board[ran_row][ran_col] == 0:
                    self.state_board[ran_row][ran_col] = 'Q'
                    break

#This function prints state of N cross N board 
def display_state(state_s):
        for uu in range(n):
            table = ""
            for vv in range(n):
                table += str(state_s[uu][vv])+" "
            print(table)
        print("")
        
def eval_h_values(the_board,n):
    expense = 0
    for uu in range(0,n):
        for vv in range(0,n):
            if the_board.state_board[uu][vv]=='Q':
                #checking in rows
                for ww in range(vv+1,n): 
                    if the_board.state_board[uu][ww] == 'Q' :
                        expense+=1
                uuu,vvv=uu+1,vv+1
                #checking the diagonals
                while (uuu<n and vvv<n):
                    if the_board.state_board[uuu][vvv] == 'Q':
                        expense+=1
                    uuu=uuu+1
                    vvv=vvv+1
                uuu,vvv=uu-1,vv+1
                while (uuu>=0 and vvv<n):
                    if the_board.state_board[uuu][vvv] == 'Q':
                        expense+=1
                    uuu=uuu-1
                    vvv=vvv+1                
    return expense

def eval_state_min(the_board,n):
    temp_list = []
    lowest_expense=eval_h_values(the_board,n)
    for uu in range(0,n):
        for vv in range(0,n):
            if the_board.state_board[vv][uu]=='Q':
                #Trying various arrangements by shifting the queen from the column
                for uuu in range(0,n):
                        if the_board.state_board[uuu][uu]!='Q' :
                            next_board_state = copy.deepcopy(the_board)
                            next_board_state.state_board[vv][uu]=0
                            next_board_state.state_board[uuu][uu]='Q'
                            expense=eval_h_values(next_board_state, n)
                            if expense < lowest_expense:
                                temp_list.clear()
                                lowest_expense = expense
                                temp_list.append([uuu,uu])
                            elif expense == lowest_expense:
                                temp_list.append([uuu,uu])
    
    return temp_list,lowest_expense

# This Function runs the hill climbing algorithm
def simple_hill_climbing_algo(state_board,iteration_number):
    step_number=0
    valuation = eval_h_values(state_board,n)
    if (iteration_number < 4):
        print('\nThe searching sequence for random configuration: ', iteration_number + 1)
        iteration_count = 0
    while 1:
        if (iteration_number < 4):
            display_state(state_board.state_board)
            iteration_count += 1
        if valuation == 0:
            break
        else:
            step_number += 1
            temp_list,expense = eval_state_min(state_board,n)
            if valuation <= expense or len(temp_list) == 0:
                break
            else:
                ran_indexing = rr(0,len(temp_list))                           
                index = temp_list[ran_indexing]
                valuation = expense
                for uu in range (0,n):
                        state_board.state_board[uu][index[1]]=0
                state_board.state_board[index[0]][index[1]]='Q'

    if (iteration_number < 4):
        #Printing if calculation is a failure or success 
        if valuation == 0:
            print("Success")
        else:
            print("Failure")
        print('Number of steps: ',iteration_count-1)
        print('~~~~~~~~~~~~~~~~~~~~')
    if valuation == 0:
        return 1, step_number
    return 0, step_number

# This function is for hill climbing using sideways movement
def hill_climbing_algo_with_sideways(the_board, iteration_number):
    step_number = 0
    side_ways_count=0
    bs = the_board
    cost_current = eval_h_values(bs, n)
    if (iteration_number < 4):
        print('\nThe searching sequence for random configuration: ', iteration_number + 1)
        iteration_count = 0
    while step_number<cent:
        if (iteration_number < 4):
            display_state(bs.state_board)
            iteration_count += 1
        if cost_current == 0:
            break
        else:
            step_number += 1
            temp_list, expense = eval_state_min(bs, n)
            if cost_current < expense:
                break
            if len(temp_list) == 0:
                break
            else:
                if cost_current == expense:
                    side_ways_count+=1
                else:
                    side_ways_count=0
                ran_indexing = rr(0, len(temp_list))
                index = temp_list[ran_indexing]
                cost_current = expense
                for uu in range(0, n):
                    bs.state_board[uu][index[1]] = 0
                bs.state_board[index[0]][index[1]] = 'Q'
    #printing if calculation is a failure or success
    if (iteration_number < 4):
        if cost_current == 0:    
            print("Success")
        else:
            print("Failure")
        print('Number of steps: ',iteration_count-1)
        print('~~~~~~~~~~~~~~~~~~~~')
    if cost_current == 0:
        return 0, step_number
    return 1, step_number

# This Function runs the hill climbing algorithm with random restart without sideways movement
def hill_climbing_algo_random_restart(the_board):
     
    no_of_restarts=0
    step_number=0
    bs= the_board
    previous_h_val = eval_h_values(bs, n)
    while 1:
        if previous_h_val == 0:
            break
        else:
            step_number += 1
            temp_list,h_val = eval_state_min(bs,n)
            if previous_h_val <= h_val or len(temp_list) == 0:
                no_of_restarts += 1
                bs = state_board(n)
                previous_h_val = eval_h_values(bs, n)
                continue 

            ran_indexing = rr(0,len(temp_list))
            index = temp_list[ran_indexing]
            previous_h_val = h_val
            for uu in range (0,n):
                    bs.state_board[uu][index[1]]=0
            bs.state_board[index[0]][index[1]]='Q'
    
    if previous_h_val == 0:
        return 0, step_number, no_of_restarts
    return 1, step_number, no_of_restarts

# This Function runs the hill climbing algorithm with sideways movement
def random_restart_hill_climbing_algo_with_sideways(the_board):
    step_number = 0
    side_ways_count=0
    no_of_restarts = 0
    bs = the_board
    previous_h_val = eval_h_values(bs, n)
    while 1:
        if previous_h_val == 0:
            break
        else:
            step_number += 1
            temp_list, h_val = eval_state_min(bs, n)
            if previous_h_val < h_val or len(temp_list) == 0:
                bs=state_board(n)
                previous_h_val = eval_h_values(bs, n)
                no_of_restarts += 1
                side_ways_count=0
                continue
            
            if previous_h_val == h_val:
                side_ways_count+=1
                if step_number >= cent:
                    bs=state_board(n)
                    previous_h_val = eval_h_values(bs, n)
                    no_of_restarts += 1
                    side_ways_count=0
            else:
                side_ways_count=0

            ran_indexing = rr(0, len(temp_list))
            index = temp_list[ran_indexing]
            previous_h_val = h_val
            for uu in range(0, n):
                bs.state_board[uu][index[1]] = 0
            bs.state_board[index[0]][index[1]] = 'Q'

    if previous_h_val == 0:
        return 0, step_number, no_of_restarts
    return 1, step_number, no_of_restarts

#The main function running the Hill climbing algorithm for N-queens solution
def main():
    global n
    global iterations
    global cent
    z=0
    cent=100
    successful_steps_count = 0
    failure_step_count = 0
    successful_iterations_count = 0
    fail_iterations_count = 0
    try: 
        iterations=100
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    N-Queens Problem    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        n = int(input("\nPlease enter the Number of Queens: "))
        print("___________________________________________________________________________________________")
        print("\n\t\t\t~~~~:Hill Climbing:~~~~ ") 
        print("\nCalculating...")    
        for uu in range(0,iterations):
            bs = state_board(n)  
            valuation,step_number = simple_hill_climbing_algo(bs,uu)
            if valuation == 0:
                fail_iterations_count +=1
                failure_step_count += step_number
            else:
                successful_iterations_count +=1
                successful_steps_count += step_number
           
        rate_of_success=(successful_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        rate_of_failure=(fail_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        print("\nSuccess rate is: ",round(rate_of_success,2),"% and Failure rate is: ",round(rate_of_failure,2),"%")
        if successful_iterations_count != 0:
            print("\nThe average number of steps when the algorithm succeeds: ", round(successful_steps_count / successful_iterations_count, 2))
        if fail_iterations_count != 0:
            print("\nThe average number of steps when the algorithm fails: ", round(failure_step_count / fail_iterations_count, 2))
        print("___________________________________________________________________________________________")
        print("\n\t\t\t~~~~:Hill-climbing search with sideways move:~~~~ ")
        print("\n Calculating...")
        successful_steps_count = z
        failure_step_count = z
        successful_iterations_count = z
        fail_iterations_count = z
        for uu in range(0, iterations):
            bs = state_board(n)
            valuation, step_number = hill_climbing_algo_with_sideways(bs,uu)
            if valuation == 1:
                fail_iterations_count += 1
                failure_step_count += step_number
            else:
                successful_iterations_count += 1
                successful_steps_count += step_number
        rate_of_success = (successful_iterations_count / (successful_iterations_count + fail_iterations_count)) * cent
        rate_of_failure = (fail_iterations_count / (successful_iterations_count + fail_iterations_count)) * cent
        print("\nSuccess rate is: ", round(rate_of_success,2), "% and Failure rate is: ", round(rate_of_failure,2), "%")
        if successful_iterations_count!=0:
            print("\nThe average number of steps when the algorithm succeeds: ", round(successful_steps_count / successful_iterations_count,2))
        if fail_iterations_count!=0:
            print("\nThe average number of steps when the algorithm fails: ", round(failure_step_count / fail_iterations_count,2))
        print("___________________________________________________________________________________________")
        print("\n\t\t\t~~~~:Random-restart hill-climbing search without sideways move:~~~~ ")
        print("\n Calculating...")
        successful_steps_count = z
        failure_step_count = z
        successful_iterations_count = z
        fail_iterations_count = z
        final_restarting_count = z
        for uu in range(0,iterations):
            bs = state_board(n)  
            valuation, step_number, final_restart_count = hill_climbing_algo_random_restart(bs)
            if valuation == 1:
                fail_iterations_count +=1
                failure_step_count += step_number
            else:
                successful_iterations_count +=1
                successful_steps_count += step_number
            final_restarting_count += final_restart_count
        rate_of_success=(successful_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        rate_of_failure=(fail_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        print("\nSuccess rate is: ",round(rate_of_success,2),"% and Failure rate is: ",round(rate_of_failure,2),"%")
        print("\nThe average number of random restarts required without sideways move", final_restarting_count/(successful_iterations_count+fail_iterations_count))
        print("\nThe average number of steps required without sideways move", successful_steps_count/(successful_iterations_count+fail_iterations_count))
        print("___________________________________________________________________________________________")
        print("\n\t\t\t~~~~:Random-Restart hill-climbing search with sideways move:~~~~ ")
        print("Calculating...")
        successful_steps_count = z
        failure_step_count = z
        successful_iterations_count = z
        fail_iterations_count = z
        final_restarting_count = z
        for uu in range(0, iterations):
            bs = state_board(n)
            valuation, step_number, final_restart_count = random_restart_hill_climbing_algo_with_sideways(bs)
            if valuation == 1:
                fail_iterations_count += 1
                failure_step_count += step_number
            else:
                successful_iterations_count += 1
                successful_steps_count += step_number
            final_restarting_count += final_restart_count
        rate_of_success=(successful_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        rate_of_failure=(fail_iterations_count/(successful_iterations_count+fail_iterations_count))*cent
        print("\nSuccess rate is: ",round(rate_of_success,2),"% and Failure rate is: ",round(rate_of_failure,2),"%")
        print("\nThe average number of random restarts required with sideways move", final_restarting_count / (successful_iterations_count + fail_iterations_count))
        print("\nThe average number of steps required with sideways move", successful_steps_count / (successful_iterations_count + fail_iterations_count))


    except ValueError:
        print("Please enter size of the Board N (integer).")
    
main()
