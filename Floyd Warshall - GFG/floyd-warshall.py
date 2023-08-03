#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		rows, cols = len(matrix), len(matrix)
		
		distance = matrix
		for i in range(rows):
		        for j in range(cols):
		            if matrix[i][j]==-1:
		                distance[i][j]= float('inf')
		
		# run iteration for each vertex, taking each as source vertex
		for k in range(cols):
		    # run through the two dimensional array (matrix)
		    for i in range(rows):
		        for j in range(cols):
		            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
		
		for i in range(rows):
		        for j in range(cols):
		            if distance[i][j]==float('inf'):
		                distance[i][j]=-1
		return distance     
		


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends