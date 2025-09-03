/*
Stock Buy and Sell - Max one Transaction Allowed

Given an array prices[] of length n, representing the prices of the stocks on different days. 
The task is to find the maximum profit possible by buying and selling the stocks on different days 
when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. 
If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
 * */

package Arrays.Day4;

public class SingleTransaction {

	public static void main(String[] args) {
		int[] prices= {61,44,70,78,73,95,27,1};
		System.out.print(singleTransactionProfit(prices));
		System.out.print(minSoFarMethod(prices));

	}
	/*	Brute Force Approach
	 * 	Time Complexity is O(n^2)
	 * 	Space Complexity is O(1)
	 * */
	static int bruteforce(int[] prices) {
		int n=prices.length;
		int res=0;
		for(int i=0;i<n;i++) {
			for(int j=i+1;j<n;j++) {
				res=Math.max(res,prices[j]-prices[i]);
			}
		}
		return res;
	}
	
	/*Approach - 1
	 * Two pointers approach
	 * Tracking left variable for minimum price
	 * Tracking right variable for maximum price
	 * finding maximum profit from them when left < right
	 * Time Complexity is O(n)
	 * Space Complexity is O(1)
	 * */
	
	static int singleTransactionProfit(int[] prices) {
		int left=0;
		int right=0;
		int total=0;
		for(int i=0;i<prices.length;i++) {
			if(prices[i]<prices[left]) {
				left=i;
			}
			else if(prices[i]>prices[right] || right<left) {
				right=i;
			}
			if(left<right) {
				total=Math.max(total, prices[right]-prices[left]);
			}
		}
		return total;
	}
	/* Tracking minimum so far and finding profit in each iteration
	 * and check with the previous profit if it greater update.
	 * Time Complexity O(n)
	 * Space Complexity O(1)
	 * */
	static int minSoFarMethod(int[] prices) {
		int n=prices.length;
		int res=0;
		int min=prices[0];
		for(int i=0;i<n;i++) {
			min=Math.min(min,prices[i]);
			res=Math.max(res,prices[i]-min);
		}
		return res;
	}
}
