#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        # select() takes arr[] and starting point of unsorted array i as 
        # input parameters and returns the selected element for each iteration 
        # in selection sort
        
        min_index = i 
        
        # find the min element index from the unsorted array 
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        
        return min_index
        
    
    def selectionSort(self, arr,n):
        #code here
        
        # start iteration
        for i in range(n):
            min_index = self.select(arr,i)
            # swap 
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
        return arr
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends