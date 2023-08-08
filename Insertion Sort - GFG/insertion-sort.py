#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        
        key = alist[index]
        
        j = index-1
        while j>=0 and key<alist[j]:
            # swap
            alist[j],alist[j+1] = key, alist[j]
            j-=1
        
        return alist
        
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        
        for index in range(1,n):
            
            alist = self.insert(alist,index,n)
            
        return alist    


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends