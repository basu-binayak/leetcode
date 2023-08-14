#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		# x = base
        # n = exponent
        # m = modulo
        if n == 0:
            return 1
    
        temp = self.PowMod(x, n//2, m)  # recursive call
        temp = (temp * temp) % m  # square the result
    
        if n % 2 == 0:  # if n is even
            return temp
        else:
            return (x * temp) % m  # if n is odd
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends