
# This file just creates a Node 
class Node:
    def __init__(self,mycolor,myname=None):
        self.next = []
        self.nextnode = None
        self.mycolor = mycolor
        self.myname = myname
    
    #funtion to create a child node
    def put_child(self,node):
        self.next.append(node)