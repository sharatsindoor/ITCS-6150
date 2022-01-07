import os
import random
from Node import Node
import pdb
import time

clrs_List = []
Every_St = []
No_of_Backtracks = 0

# Function used to select biggest state for coloring.
def Choose_St_Big(clr_Legal):
    for q in sorted(clr_Legal, key=lambda q: len(clr_Legal[q]), reverse=True):
        return q

# Function to update the clrs for neighboring states. 
def Neigh_Upt(St_chng,clr_Legal,Dict_St,Assigned_clr,Sts):
    for St in Dict_St[St_chng]:
            if Assigned_clr in list(filter(lambda z:z[0]==St,clr_Legal))[0][1]:
                list(filter(lambda z:z[0]==St,clr_Legal))[0][1].remove(Assigned_clr)

# Function to Intialize colors.
def clr_Init(n):
    for m in range(n):
        clrs_List.append(random.randint(0,255))

# Function to gen random colors.
def clr_Random(n):
    return tuple(clrs_List)

# Function to build graph for coloring
def clr_Graph_Bld(no,no_Sts,Sts):
    clrs = clr_Random(3)
    p = Node(clrs[0],Sts[0])
    root = p
    mySts = {}
    for m in range(1,no_Sts,1):
        u = Node(clrs[0],Sts[m])
        p.put_child(u)
        p.nextnode = u
        mySts[Sts[m]] = p

        for n in range(1,no,1):
            k = Node(clrs[n])
            p.put_child(k)
        p = u
            
    print(root)
    print(root.next)
    print(root.next[1].next)

def clr_Get(Sts,Dictionary_St):
    clr_List = []
    for m in Sts:
        clr_List.append(Dictionary_St.get(m,""))

    return clr_List

# Function to gen color.
def clr_gen(Sts,m,no_clr,clrs):
    ListT = []
    for n in range(no_clr):
        ListT.append(Node(clrs[n],Sts[m]))

    return ListT

# Function using Heuristic to compute backtracks 
def included_Heuristic(Dictionary_St,Dict_St,no_clr,St_Current,Sts,no,clr_Legal):
    global No_of_Backtracks

    Every_St.append(Dictionary_St.copy())
    for m in range(len(St_Current.next)):
        Legal_clr_Temp= clr_Legal.copy()
        Dictionary_St[St_Current.next[0].myname] = St_Current.next[m].mycolor   

        if Dictionary_St.get(St_Current.next[0].myname) in clr_Get(Dict_St[St_Current.next[0].myname],Dictionary_St):
            continue

        if no == len(Sts) - 1:
            return 1,Dictionary_St

        
        No_of_Backtracks +=1
        Neigh_Upt(St_Current.next[0].myname,Legal_clr_Temp,Dict_St,St_Current.next[m].mycolor,Sts)

        Legal_clr_Temp= sorted(Legal_clr_Temp,key=lambda z:len(z[1]))
        temp_clrs_List = clrs_List.copy()
        clr_Remove = clr_Get(Legal_clr_Temp[no+1][0],Dictionary_St)
        temp_clrs_List = [z for z in temp_clrs_List if z not in clr_Remove]
        St_Current.next[m].next = clr_gen(Sts,no+1,no_clr,temp_clrs_List)
        Answer = included_Heuristic(Dictionary_St,Dict_St,no_clr,St_Current.next[m],Sts,no+1,Legal_clr_Temp)
        if Answer[0] == 1:
            return 1,Dictionary_St

        continue

    return 0,Dictionary_St 


def init(Sts,Dict_St,no_clr):
    clrs = clrs_List
    root = Node(clrs[0],Sts[0])
    for n in range(no_clr):
        root.put_child(Node(clrs[n],Sts[0]))

    return root
    
# Calling Main Function
if __name__ == "__main__":
    global m
    m=int(input("Choose the Map 1. USA 2. Australia\n"))
    
    if m==1:
        no_clr = 4
        clr_Init(no_clr)
        clrs_List = ["red","blue","green","black"]
        Dict_St = {
    'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
    'Arizona':['California', 'clrado', 'Nevada', 'New Mexico', 'Utah'],
    'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
    'California':['Arizona', 'Nevada', 'Oregon'],
    'clrado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
    'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
    'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
    'Florida':['Alabama', 'Georgia'],
    'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
    'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
    'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
    'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
    'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
    'Kansas' :['clrado', 'Missouri', 'Nebraska', 'Oklahoma'],
    'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
    'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
    'Maine':["New Hampshire"],
    "Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
    'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
    'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
    'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
    'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
    'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
    'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'Nebraska' :['clrado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
    'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
    'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
    'New Jersey':["Delaware", "New York", "Pennsylvania"],
    'New Mexico':['Arizona', 'clrado', 'Oklahoma', 'Texas', 'Utah'],
    'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
    'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
    'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
    'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
    'Oklahoma' :['Arkansas', 'clrado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
    'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
    'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
    'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
    'South Carolina':['Georgia', 'North Carolina'],
    'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
    'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
    'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
    'Utah':['Arizona', 'clrado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
    'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
    'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
    'Washington':['Idaho', 'Oregon'],
    'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
    'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
    'Wyoming':['clrado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
    }
    Sts = ['Illinois', 'Oklahoma', 'California', 'Utah', 'Wyoming', 'Missouri', 'Michigan', 'Texas', 'Iowa', 'Delaware', 'Tennessee', 'Maryland', 'Kentucky', 'Montana', 'Minnesota', 'Connecticut', 'Louisiana', 'West Virginia', 'Pennsylvania', 'Nebraska', 'Kansas', 'Indiana', 'Rhode Island', 'Arizona', 'Florida', 'Massachusetts', 'South Dakota', 'Nevada', 'South Carolina', 'Ohio', 'New Hampshire', 'Idaho', 'Washington', 'clrado', 'Oregon', 'New Jersey', 'Mississippi', 'Arkansas', 'Vermont', 'Wisconsin', 'Alabama', 'Georgia', 'Maine', 'New Mexico', 'North Carolina', 'New York', 'Virginia', 'North Dakota']
    
    
    if m==2:
        no_clr = 3
        clr_Init(no_clr)
    
        clrs_List = ["red","blue","green","black"]
        Sts=['wa','nt','q','nsw','v','sa']
        Dict_St  ={
            'wa':['nt','sa'],
            'nt':['wa','q','sa'],
            'sa':['wa','q','nsw','nt','v'],
            'q':['nt','sa','nsw'],
            'nsw':['q','v','sa'],
            'v':['sa','nsw']}

    clr_Legal = []

    for St in Sts:
        clr_Legal.append([St,clrs_List.copy()])

    Dictionary_St = {}
    root = init(Sts,Dict_St,no_clr)

    Time_Start = time.time()
    Answer = included_Heuristic(Dictionary_St,Dict_St,no_clr,root,Sts,0,clr_Legal)

    Time_End = time.time()
    count = 0 
    for key in Answer[1]:
        count+=1
        if Answer[1][key] in clr_Get(Dict_St[key],Dictionary_St):
            print("No Answer")


    time.sleep(10)
    print("Answer Verified")
    print(Answer)
    print("No_of_Backtracks: "+ str(No_of_Backtracks))
    print("Time Taken for Exec: " + str(Time_End - Time_Start) + "seconds") 