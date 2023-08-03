#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        
        #initialize 
        distance = [100000000]*V # distance[i] denotes the shortest distance of vertex i from S
        distance[S] = 0
        
        
        # convert edges to adj list
        adjList = {}
        for v in range(V):
            adjList[v]=[]
        for element in edges:
            adjList[element[0]].append((element[1],element[2]))
        
        # loop and relax the edges repeatedly
        for _ in range(V):
            for u in range(V):
                for v,d in adjList[u]:
                    distance[v] = min(distance[v], distance[u]+d)
        
        # to detect a negative cycle 
        # test if the distance further reduces for any vertex then negative cycle present
        for u in range(V):
                for v,d in adjList[u]:
                    if distance[v] > distance[u]+d:
                        return [-1]
        
        return distance
        
        


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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends