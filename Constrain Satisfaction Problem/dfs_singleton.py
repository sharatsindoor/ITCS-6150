# This file runs the dfs algorithm on both aus and USA with added singleton propagation

#importing all relevevant files
from copy import deepcopy as dc
import time


# variables that are global 
lst_full = []
track_backs = 0


# class definiation and initialization
class State:
    def __init__(self,nme_st,dm_in,st_us="not visited"):
        self.nme_st=nme_st
        self.neigh_brs=None
        self.nme_clr=None
        self.st_us=st_us
        self.dm_in=dm_in
        self.sin_leton=False
    # internal funtions required to run 
    def se_tNeigh(self,neigh_brs):
        self.neigh_brs=neigh_brs
    def get_neigh(self):
        return self.neigh_brs
    def set_clrs(self,nme_clr):
        self.nme_clr=nme_clr
    def set_par_ent(self,par_ent):
        self.par_ent=par_ent
    def put_do_main(self,dm_in):
        self.dm_in=dm_in
    def ret_do_main(self):
        return self.dm_in
    def check_single(self):
        if self.sin_leton:
            return self.sin_leton
        return False
    

#this function determines which states are still available/not visited       
def ava_sta_tes(st_a_te_obj_ects):
    states_not_visted=[]
    for st_a_te in st_a_te_obj_ects:
        if st_a_te.st_us=="not visited":
            states_not_visted.append(st_a_te)        
    return states_not_visted

#this function checks which colors are still available  for use    

def ava_clrs(st_a_te,dm_in):  
    dmn_avail_able=dm_in.copy()
    for nai_bhor in st_a_te.neigh_brs:
        clr = nai_bhor.nme_clr       
        if clr!=None and (clr in dmn_avail_able) :
            dmn_avail_able.remove(clr)
    return dmn_avail_able


#this function is used to change domains
def chng_dmn(st_a_te,clr):
    for nai_bhor in st_a_te.nai_bhor:
        if (nai_bhor.st_us=="not visited") and (clr in nai_bhor.dm_in):
            (nai_bhor.dm_in).remove(clr)
 
#this function checks which states need propagation            
def sngle_dmn_sts(st_a_te_obj_ects):
    k=None
    for st_a_te in st_a_te_obj_ects:
        if st_a_te.sin_leton==False and len(st_a_te.ret_do_main())==1:         
            st_a_te.sin_leton=True
            clr = st_a_te.dm_in[0]
            return st_a_te,clr
    return k,k

# main part of the code i.e singleton propagation
def prop_single_ton(st_a_te_obj_ects):
    sngl_ton_sts={}
    while True:      
        st_a_te,clr = sngle_dmn_sts(st_a_te_obj_ects)      
        if st_a_te==None:
            return sngl_ton_sts,"success"
        else:
            sngl_ton_sts[st_a_te]=clr
            for nai_bhor in st_a_te.neigh_brs:
                if nai_bhor.st_us=="not visited" and clr in nai_bhor.dm_in:
                    if len(nai_bhor.dm_in)==1:
                        return sngl_ton_sts,"unsucessful"
                    (nai_bhor.dm_in).remove(clr)
                        
                    
#this function sets the random initial colors for the states based on domains
        
def setting_clrs(dm_in,state_domain):    
    dom=dc(dm_in)
    dom2=dc(dom)
    state_dom=dc(state_domain) 
    for clr in dom:
        count=0      
        for st_a_te_clr in state_dom:         
            if clr!=st_a_te_clr:              
                count+=1     
        if count==len(state_dom):         
            dom2.remove(clr)          
    return dom2
                
#this function updates the initial colors for the states based on domains
    
def upgrade_clrs(st_a_te,clr):
    updated_states=[]
    for nai_bhor in st_a_te.neigh_brs:    
        if nai_bhor.st_us=="not visited" and clr in nai_bhor.dm_in:         
            (nai_bhor.dm_in).remove(clr)          
            updated_states.append(nai_bhor)  
    return updated_states


#this function resets the initial colors for the states based on neighbouring states

def reset(st_a_te,dm_in,clr,updated_states):
    pos = dm_in.index(clr)  
    for nai_bhor in st_a_te.neigh_brs:
        if nai_bhor.st_us=="not visited" and (nai_bhor in updated_states):
            (nai_bhor.dm_in).insert(pos,clr)
            dom = setting_clrs(dm_in,nai_bhor.dm_in)
            nai_bhor.dm_in=dc(dom)
            
#this function resets the singleton propogation status for the states based on neighbouring states
            
def re_set_single(sngl_ton_sts,dm_in,colour): 
    for st_a_te,clr in sngl_ton_sts.items():      
        pos = dm_in.index(clr)  
        for nai_bhor in st_a_te.neigh_brs:         
            if nai_bhor.st_us=="not visited" and (nai_bhor.check_single()):        
                (nai_bhor.dm_in).insert(pos,clr)
                dom = setting_clrs(dm_in,nai_bhor.dm_in)
                nai_bhor.dm_in=dom
        st_a_te.sin_leton=False
       
            
