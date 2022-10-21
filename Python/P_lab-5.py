#Edges to adjacency list of weighted undirected graph.
vertices = int(input("Enter  Number  of  vertices:  ")) 

adj_list = {} 

edges  =  int(input("Enter  number  of  edges:  "))

print("\nStart  Entering  edges  (s,d,w) : ")
for  i  in  range(edges): 
    v1,v2,w  =  list(map(int,input().split(" ")))
    
    if  v1  in  adj_list: 
        adj_list[v1].append((v2,w))
    else:
        adj_list[v1]  =  [(v2,w)] 
    
    if  v2  in  adj_list: 
        adj_list[v2].append((v1,w))
    else:
        adj_list[v2]  =  [(1,w)] 
    
    print("\nAdjacency  List  is:  ") 
    for  vertex  in  adj_list.keys(): 
        print(f"{vertex}  ->  {adj_list[vertex]}") 