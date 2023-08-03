class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        # V - number of vertices 
        # an adjacency list adj where adj[i] is a list of lists containing 
        # two integers where the first integer of each list j denotes there 
        # is edge between i and j , second integers corresponds to the weight 
        # of that  edge.
        # S - source 
        
        # Initiation
        visited = {} # to keep track of the visited vertices
        distance = {} # to keep note of the shortest distance from S
        predecessor = {} # to keep track of the predecessor.
        
        # set initial values for visited to False, distance to infinity and 
        # predecessor to None 
        
        for v in range(V):
            visited[v] = False
            distance[v] = float('inf')
            predecessor[v] = None 
        
        # start jouney from first node 
        distance[S] = 0
        
        # iterate over all the vertices 
        for u in range(V):
            # find the minimum distance(from source) among the 
            # non visited vertices
            nextMind = float('inf')
            for v in range(V):
                if not visited[v] and distance[v]<nextMind:
                    nextMind = distance[v]
            
            # next based on the min distance chosse the vertex list
            nextvlist=[]
            for v in range(V):
                if not visited[v] and distance[v] == nextMind:
                    nextvlist.append(v)
            
            # boundary condition
            if nextvlist == []:
                break
            
            # choose the vertex to visit from the nextvlist
            nextv = min(nextvlist)
            visited[nextv] = True 
            
            # relax the adj nodes of the nextv
            for v,d in adj[nextv]:
                if not visited[v]:
                    if distance[v] > distance[nextv]+d:
                        distance[v] = distance[nextv]+d
                        predecessor[v] = nextv
        
        # output
        result=[]
        for v,d in distance.items():
            # list of tuples
            result.append(d)
        return result 
            
            
            
            
            
            
            
                    
            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends