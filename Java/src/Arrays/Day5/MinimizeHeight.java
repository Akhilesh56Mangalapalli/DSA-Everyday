/*Minimize the Heights II

Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers 
after you have modified each tower.

Note: It is compulsory to increase or decrease the height by k for each tower. 
After the operation, the resultant array should not contain any negative integers.
 * */

package Arrays.Day5;
import java.util.Arrays;
public class MinimizeHeight {

	public static void main(String[] args) {
		int[] heights= {3, 9, 12, 16, 20};
		int k=3;
		System.out.print(minimizeHeight(heights,k));
 		

	}
	/*	Draw and Understand the number line
	 * 	take a random possible position of i and analyze where are chances of maxima and minima
	 * 	Time Complexity is O(nlogn)
	 * 	Space Complexity is O(n)   because we are sorting the array
	 * */
	
	static int minimizeHeight(int[] heights,int k) {
		int n=heights.length;
		Arrays.sort(heights);
		int res=heights[n-1]-heights[0];
		for(int i=1;i<n;i++) {
			if(heights[i]-k<0) {
				continue;
			}
			int minHeight=Math.min(heights[0]+k, heights[i]-k);
			int maxHeight=Math.max(heights[n-1]-k, heights[i-1]+k);
			res=Math.min(res,maxHeight-minHeight);
			
		}
		return res;
			
	}
}
