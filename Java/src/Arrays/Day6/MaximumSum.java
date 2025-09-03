/*
 * Maximum Subarray Sum - Kadane's Algorithm
 * 
 * Given an integer array arr[], find the subarray (containing at least one element) 
 * which has the maximum possible sum, and return that sum.
 * Note: A subarray is a continuous part of an array.
 * */

package Arrays.Day6;

public class MaximumSum {

	public static void main(String[] args) {
		int[] arr= {2, 3, -8, 7, -1, 2, 3};
		System.out.println(maximumSum(arr));
		System.out.println(kadaneAlgorithm(arr));
	}
	/* Brute force Approach
	 * use 1st loop to start with every element in array
	 * add every other elements on each iteration and track maximum sum
	 * Time Complexity is O(n^2)
	 * Space Complexity is O(1)
	 * */
	static int maximumSum(int[] arr) {
		int n=arr.length;
		int res=arr[0];
		for(int i=0;i<n;i++) {
			int sum=arr[i];
			for(int j=i+1;j<n;j++) {
				sum+=arr[j];
				res=Math.max(sum, res);
			}
		}
		return res;
	}
	
	/*	Kadane's Algorithm
	 * 	Check the element adding to current max giving greater than that element
	 * 	if gives update it as current max, if not take that element as current max
	 * 	simultaneously track the resultant max and return in the end
	 * 	Time Complexity is O(n)
	 * 	Space complexity is O(1)
	 * */
	static int kadaneAlgorithm(int[] arr) {
		int n=arr.length;
		int max=arr[0];
		int res=arr[0];
		for(int i=1;i<n;i++) {
			max=Math.max(max+arr[i], arr[i]);
			res=Math.max(max,res);
		}
		return res;
	}

}