# This function acts as the anchor that holds the whole program together       
def c_s_p(st_a_te_obj_ects,dm_in,states_and_colors):
        global track_backs 
        if len(states_and_colors)==len(st_a_te_obj_ects):
            return states_and_colors    
        un_assigned_states=ava_sta_tes(st_a_te_obj_ects)
        st_a_te=un_assigned_states[0]
        dmn_avail_able=dc(st_a_te.dm_in)
        iter1 = 0
        for clr in dmn_avail_able:
            iter1+=1 
            st_a_te.st_us="visited"
            st_a_te.nme_clr=clr
            states_and_colors[st_a_te.nme_st]=clr
            updated_states=upgrade_clrs(st_a_te,clr)
            sngl_ton_sts,st_us=prop_single_ton(st_a_te_obj_ects)          
            if st_us!="unsucessful":
                rslt=c_s_p(st_a_te_obj_ects,dm_in,states_and_colors)
            else:
                rslt=st_us
            if rslt!="unsucessful":
                return rslt
            del states_and_colors[st_a_te.nme_st]
            st_a_te.nme_clr=None
            st_a_te.st_us="not visited"
        track_backs+=1
        return "unsucessful"
#this func sets the objects according to domains        
def set_obj(stat_es,dm_in):
    state_objs = []
    dom=dc(dm_in)
    for st_a_te in stat_es:
        state_obj=State(st_a_te,dom)
        state_objs.append(state_obj)
        dom=dc(dom)
    return state_objs
        
#main function        
def main():
    
    global m,k
    m=int(input("Choose The Map : 1. USA  2. Australia \n"))
    #different states are assigned based on users choice 

    if m==2:
        stat_es=['wa','nt','q','nsw','v','sa']
        graph_rest_riction={
            'wa':['nt','sa'],
            'nt':['wa','q','sa'],
            'sa':['wa','q','nsw','nt','v'],
            'q':['nt','sa','nsw'],
            'nsw':['q','v','sa'],
            'v':['sa','nsw']
            }
    if m==1:
        stat_es= ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland',
                 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 
                 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 
                 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa',
                 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington',
                 'Delaware', 'Colorado', 'Mississippi', 'Arkansas']
        k={'Ohio': 'blue', 'Hawaii': 'blue', 'Vermont': 'blue', 'Maine': 'blue', 'Tennessee': 'blue', 
        'Oklahoma': 'blue', 'Colorado': 'green', 'Alabama': 'green', 'Oregon': 'blue',
         'Minnesota': 'blue', 'New Mexico': 'red', 'Mississippi': 'red', 'Kansas': 'red',
         'New Hampshire': 'green', 'Louisiana': 'blue', 'Rhode Island': 'blue', 'Montana': 'blue',
         'Wisconsin': 'green', 'Michigan': 'red', 'Arkansas': 'green', 'Maryland': 'blue',
         'Missouri': 'orange', 'Massachusetts': 'red', 'North Dakota': 'green', 'Nevada': 'green',
         'South Dakota': 'orange', 'Illinois': 'blue', 'Washington': 'green', 'Virginia': 'green',
         'Indiana': 'green', 'Alaska': 'blue', 'Connecticut': 'green', 'North Carolina': 'red',
         'New York': 'orange', 'New Jersey': 'blue', 'Iowa': 'red', 'Kentucky': 'red',
         'South Carolina': 'blue', 'West Virginia': 'orange', 'Idaho': 'orange',
         'Florida': 'blue', 'Delaware': 'green', 'Nebraska': 'blue', 'Arizona': 'orange', 
        'Wyoming': 'red', 'California': 'red', 'Utah': 'blue', 'Texas': 'orange', 'Pennsylvania': 'red',
         'Georgia': 'orange'}
        graph_rest_riction ={
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
                'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
                'Hawaii':[],
                'Alaska':[]
                }
        
    
    dm_in=["blue","green","red","orange"]
    st_a_te_obj_ects = set_obj(stat_es,dm_in)
    states_and_colors={}
    for st_a_te in st_a_te_obj_ects:
        key = st_a_te.nme_st
        values=graph_rest_riction[key]
        neigh_brs=[]
        for value in values:
            obj=[obj_form for obj_form in st_a_te_obj_ects if obj_form.nme_st==value ]
            neigh_brs.append(obj[0])           
        st_a_te.se_tNeigh(neigh_brs)   
    global st    
    st=c_s_p(st_a_te_obj_ects,dm_in,states_and_colors)

starting_time = time.time()
main()
ending_time = time.time()

print("Time taken for execution = " + str(ending_time- starting_time) + " seconds")
print("Number of Backtracks = " + str(track_backs))
        


#displaying the acquired solution

if m==1:
    print(k)
if m==2:
    print(st)