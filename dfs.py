
# This file runs the dfs algorithm on both aus and USA without any heuristics
#importing all relevevant files
import time
import random
from Node import Node

# variables that are global 
lst_of_clrs = []
sta_tes_all = []
track_backs = 0


#this function sets the random initial colors for the states
def setting_clrs(wn):
    for qq in range(wn):
        lst_of_clrs.append(random.randint(0,255))


#this function just returns the random config of colors
def rdm_clrs(wn):
    return tuple(lst_of_clrs)

#this func builds a graph of colors
def building_clr_grphs(n0,ste_n0,sta_tess):
    clrs = rdm_clrs(3)
    x = Node(clrs[0],sta_tess[0])
    root_r = x
    my_state_s = {}
    for f in range(1,ste_n0,1):
        w = Node(clrs[0],sta_tess[f])
        x.put_child(w)
        x.next_nde = w
        my_state_s[sta_tess[f]] = x
        for y in range(1,n0,1):
            z = Node(clrs[y])
            x.put_child(z)
        x = w         
    print(root_r)
    print(root_r.next)
    print(root_r.next[1].next)

#function for color retrieving
def geting_clrs(sta_tess,my_ste_dic):
    clr_lst = []
    for qq in sta_tess:
        clr_lst.append(my_ste_dic.get(qq,""))
    return clr_lst


#funct for color generation
def clr_generate(sta_tess,qq,n0_of_clrs,clrs):
    lst_t = []  
    for rr in range(n0_of_clrs):
        lst_t.append(Node(clrs[rr],sta_tess[qq]))
    return lst_t


#main dfs part of the program
def d_f_s(my_ste_dic,dic_sta_te,n0_of_clrs,st_ate_cur,sta_tess,n0):   
    global track_backs
    for qq in range(len(st_ate_cur.next)):
        my_ste_dic[st_ate_cur.next[0].myname] = st_ate_cur.next[qq].mycolor   
        if my_ste_dic.get(st_ate_cur.next[0].myname) in geting_clrs(dic_sta_te[st_ate_cur.next[0].myname],my_ste_dic):   
            continue  
        sta_tes_all.append(my_ste_dic.copy())    
        if n0 == len(sta_tess) - 1:
            return 1,my_ste_dic
        temp_colorlist = lst_of_clrs.copy()      
        st_ate_cur.next[qq].next = clr_generate(sta_tess,n0+1,n0_of_clrs,temp_colorlist)
        sol1 = d_f_s(my_ste_dic,dic_sta_te,n0_of_clrs,st_ate_cur.next[qq],sta_tess,n0+1)
        if sol1[0] == 1:
            return 1,my_ste_dic
        continue
    track_backs+=1
    return 0,my_ste_dic 


#initializing function
def init(sta_tess,dic_sta_te,n0_of_clrs):
    clrs = lst_of_clrs
    root_r = Node(clrs[0],sta_tess[0])
    for rr in range(n0_of_clrs):
        root_r.put_child(Node(clrs[rr],sta_tess[0]))
    return root_r
  

#main funtion  
if __name__ == "__main__":
    m=int(input("Choose The Map : 1. USA  2. Australia \n"))
    n0_of_clrs = 4
    setting_clrs(n0_of_clrs)
    
    lst_of_clrs = ["red","blue","green","black"]
    #different states are assigned based on users choice 
    if m==1:
        dic_sta_te = {
        'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
        'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
        'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
        'California':['Arizona', 'Nevada', 'Oregon'],
        'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
        'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
        'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
        'Florida':['Alabama', 'Georgia'],
        'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
        'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
        'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
        'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
        'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
        'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
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
        'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
        'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
        'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
        'New Jersey':["Delaware", "New York", "Pennsylvania"],
        'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
        'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
        'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
        'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
        'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
        'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
        'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
        'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
        'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
        'South Carolina':['Georgia', 'North Carolina'],
        'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
        'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
        'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
        'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
        'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
        'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
        'Washington':['Idaho', 'Oregon'],
        'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
        'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
        'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
        }
        


        sta_tess = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut',
                    'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia',
                    'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana',
                    'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 
                    'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']


    if m==2:
        sta_tess=['wa','nt','q','nsw','v','sa']
    
        dic_sta_te  ={
            'wa':['nt','sa'],
            'nt':['wa','q','sa'],
            'sa':['wa','q','nsw','nt','v'],
            'q':['nt','sa','nsw'],
            'nsw':['q','v','sa'],
            'v':['sa','nsw']}
    
    
    my_ste_dic = {}
    
    root_r = init(sta_tess,dic_sta_te,n0_of_clrs)
    
    starting_time = time.time()
    solution = d_f_s(my_ste_dic,dic_sta_te,n0_of_clrs,root_r,sta_tess,0)
    
    
    #displaying the acquired solution
    for kk in solution[1]:
        if solution[1][kk] in geting_clrs(dic_sta_te[kk],my_ste_dic):
            print("Problem Occured")
    #calculating time         
    ending_time = time.time()

    print(solution)

    print("\n\nNUMBER OF BACKTRACKS: "+ str(track_backs))
    print("\nTIME TAKEN FOR EXECUTION: " + str(ending_time - starting_time) + "seconds") 

