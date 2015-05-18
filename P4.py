'''
CSCI 466 - P4
Lina Baquero
'''

from hashlib import md5
import networkx as nx

DG = nx.DiGraph()
cycles = []
tails = []

def getHash(x, iterations): #i is the complexity
    #Get md5 hash
    x = x.encode('utf-8')
    md5_ = md5(x).hexdigest()
    #Convert hex hash representation to bin representation
    #Add leading 0's
    h_size = (iterations)      
    h = (bin(int(md5_, 16) % pow(2,iterations))[2:]).zfill(h_size)
    return h

def graph(iterations, ID=0):
    for i in range(2**iterations):
        x = bin(i)[2:] #delete 0b
        h = getHash(x, iterations)
        #Convert to int
        u = int(x, 2)
        v = int(h, 2)
        DG.add_edge(u, v) 

def getCycles():
    #Get cycles
    global cycles
    cycles_len = []
    cycles += list(nx.simple_cycles(DG))
    
    for i in cycles:
        cycles_len.append(len(i))
    
    print ("Cycles:\n  Number: %d\n  Min: %d\n  Max: %d\n  Average: %.3f" % (len(cycles_len), min(cycles_len), max(cycles_len), sum(cycles_len)/float(len(cycles_len))))    
 
def getTails():
    global tails
    tails_num = 0
    degree =  nx.degree(DG)  
    for key, value in degree.items():
        if value == 1:
            tails_num+=1
            tails.append(key)
    
    print ("Number of tails: %d" % tails_num) 

def pathInfo():
    global cycles
    cycles_nodes = []
    for i in cycles:
        for j in i:
            cycles_nodes.append(j)
    
    path_len = 1
    path_list = []
    path_nodes_length = []
    def path_length(node, path_len): 
        if (node in cycles_nodes):
            path_list.append(path_len)
        else:
            path_len+=1
            node = DG.neighbors(node)[0]
            path_length(node, path_len)        
            
    for i in tails:
        node = DG.neighbors(i)[0]
        path_length(node, path_len)   

    print ("Tail length:\n  Min: %d\n  Max: %d\n  Average: %.3f" % (min(path_list), max(path_list), sum(path_list)/float(len(path_list))))                                                                                                              

def getComponents():
    components = nx.number_connected_components(DG.to_undirected())
    print ("Components: %d" % components)

def Main():
    iterations = 16
    
    graph(iterations)
    getCycles()
    getTails()
    pathInfo()
    getComponents()
    
if __name__ == '__main__':
    Main()