'''
Stock Buy and Sell - Max one Transaction Allowed

Given an array prices[] of length n, representing the prices of the stocks on different days. 
The task is to find the maximum profit possible by buying and selling the stocks on different days 
when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. 
If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''

class SingleTransaction:
    '''
    Brute Force Approach
	 * 	Time Complexity is O(n^2)
	 * 	Space Complexity is O(1)
    '''
    def bruteforce(self,prices):
        n=len(prices)
        res=0
        for i in range(n):
            for j in range(i+1,n):
                res=max(res, prices[j]-prices[i])

        return res

    '''
    Approach - 1
	 * Two pointers approach
	 * Tracking left variable for minimum price
	 * Tracking right variable for maximum price
	 * finding maximum profit from them when left < right
	 * Time Complexity is O(n)
	 * Space Complexity is O(1)
    '''
    def singleTransaction(self, prices):
        left=0
        right=0
        total=0
        for i in range(len(prices)):
            if prices[i]<prices[left]:
                left=i
            elif prices[i]>prices[right] or right<left:
                right=i
            if left<right:
                total=max(total,prices[right]-prices[left])
        
        return total
    
    '''
    Tracking minimum so far and finding profit in each iteration
	 * and check with the previous profit if it greater update.
	 * Time Complexity O(n)
	 * Space Complexity O(1)
    '''
    def minSoFar(self,prices):
        n=len(prices)
        res=0
        minima=prices[0]
        for i in range(n):
            minima=min(minima,prices[i])
            res=max(res,prices[i]-minima)
        return res

if __name__=="__main__":
    prices=[7, 10, 1, 3, 6, 9, 2]
    st=SingleTransaction()
    print(st.bruteforce(prices))
    print(st.singleTransaction(prices))
    print(st.minSoFar(prices))