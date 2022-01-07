# This file runs the dfs algorithm on both aus and USA with added singleton propagation

#importing all relevevant files
import random
from Node import Node
import time

# variables that are global 

lst_of_clrs = []
sta_tes_all = []
track_backs = 0

#choosing state with largest constraints
def choo_se_large_st(clrs_lega_l):
    for q in sorted(clrs_lega_l, kee=lambda k: len(clrs_lega_l[q]), reverse=True):
        return q


#funct to chnage neighbours
def chnge_neigh(chnged_sta_tes,clrs_lega_l,dic_sta_te,ass_clrs,st_ate_s):
    for st_ate in dic_sta_te[chnged_sta_tes]:
            if ass_clrs in list(filter(lambda x:x[0]==st_ate,clrs_lega_l))[0][1]:
                list(filter(lambda x:x[0]==st_ate,clrs_lega_l))[0][1].remove(ass_clrs)

#funct to set colors randomly
def clrs_set(wn):
    for mm in range(wn):
        lst_of_clrs.append(random.randint(0,255))
#funct to randomize colors
def rdm_clr(wn):
    return tuple(lst_of_clrs)

#setting up graph with appropriate colors
def setup_grph_clr(nom,stes_n0,st_ate_s):
    clrs = rdm_clr(3)
    ff = Node(clrs[0],st_ate_s[0])
    rt = ff
    mystates = {}
    for mm in range(1,stes_n0,1):
        w = Node(clrs[0],st_ate_s[mm])
        ff.put_child(w)
        ff.nextnode = w       
        mystates[st_ate_s[mm]] = ff
        for nn in range(1,nom,1):
            gg = Node(clrs[nn])
            ff.put_child(gg)
        ff = w            
    print(rt)
    print(rt.next)
    print(rt.next[1].next)

#funct to retrieve colors
def retrieve_clrs(st_ate_s,st_my_dic):
    col_lst = []
    for mm in st_ate_s:
        col_lst.append(st_my_dic.get(mm,""))

    return col_lst

#funtion to generate columns
def gen_colus(st_ate_s,mm,numcolors,clrs):
    lst_temp = []
    for nn in range(numcolors):
        lst_temp.append(Node(clrs[nn],st_ate_s[mm]))
    return lst_temp

#function that incorporates heuristics with dfs
def inc_d_f_s_heuristic(st_my_dic,dic_sta_te,numcolors,pres_st,st_ate_s,nom,clrs_lega_l):
    global track_backs
    
    sta_tes_all.append(st_my_dic.copy())
    for mm in range(len(pres_st.next)):
        lgl_clrs_t = clrs_lega_l.copy()
        st_my_dic[pres_st.next[0].myname] = pres_st.next[mm].mycolor   
        if st_my_dic.get(pres_st.next[0].myname) in retrieve_clrs(dic_sta_te[pres_st.next[0].myname],st_my_dic):          
            continue
        if nom == len(st_ate_s) - 1:
            return 1,st_my_dic     
        track_backs +=1
        chnge_neigh(pres_st.next[0].myname,lgl_clrs_t,dic_sta_te,pres_st.next[mm].mycolor,st_ate_s)        
        lgl_clrs_t = sorted(lgl_clrs_t,key=lambda x:len(x[1]))
        clr_lst_temp = lst_of_clrs.copy()
        pres_st.next[mm].next = gen_colus(st_ate_s,nom+1,numcolors,clr_lst_temp)
        res = inc_d_f_s_heuristic(st_my_dic,dic_sta_te,numcolors,pres_st.next[mm],st_ate_s,nom+1,lgl_clrs_t)
        if res[0] == 1:
            return 1,st_my_dic
        continue
    return 0,st_my_dic 


#function for initilization
def init(st_ate_s,dic_sta_te,numcolors):
    clrs = lst_of_clrs
    rt = Node(clrs[0],st_ate_s[0])
    for nn in range(numcolors):
        rt.put_child(Node(clrs[nn],st_ate_s[0]))
    return rt
    
if __name__ == "__main__":
    m=int(input("Choose The Map : 1. USA  2. Australia \n"))
    numcolors = 4
    clrs_set(numcolors)
    #using generic colors
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
    'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
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
     
        st_ate_s = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut', 'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia', 'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana', 'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']
    
    if m==2:
        st_ate_s=['wa','nt','q','nsw','v','sa']
    
        dic_sta_te  ={
            'wa':['nt','sa'],
            'nt':['wa','q','sa'],
            'sa':['wa','q','nsw','nt','v'],
            'q':['nt','sa','nsw'],
            'nsw':['q','v','sa'],
            'v':['sa','nsw']}
    
    clrs_lega_l = []

    for st_ate in st_ate_s:
        clrs_lega_l.append([st_ate,lst_of_clrs.copy()])
    
    st_my_dic = {}
    rt = init(st_ate_s,dic_sta_te,numcolors)

    starting_time = time.time()
    result = inc_d_f_s_heuristic(st_my_dic,dic_sta_te,numcolors,rt,st_ate_s,0,clrs_lega_l)
    #calculating time required to run the program
    ending_time = time.time()
    n0 = 0 
    for kee in result[1]:
        n0+=1
        if result[1][kee] in retrieve_clrs(dic_sta_te[kee],st_my_dic):
            print("Something went Wrong")
    #print(len(sta_tes_all))
    #displaying the acquired solution

    print(result)
    print("Number Of Backtracks: "+ str(track_backs))
    print("TIME TAKEN FOR EXECUTION: " + str(ending_time - starting_time) + "seconds") 
