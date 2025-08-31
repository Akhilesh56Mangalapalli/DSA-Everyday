/*NextPermutation
 * 
 * Given an array of integers arr[] representing a permutation (i.e., all elements are unique and 
 * arranged in some order), find the next lexicographically greater permutation by rearranging the elements of the array.
 * If such a permutation does not exist (i.e., the array is the last possible permutation), 
 * rearrange the elements to form the lowest possible order (i.e., sorted in ascending order).
 * */


package Arrays.Day3;

public class NextPermutation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr= {3,2,1}  ;
		nextPermutaion(arr);
		for(int i:arr) {
			System.out.print(i+" ");
		}
	}
	static void nextPermutaion(int[] arr) {
		int n=arr.length;
		int pivot=0;

		for(int i=n-2;i>=0;i--) {
			if(arr[i]<arr[i+1]) {
				pivot=i;

				break;
			}
		}
		
		for(int i=n-1;i>=0;i--) {
			if(pivot==0) {
				break;
			}
			else if(arr[i]>arr[pivot]) {
				arr[pivot]=arr[i];
				arr[i]=arr[pivot];
				break;
			}
		}
		if(pivot==0) {
			reversal(arr,0,n-1);
		}
		else {
			reversal(arr,pivot+1,n-1);
		}
		
	}
	static void reversal(int[] arr,int l,int r) {
		while(l<r) {
			int temp=arr[l];
			arr[l]=arr[r];
			arr[r]=temp;
			l++;
			r--;
		}
	}

}
