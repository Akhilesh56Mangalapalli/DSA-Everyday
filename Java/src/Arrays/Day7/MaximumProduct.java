/*
Maximum Product Subarray

Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr[].
Note: It is guaranteed that the answer fits in a 32-bit integer.
 * */

package Arrays.Day7;

public class MaximumProduct {

	public static void main(String[] args) {
		int[] arr1= {-2, 6, -3, -10, 0, 2};
		int[] arr2= {-1, -3, -10, 0, 6};
		int[] arr3= {2, 3, 4};
		System.out.print(maximumProduct(arr1));
		System.out.print(greedyMinMax(arr2));
		System.out.print(TraversalMethod(arr3));
	}
	
	/*
	 Brute Force Approach
	 * finding all possible products and keep tracking maximum product
	 * Time complexity is O(n^2)
	 * Space Complexity is O(1)
    */
	static int maximumProduct(int[] arr) {
		int n=arr.length;
		int res=0;
		for(int i=0;i<n;i++) {
			int mul=arr[i];
			for(int j=i+1;j<n;j++) {
				mul*=arr[j];
				res=Math.max(mul, res);
			}
		}
		return res; 
	}
	
	/*
	 Greedy Min-Max Algorithm
	 * Keeping track of both minimum product and maximum product
	 * There are situations where both negative give greater max then current
	 * and find maximum product using both minimum and maximum then return
	 * Time complexity is O(n)
	 * Space Complexity is O(1)
	 */
	
	static int greedyMinMax(int[] arr) {
		int n=arr.length;
		int current_minimum=arr[0];
		int current_maximum=arr[0];
		int res=arr[0];
		for(int i=1;i<n;i++) {
			int temp=max(arr[i],current_maximum*arr[i],current_minimum*arr[i]);
			current_minimum=min(arr[i],current_minimum*arr[i],current_maximum*arr[i]);
			current_maximum=temp;
			res=max(res, current_maximum,current_minimum);
		}
		return res; 
	}
	static int max(int a, int b, int c) {
		return Math.max(a, Math.max(b, c));
	}
	static int min(int a, int b, int c) {
		return Math.min(a, Math.min(b, c));
	}
	
	/*
	Traversal Approach | Even or Odd 
	
	if there are even number of negative elements, then multiply complete array gives max product
    if there are odd  number of negative elements, then we need ignore one negative element
    to make number of negative numbers into even so that we max product
    it may be first negative number or last negative number in the array
    One of them gives maximum product, to find that
    we need traverse in both directions in one loop
    find max products with different variables
    if '0' is found in the traversal, change the subarray
    i.e., current product is updated as 1 (for both left and right traversal)     
    keep track of maximum product and return
    Time complexity is O(n)
    Space Complexity is O(1)
	 * */
	static int TraversalMethod(int[] arr) {
		int n=arr.length;
		int LeftToRight=arr[0];
		int RightToLeft=arr[0];
		int res=arr[0];
		for(int i=1;i<n;i++) {
			if(LeftToRight==0) {
				LeftToRight=1;
			}
			if(RightToLeft==0) {
				RightToLeft=1;
			}
			LeftToRight*=arr[i];
			int j=n-1-i;
			RightToLeft*=arr[j];
			res=max(res,LeftToRight,RightToLeft);	//max function is used from previous approach
		}
			
		return res;
	}
}
