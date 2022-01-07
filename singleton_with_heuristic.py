import os
import random
from Node import Node
import pdb
import time

lst_of_clrs = []
No_of_Back_tracks = 0
Every_St = []

# Class state conatins State name, State colors, status etc.
class State:
    def __init__(self,name,dom,Status="Not_Visited"):
        self.name=name
        self.Neighbor=None
        self.Named_Clrs=None
        self.Status=Status
        self.dom=dom
        self.Heuristic_singleton=False

    def Neighbor_Set(self,Neighbor):
        self.Neighbor=Neighbor
    def Neighbor_Get(self):
        return self.Neighbor
    def clrs_Set(self,Named_Clrs):
        self.Named_Clrs=Named_Clrs
    def Parents_Set(self,parent):
        self.parent=parent
    def dom_Set(self,dom):
        self.dom=dom
    def dom_Get(self):
        return self.dom
    def Is_Heuristic_Singleton(self):
        if self.Heuristic_singleton:
            return self.Heuristic_singleton
        return False

# Function used to iniz colors
def clr_iniz(n):
    for l in range(n):
        lst_of_clrs.append(random.randint(0,255))

# Function used to generate random clrs
def clrs_Random(n):
    return tuple(lst_of_clrs)

# Function used to build the graph for clring
def clrs_graph_bld(no,no_st,st):
    clrs = clrs_Random(3)
    c = Node(clrs[0],st[0])
    root = c
    myst = {}
    for l in range(1,no_st,1):
        z = Node(clrs[0],st[l])
        c.put_child(z)
        c.Next_Node = z
        myst[st[l]] = c

        for m in range(1,no,1):
            d = Node(clrs[m])
            c.put_child(d)
        c = z
            
    print(root)
    print(root.next)
    print(root.next[1].next)

def clr_Get(st,My_State_Dict):
    lstcol = []
    for l in st:
        lstcol.append(My_State_Dict.get(l,""))

    return lstcol

#Function for generating clrs
def clr_gen(st,l,clr_no,clrs):
    ListT = []
    for m in range(clr_no):
        ListT.append(Node(clrs[m],st[l]))

    return ListT

# Function using Singleton Heuristic method to compute backtracking
def Heuristic_singleton(My_State_Dict,dict_st,clr_no,st_cur,st,no):

    global No_of_Back_tracks
    Every_St.append(My_State_Dict.copy())
    for l in range(len(st_cur.next)):
        My_State_Dict[st_cur.next[0].myname] = st_cur.next[l].mycolor   
        if My_State_Dict.get(st_cur.next[0].myname) in clr_Get(dict_st[st_cur.next[0].myname],My_State_Dict):
            continue

        if no == len(st) - 1:
            return 1,My_State_Dict

        temp_lst_of_clrs = lst_of_clrs.copy()
        clr_Remove = clr_Get(st[no+1],My_State_Dict)
        temp_lst_of_clrs = [y for y in temp_lst_of_clrs if y not in clr_Remove]
        st_cur.next[l].next = clr_gen(st,no+1,clr_no,temp_lst_of_clrs)

        ans = Heuristic_singleton(My_State_Dict,dict_st,clr_no,st_cur.next[l],st,no+1)
        if ans[0] == 1:
            return 1,My_State_Dict

        continue
        
    No_of_Back_tracks +=1

    return 0,My_State_Dict 


def init(st,dict_st,clr_no):
    clrs = lst_of_clrs
    root = Node(clrs[0],st[0])
    for m in range(clr_no):
        root.put_child(Node(clrs[m],st[0]))

    return root
    
# Calling Main Function.
if __name__ == "__main__":
    i=int(input("Choose The Map : 1. USA  2. Australia \n"))
    clr_no = 4
    clr_iniz(clr_no)

    lst_of_clrs = ["green","brown","yellow","blue"]
    if i==1:

            dict_st = {
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
        'Mississippi':['Alabama', 'Arkanssas', 'Louisiana', 'Tennessee'],
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
        'Wyoming':['clrado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
        "Hawai":[],
        "Alaska":[]
        }
        
            st = ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'clrado', 'Mississippi', 'Arkansas']
        
            
            st = ['Kansas', 'New Hampshire', 'Idaho', 'Louisiana', 'New Jersey', 'Arkansas', 'Kentucky', 'Maine', 'Minnesota', 'Missouri',
                    'West Virginia', 'North Carolina', 'Massachusetts', 'Michigan', 'Indiana', 'Illinois', 'Virginia', 'Oklahoma', 'Montana',
                    'North Dakota', 'Texas', 'clrado', 'South Carolina', 'Maryland', 'California', 'New York', 'Florida', 'Vermont', 'Utah',
                    'Georgia', 'Oregon', 'Wisconsin', 'Rhode Island', 'Nebraska', 'New Mexico', 'Mississippi', 'Alabama', 'Nevada', 'Tennessee',
                    'Iowa','South Dakota', 'Ohio', 'Pennsylvania', 'Washington', 'Wyoming', 'Arizona', 'Delaware', 'Connecticut']
    else:        
            st=['wa','nt','q','nsw','v','sa']
            dict_st  ={
                'wa':['nt','sa'],
                'nt':['wa','q','sa'],
                'sa':['wa','q','nsw','nt','v'],
                'q':['nt','sa','nsw'],
                'nsw':['q','v','sa'],
                'v':['sa','nsw']}
    
    My_State_Dict = {}
    print(st)

    root = init(st,dict_st,clr_no)

    Time_Start = time.time()
    Ans = Heuristic_singleton(My_State_Dict,dict_st,clr_no,root,st,0)
    end_time = time.time()
    count = 0 
    for key in Ans[1]:
        count+=1
        if Ans[1][key] in clr_Get(dict_st[key],My_State_Dict):
            print("No Answer")


    print("Answer that's Verified")
    print(Ans)
    print("No_of_Back_tracks: "+ str(No_of_Back_tracks))
    print("Total Time taken for Execution: " + str(end_time - Time_Start) + "seconds") 

    print(len(Every_St))
    time.sleep(10)
    