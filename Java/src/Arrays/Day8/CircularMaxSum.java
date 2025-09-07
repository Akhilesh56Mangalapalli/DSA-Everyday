/*
Maximum Circular Subarray Sum

Given a circular array arr[], find the maximum sum of any non-empty subarray. 
A circular array allows wrapping from the end back to the beginning.
Note: A subarray may wrap around the end and continue from the beginning, 
forming a circular segment.
*/

package Arrays.Day8;

public class CircularMaxSum {

	public static void main(String[] args) {
		int[] arr1= {8, -8, 9, -9, 10, -11, 12};
		int[] arr2= {10, -3, -4, 7, 6, 5, -4, -1};
		int[] arr3= {5, -2, 3, 4};
		int[] arr4= {-1,-2,-3};
		System.out.print(maxSum(arr1));
		System.out.print(prefixSum(arr2));
		System.out.print(minKadane(arr3));
	}
	/*
	Brute force Approach
	
	traverse circularly, when index reached n, make it zero and continue
    or use % operator => j=j%n
    Time complexity is O(n^2)
    Space Complexity is O(1) 
	*/
	static int maxSum(int[] arr) {
		int n=arr.length;
		int res=arr[0];
		for(int i=0;i<n;i++) {
			int sum=arr[i];
			int j=i+1;
			for (int x=0;x<n-1;x++) {
				if (j==n) {
					j=0;
				}
				sum+=arr[j];
				res=Math.max(sum, res);
				j++;
			}
		}
		return res;
	}
	
	/*
	PrefixSum and Suffix Approach
	
    Here take an array of n+1 size and find suffix from (n-1)th position
    find the prefix sum and parallelly find the maximum sum using kadane's Algorithm
    summation of (i)th prefix value and (i+1)th suffix value gives the circular sum
    keep track of circular max, and normal max using kadane's algorithm
    return max between circular sum and normal sum
    Time Complexity is O(n)
    Space Complexity is O(n)
	*/
	static int prefixSum(int[] arr) {
		int n=arr.length;
		int[] suffix_Array=new int[n+1];
		for(int i=0;i<n+1;i++) {
			suffix_Array[i]=0;
		}
		suffix_Array[n-1]=arr[n-1];
		int sufsum=arr[n-1];
		int sufmax=arr[n-1];
		for(int i=n-2;i>=0;i--) {
			sufsum+=arr[i];
			sufmax=Math.max(sufsum, sufmax);
			suffix_Array[i]=sufmax;
		}
		int normalSum=arr[0];
		int currSum=0;
		int prefixSum=0;
		int CircularSum=arr[0];
		for (int i=0;i<n;i++) {
			currSum=Math.max(arr[i],currSum+arr[i]);
			normalSum=Math.max(normalSum, currSum);
			prefixSum+=arr[i];
			CircularSum=Math.max(CircularSum, prefixSum+suffix_Array[i+1]);
			
		}
		return Math.max(normalSum, CircularSum);
	}
	
	
	/*
	Kadane's Algorithm | Best Approach
	
    total_Sum=maximum_Sum+minimum_Sum
    find the minimum_sum and maximum sum using kadane's Algorithm 
    and find total sum of the array
    return totalSum-minimumSum which results maximum circular sum
    if minimum_kadane_sum is equal to total sum then return maximumKadaneSum
    Time complexity is O(n)
    Space Complexity is O(1)
    */
	static int minKadane(int[] arr) {
		int n=arr.length;
		int minsum=arr[0];
		int currsum=0;
		int normalSum=arr[0];
		int sum=0;
		int total=0;
		for(int i=0;i<n;i++) {
			currsum=Math.min(currsum+arr[i], arr[i]);
			minsum=Math.min(currsum,minsum);
			sum=Math.max(sum+arr[i],arr[i]);
			normalSum=Math.max(normalSum, sum);
			total+=arr[i];
		}
		if(total==minsum) {
			return normalSum;
		}
		return total-minsum;
				
	}

}
