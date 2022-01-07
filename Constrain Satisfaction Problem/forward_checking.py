import time
import random
from Node import Node

clr_list = []
No_of_Backtracks = 0
every_st = []

# Function to iniz the color. 
def clr_iniz(n):
    for m in range(n):
        clr_list.append(random.randint(0,255))

# Function for Random color generation
def clr_Random(n):
    return tuple(clr_list)

# Function to build the colored graph
def clr_Graph_bld(No,No_st,st):
    clr = clr_Random(3)
    c = Node(clr[0],st[0])
    Root_Node = c # Creating Root node
    st_cur = {} 
    for m in range(1,No_st,1):
        z = Node(clr[0],st[m])
        c.put_child(z)
        c.nextnode = z
        st_cur[st[i]] = c

        for n in range(1,No,1):
            d = Node(clr[n])
            c.put_child(d)
        c = z
            
    print(Root_Node)
    print(Root_Node.next)
    print(Root_Node.next[1].next)

def clr_Get(st,st_cur_Dict):
    col_lst = []
    for m in st:
        col_lst.append(st_cur_Dict.get(m,""))

    return col_lst

# Function to gen colors
def Col_gen(st,m,Col_No,clr):
    lstT = []
    for n in range(Col_No):
        lstT.append(Node(clr[n],st[m]))

    return lstT

# Function to apply Forward tracking method.
def Forw_chq(st_cur_Dict,st_Dict,Col_No,st_Cur,st,No):
    global No_of_Backtracks
    every_st.append(st_cur_Dict.copy())
    for m in range(len(st_Cur.next)):
        time.sleep(0.000002)
        st_cur_Dict[st_Cur.next[0].myname] = st_Cur.next[m].mycolor   
        if st_cur_Dict.get(st_Cur.next[0].myname) in clr_Get(st_Dict[st_Cur.next[0].myname],st_cur_Dict):
            continue

        if No == len(st) - 1:
            return 1,st_cur_Dict

        Temporary_CList = clr_list.copy()
        clr_Remove = clr_Get(st[No+1],st_cur_Dict)
        Temporary_CList = [x for x in Temporary_CList if x not in clr_Remove]
        st_Cur.next[m].next = Col_gen(st,No+1,Col_No,Temporary_CList)
        ans = Forw_chq(st_cur_Dict,st_Dict,Col_No,st_Cur.next[m],st,No+1)
        if ans[0] == 1:
            return 1,st_cur_Dict

        continue
        
    No_of_Backtracks +=1

    return 0,st_cur_Dict 


def init(st,st_Dict,Col_No):
    clr = clr_list
    Root_Node = Node(clr[0],st[0])
    for n in range(Col_No):
        Root_Node.put_child(Node(clr[n],st[0]))

    return Root_Node
    
# Calling main 
if __name__ == "__main__":
    i=int(input("Choose The Map : 1. USA  2. Australia \n"))
    Col_No = 4
    clr_iniz(Col_No)

    clr_list = ["blue","yellow","brown","red"]
    if i==1:
            st_Dict = {
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
        st_Dict  ={
                'wa':['nt','sa'],
                'nt':['wa','q','sa'],
                'sa':['wa','q','nsw','nt','v'],
                'q':['nt','sa','nsw'],
                'nsw':['q','v','sa'],
                'v':['sa','nsw']}
    

    st_cur_Dict = {}
    print(st)

    Root_Node = init(st,st_Dict,Col_No)

    strt_Time = time.time()
    Ans = Forw_chq(st_cur_Dict,st_Dict,Col_No,Root_Node,st,0)
    ending_time = time.time()
    count = 0 
    for key in Ans[1]:
        count+=1
        if Ans[1][key] in clr_Get(st_Dict[key],st_cur_Dict):
            print("No Answer")


    print("Answer Verified")
    print(Ans)
    print("No_of_Backtracks: "+ str(No_of_Backtracks))
    print("Total Time taken for Execution: " + str(ending_time - strt_Time) + "seconds") 

    print(len(every_st))
    time.sleep(10)
    