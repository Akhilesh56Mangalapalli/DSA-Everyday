'''
Stock Buy and Sell - Multiple Transaction Allowed

The cost of stock on each day is given in an array price[]. 
Each day you may decide to either buy or sell the stock i at price[i], 
you can even buy and sell the stock on the same day. 
Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and 
multiple stocks cannot be held on any given day.
'''

class StockBuyAndSell:
    '''
    Brute force Approach
    Using Recurrsion
    finding all possible profits and checking for max profits if found updates
    time complexity is exponentially increases with size of the array varies.
    '''
    def maximumProfitUsingRecurrsion(self,prices,start,end)->int:
        total=0
        for i in range(start,end):
            for j in range(i+1,end+1):
                if prices[j]>prices[i]:
                    curr=(prices[j]-prices[i])+self.maximumProfitUsingRecurrsion(prices,start,i-1)+self.maximumProfitUsingRecurrsion(prices,j+1,end)
                    total=max(total,curr)
        return total
    
    '''
    Approach - 2 | Local Minima and Local Maxima Algorithm
    Initially, local minima and local maxima is taken as first index of array
    Here, in this approach if we observe increase in profit we will do nothing 
    it till it is going to decrease, index before decrease is taken as local maxima.
    same as maxima minima is calculated do nothing if stock values are decreasing
    until there starts increase, before index of increasing is taken as local minima
    After finding both claim the profit(max-min) and repeat the profit till end of array
    and return total profit
    Time Complexity : O(n)
    Space Complexity: O(1)
    '''
    def maximumProfit(self, prices) -> int:
        n=len(prices)
        total=0
        mimima=prices[0]
        maxima=prices[0]
        i=0
        while i<n-1:
            while i<n-1 and prices[i+1]<=prices[i]:
                i+=1
            minima=prices[i]
            while i<n-1 and prices[i+1]>prices[i]:
                i+=1
            maxima=prices[i]
            total+=maxima-minima
        return total

    '''
    Approach - 3 | Acumulate Maximum Profit Algorithm
    ------Optimized------
    Here we reduce number of condition by ignoring the profit drops
    we check stocks giving profit and add them to our total,
    if there found drop in profit, ignore it another profit found
    repeat till end of array and return total 
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def AcumulateProfit(self,prices)->int:
        total=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                total+=prices[i+1]-prices[i]

        return total
if __name__=="__main__":
    prices=[100,180,260,310,40,535,695]
    stock_obj=StockBuyAndSell()
    #Call which ever function | Approach you like.
    print(stock_obj.maximumProfitUsingRecurrsion(prices,0,len(prices)-1) ) 
    print(stock_obj.maximumProfit(prices))     
    print(stock_obj.AcumulateProfit(prices)) 
    
