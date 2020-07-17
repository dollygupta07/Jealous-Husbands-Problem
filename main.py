from copy import deepcopy
import time
import sys
import prettytable
from time import perf_counter 
from prettytable import PrettyTable
class State:
    shore = None                        
    boat = 0                          
    depth = 0                     
    path = None                        
    
    def __init__(self, s=[], b=0):
        self.shore = s
        self.boat = b
        self.depth = 0
        self.path = []
        
    def f(self):                        # evaluation function
        return self.depth + h(self)     # f(n) = g(n) + h(n)
          

def jealousy(current):
    for i in range(0,noCouples):
        if current.shore[i] != current.shore[noCouples+i]:       
            for j in range(noCouples, noCouples*2): 
                    if(current.shore[j] == current.shore[i]):       
                        return 1
    return 0

def alterbit(bit):                                                  
    return abs(bit - 1)

def isGood(state):                                                  
    good_people = deepcopy(state.shore)
    for i in range(0, len(state.shore)):
        if state.shore[i] == state.boat:
            good_people[i] = 1
    return good_people

def h(state):                                                       # the heuristic function equals the number of people who are not on the goal shore
    result = len(state.shore)
    for i in state.shore:
        result = result - i
    return result

def visited(state, searched):                                       # determines whether a State has already been visited
    for k in range(0, len(searched)):
        if state.shore == searched[k].shore and state.boat == searched[k].boat:
            return True
    return False

def move(cap, state, movement, result, start):                      # computes all possible moves from a current State with a certain boat capacity
    for i in range(start, len(state.shore)):
        if isGood(state)[i] == 1:                                   
            movement.append(i)                                      
            if cap > 1:                                             
                move(cap-1, state, movement, result,i)              
            if cap == 1:                                           
                result.append(deepcopy(movement))                 
            movement.pop()                                          
    return result                                                 

def expand(state): 
    following = deepcopy(state)
    result = [] 
    possible_moves = move(boat_capacity, state, [], result,0)       
    for i in possible_moves:                                       
        following = deepcopy(state)
        for j in i:
            following.shore[j]  = alterbit(state.shore[j])          
        following.boat = alterbit(state.boat)                     
        if visited(following, searched):                           
            True
        elif jealousy(following):                                  
            searched.append(following)
        elif True:
            following.depth = following.depth + 1                 
            following.path.append(state)                          
            frontier.append(following)                             
            


def BFS():
    d = -1                                                      
    global noStates
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        current = frontier.pop(0)                              
        
        if h(current) == 0:                                  
            return current                                    
        if current.depth != d:                                
            d = current.depth
            print("current depth: ", d)
        
        expand(current)                                        
        searched.append(current)                             

def DFS():
    global noStates
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        current = frontier.pop()                             
        
        if h(current) == 0:                                   
            return current                                    
        
        expand(current)                                         
        searched.append(current)                                

def GBEST():                   
    global noStates
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        frontier.sort(key=lambda state: h(state))              
        
        current = frontier.pop(0)                               
        
        if h(current) == 0:                                   
            return current                                     
        
        expand(current)                                         
        searched.append(current)                               
        
def ASTAR():
    global noStates
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        frontier.sort(key=lambda state: state.f())         
        
        current = frontier.pop(0)                              

        if h(current) == 0:                                   
            return current                                
        
        expand(current)                                       
        searched.append(current)                               
                
if __name__ =='__main__':
    print("\nsearch strategies used:")
    print("\t(1) Breadth-First-Search")
    print("\t(2) Depth-First-Search")
    print("\t(3) Greedy Best-First-Search")
    print("\t(4) A*-Search-Algorithm")
    noCouples = int(input("Enter the number of couples: "))
    boat_capacity = int(input("How many persons can the boat hold: "))
    

    #bfs starts
    t_start=perf_counter()
    
    couple = [0,0]
    initial = State([], 0)
    goal = State([], 0)
    path = []
    frontier = []                                       
    searched = []                                       
    noStates = 0
    
    for i in range(0,noCouples):                       
        initial.shore.extend(couple)                   
    
    frontier.append(initial)                           
    
  
    print("\t(1) Breadth-First-Search:")

    goal = BFS()                            
        
    print("\nSuccess using bfs: ", goal.shore, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.shore)
    print("Path: ", path)
    t_stop= perf_counter()
    bfs_t=t_stop-t_start



   

    #gest starts
    t_start=perf_counter()
    
    couple = [0,0]
    initial = State([], 0)
    goal = State([], 0)
    path = []
    frontier = []                                      
    searched = []                                      
    noStates = 0
    
    for i in range(0,noCouples):                      
        initial.shore.extend(couple)                  
    
    frontier.append(initial)                           
    
  
    print("\t(1) Greedy-Best-First-Search:")

    goal = GBEST()                            
        
    print("\nSuccess using gbest: ", goal.shore, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.shore)
    print("Path: ", path)
    t_stop= perf_counter()
    gbest_t=t_stop-t_start 

    #astar starts

    t_start=perf_counter()
    
    couple = [0,0]
    initial = State([], 0)
    goal = State([], 0)
    path = []
    frontier = []                                       
    searched = []                                      
    noStates = 0
    
    for i in range(0,noCouples):                        
        initial.shore.extend(couple)                  
    frontier.append(initial)                           
    
  
    print("\t(1) A -star-Search:")

    goal = ASTAR()                            
        
    print("\nSuccess using astar: ", goal.shore, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.shore)
    print("Path: ", path)
    t_stop= perf_counter()
    astar_t=t_stop-t_start
    
  #  print("\nbfs_time: %.2f"%bfs_t)
  #  print("\ndfs_time: %.2f"%dfs_t)
  #  print("\ngbest_time: %.2f"%gbest_t)
  #  print("\nastar_time:%.2f"%astar_t)
    
t = PrettyTable(['Number of couples','Boat capacity','Bfs_time', 'Dfs_time','Gbest_time','Astar_time'])
t.add_row([noCouples,boat_capacity,round(bfs_t,6),0,round(gbest_t,6),round(astar_t,6)])
print(t)
