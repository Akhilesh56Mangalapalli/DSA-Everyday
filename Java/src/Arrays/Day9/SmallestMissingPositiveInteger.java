package Arrays.Day9;

public class SmallestMissingPositiveInteger {

	public static void main(String[] args) {
		int[] arr1= {2,-3,4,1,1,7};
		int[] arr2= {5,3,2,5,1};
		int[] arr3= {-8,0,-1,-4,-3};
		int[] arr4= {1,2,3,4,5};
		System.out.print(UsingCycleSort(arr4));

	}
	
	/*
	CycleSort Approach
    
    iterate only over valid cases
    i.e., number lies between 1 and n
    swap if number is not in correct position
    ignore if there are duplicate elements already in position
    after applying sort check which first position is not correctly placed
    return position + 1
    if all placed correctly return n+1
    Time Complexity is O(n)
    Space Complexity is O(1)    
    */
	static int UsingCycleSort(int[] arr) {
		int n=arr.length;
		for(int i=0;i<n;i++) {
			while(1<=arr[i] && arr[i]<=n && arr[i]!=arr[arr[i]-1]) {
				int temp=arr[i];
				arr[i]=arr[arr[i]-1];
				arr[temp-1]=temp;
			}
		}
		for(int i=1;i<n;i++) {
			if(arr[i-1]!=i) {
				return i;
			}
		}
		return n+1;
		
	}

}
