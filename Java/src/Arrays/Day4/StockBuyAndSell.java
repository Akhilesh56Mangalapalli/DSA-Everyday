/*
Stock Buy and Sell - Multiple Transaction Allowed

The cost of stock on each day is given in an array price[]. 
Each day you may decide to either buy or sell the stock i at price[i], 
you can even buy and sell the stock on the same day. 
Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and 
multiple stocks cannot be held on any given day.
 * */

package Arrays.Day4;

public class StockBuyAndSell {
	public static void main(String[] args) {
		int[] prices= {100,180,260,310,40,535,695};
		// Call which ever function | Approach you like.
		System.out.print(stockbuysell(prices,0,prices.length-1));
		System.out.print(localminmax(prices));
		System.out.print(localminmaxUsingForLoop(prices));
		System.out.print(AcumulateProfit(prices));
		
	}
	
	/*
	- Brute force Approach | Using Recurrsion
    finding all possible profits and checking for max profits if found updates
    time complexity is exponentially increases with size of the array varies.
	 * */
	static int stockbuysell(int[] prices,int start,int end) {
		int sum=0;
		for(int i=start;i<end;i++) {
			for(int j=i+1;j<=end;j++) {
				if(prices[j]>prices[i]) {
					int curr_max=(prices[j]-prices[i])+stockbuysell(prices,start,i-1)+stockbuysell(prices,j+1,end);
					sum=Math.max(sum,curr_max);
				}
			}
		}
		return sum;
	}
	
	/*
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
	 * */
	
	static int localminmax(int[] prices) {
		int total=0;
		int n=prices.length;
		int local_minima=prices[0];
		int local_maxima=prices[0];
		int i=0;
		while(i<n-1) {
			while(i<n-1 && prices[i]>=prices[i+1]) {
					i++;
			}
			local_minima=prices[i];	
			while(i<n-1 && prices[i]<=prices[i+1]) {
				i++;
			}
			local_maxima=prices[i];
			total+=local_maxima-local_minima;
		}
		return total;
	}
	
	/*
	 * Same as above no change tried with for loop
	 * cause for loop is love!!
	 * */
	static int localminmaxUsingForLoop(int[] prices) {
		int total=0;
		int n=prices.length;
		int local_min=prices[0];
		int local_max=prices[0];
		
		for(int i=0;i<n-1;) {
			//loop to find local minima
			for(;i<n-1 && prices[i]>=prices[i+1];i++);
			local_min=prices[i];
			//loop to find local maxima
			for(;i<n-1&&prices[i]<=prices[i+1];i++);
			local_max=prices[i];
			total+=local_max-local_min;
		}
		return total;
	}
	
	/*
	Approach - 3 | Acumulate Maximum Profit Algorithm
    ------Optimized------
    Here we reduce number of condition by ignoring the profit drops
    we check stocks giving profit and add them to our total,
    if there found drop in profit, ignore it another profit found
    repeat till end of array and return total 
    Time Complexity: O(n)
    Space Complexity: O(1)
	 * */
	static int AcumulateProfit(int[] prices) {
		int total=0;
		int n=prices.length;
		for(int i=1;i<n;i++) {
			if(prices[i]>prices[i-1]) {
				total+=prices[i]-prices[i-1];
			}
		}
		return total;
	}
}
