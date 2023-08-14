#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        # note k starts from 1 i.e. the first element is at pos 1 
        # n = len(arr1)
        # m = len(arr2)
        # k = the kth element position in the final sorted array
        if n > m:  # to ensure arr1 is always the smaller array
            return self.kthElement(arr2, arr1, m, n, k)
        if n == 0:  # if arr1 is empty, then kth element is at index k-1 in arr2
            return arr2[k-1]  # kth element is at index k-1 in arr2
        if k == 1:  # if k is 1, then the smallest element is the minimum of the first elements of both arrays
            return min(arr1[0], arr2[0])
        i = min(n, k//2)  # to ensure we're not overshooting the kth position
        j = min(m, k//2)  # to ensure we're not overshooting the kth position
    
        if arr1[i-1] > arr2[j-1]:  # if arr1[i-1] is greater, it means we can discard the first j elements of arr2 because those elements are guaranteed to be smaller than the kth element
    
            # recursively call the function with a modified set of parameters where arr2 starts from index j and k is reduced by j
            return self.kthElement(arr1, arr2[j:], n, m-j, k-j)
        else:
            # recursively call the function with a modified set of parameters where arr1 starts from index i and k is reduced by i
            return self.kthElement(arr1[i:], arr2, n-i, m, k-i)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends